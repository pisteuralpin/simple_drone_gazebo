# Simple Drone - Gazebo integration package
Simple Drone are ROS2 packages designed for simulating drones in a Gazebo environment. This package provides integration between the drone models and Gazebo simulator.

Drone models from [NovoG93/sjtu_drone](https://github.com/NovoG93/sjtu_drone/tree/ros2)

## Associated packages
- [simple_drone_description](https://github.com/simple_drone/simple_drone_description)
- [simple_drone_gazebo](https://github.com/simple_drone/simple_drone_gazebo) (this package)

## Features
- [x] Start Gazebo with a predefined world
- [x] Spawn multiple drones models in the Gazebo simulation

## Tested configuration
- ROS2 Kilted
- Gazebo Harmonic

# Usage
To launch the Gazebo simulation, use the following command:
```bash
ros2 launch simple_drone_gazebo start_gz.launch.py
```

To spawn drones in the simulation, run the following command:
```bash
ros2 launch simple_drone_gazebo drones.launch.py
```