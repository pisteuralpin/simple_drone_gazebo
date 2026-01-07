from simple_launch import SimpleLauncher, GazeboBridge
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


sl = SimpleLauncher(use_sim_time = True)
sl.declare_arg('x', True, description = 'Initial X position of the drone')
sl.declare_arg('y', True, description = 'Initial Y position of the drone')
sl.declare_arg('z', True, description = 'Initial Z position of the drone')
sl.declare_arg('ns', True, description = 'Namespace of the drone')


def launch_setup():
    x = sl.arg('x')
    y = sl.arg('y')
    z = sl.arg('z')
    ns = sl.arg('ns')
    
    with sl.group(ns=ns):
        # robot state publisher
        sl.robot_state_publisher('simple_drone_description', 'x3.urdf')

        # display thrusters in RViz
        sl.node('thruster_manager', 'publish_wrenches',
                parameters = {'control_frame': f'{ns}/base_link'})
                    
        # URDF spawner to Gazebo, defaults to relative robot_description topic
        sl.spawn_gz_model(ns, spawn_args = f'-x {x} -y {y} -z {z} -Y 0.'.split())
            
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
