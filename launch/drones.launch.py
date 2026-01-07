from simple_launch import SimpleLauncher, GazeboBridge
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import yaml
import math

sl = SimpleLauncher(use_sim_time = True)
sl.declare_arg('gt', True, description = 'Whether to use ground truth localization')


def launch_setup():
    
    pkg_share_dir = get_package_share_directory('simple_drone_gazebo')
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
    
    # Spawn drones in a grid
    for i in range(drone_number):
        row = i // n
        col = i % n
        x = center_x + (col - (n-1)/2) * spacing
        y = center_y + (row - (n-1)/2) * spacing
        z = center_z + altitude
        drones.append({'name': f'drone_{i}', 'x': x, 'y': y, 'z': z})
        
        drone_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([pkg_share_dir, '/launch/spawn_drone.launch.py']),
            launch_arguments={'x': str(x), 'y': str(y), 'z': str(z), 'ns': f'drone_{i}'}.items()
        )
        
        sl.add_action(drone_launch)
            
    
    return sl.launch_description()


generate_launch_description = sl.launch_description(launch_setup)
