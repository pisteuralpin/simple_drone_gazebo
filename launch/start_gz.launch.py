from simple_launch import SimpleLauncher
from ament_index_python.packages import get_package_share_directory
import os

sl = SimpleLauncher(use_sim_time=True)
sl.declare_arg('gui', True)
sl.declare_arg('rviz', False)
full_world = sl.find('simple_drone_gazebo', 'flat.sdf')


def launch_setup():

    gz_args = '-r' if sl.arg('gui') else '-r -s'

    if os.path.exists(full_world):
        sl.gz_launch(full_world, gz_args)
    else:
        sl.gz_launch(sl.find('simple_drone_gazebo', 'world.sdf'), gz_args)
        sl.save_gz_world(full_world, 5.)

    # display in RViz
    if sl.arg('rviz'):
        sl.rviz(sl.find('simple_drone_description', 'x3.rviz'))

    return sl.launch_description()


generate_launch_description = sl.launch_description(launch_setup)
