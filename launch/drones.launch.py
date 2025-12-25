from simple_launch import SimpleLauncher, GazeboBridge
from ament_index_python.packages import get_package_share_directory
import yaml
import math

sl = SimpleLauncher(use_sim_time = True)
sl.declare_arg('gt', True, description = 'Whether to use ground truth localization')


def launch_setup():
    
    pkg_share_dir = get_package_share_directory('pisteur_drone_gazebo')
    config_file = pkg_share_dir + '/config/simulation.yaml'
    
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    drone_number = config['drone_number']
    shape = config['starting']['shape']
    spacing = config['starting']['spacing']
    altitude = config['starting']['altitude']
    center_x = config['starting']['center']['x']
    center_y = config['starting']['center']['y']
    center_z = config['starting']['center']['z']

    drones = []
    n = int(math.ceil(math.sqrt(drone_number)))
    for i in range(drone_number):
        row = i // n
        col = i % n
        x = center_x + (col - (n-1)/2) * spacing
        y = center_y + (row - (n-1)/2) * spacing
        z = center_z + altitude
        drones.append({'name': f'drone_{i}', 'x': x, 'y': y, 'z': z})
        
    
    for drone in drones:  
        ns = drone['name']
        with sl.group(ns=ns):

            # robot state publisher
            sl.robot_state_publisher('pisteur_drone_description', 'x3.urdf')

            # display thrusters in RViz
            sl.node('thruster_manager', 'publish_wrenches',
                    parameters = {'control_frame': f'{ns}/base_link'})
                        
            # URDF spawner to Gazebo, defaults to relative robot_description topic
            sl.spawn_gz_model(ns, spawn_args = f'-x {drone["x"]} -y {drone["y"]} -z {drone["z"]} -Y 0.'.split())
                
            # ROS-Gz bridges
            bridges = []
            gz_js_topic = GazeboBridge.model_prefix(ns) + '/joint_state'
            bridges.append(GazeboBridge(gz_js_topic, 'joint_states', 'sensor_msgs/JointState', GazeboBridge.gz2ros))
            
            # pose ground truth
            bridges.append(GazeboBridge(f'/model/{ns}/pose',
                                        'pose_gt', 'geometry_msgs/Pose', GazeboBridge.gz2ros))
            
            # imu
            for imu in ('mpu', 'lsm'):
                bridges.append(GazeboBridge(f'{ns}/{imu}',
                            f'{imu}_raw', 'sensor_msgs/Imu', GazeboBridge.gz2ros))

            # thrusters
            for thr in range(1, 7):
                thruster = f'thruster{thr}'
                gz_thr_topic = f'/{ns}/{thruster}/cmd'
                bridges.append(GazeboBridge(gz_thr_topic, f'cmd_{thruster}', 'std_msgs/Float64', GazeboBridge.ros2gz))
                            
            # ground truth to tf if requested
            if sl.arg('gt'):
                # odometry from Gz
                bridges.append(GazeboBridge(f'/model/{ns}/odometry_with_covariance',
                                        'odom', 'nav_msgs/Odometry', GazeboBridge.gz2ros, 'gz.msgs.Odometry'))

                sl.node('pose_to_tf',parameters={'child_frame': ns + '/base_link'})
            else:
                # otherwise publish ground truth as another link to get, well, ground truth
                sl.node('pose_to_tf',parameters={'child_frame': ns+'/base_link_gt'})

            sl.create_gz_bridge(bridges)
    
    return sl.launch_description()


generate_launch_description = sl.launch_description(launch_setup)
