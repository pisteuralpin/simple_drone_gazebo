# Simple Drone - Gazebo integration package
[![ROS2](https://img.shields.io/badge/ROS2-Jazzy-green)](https://docs.ros.org/en/jazzy/index.html)
[![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-orange)](http://gazebosim.org/)
[![License](https://img.shields.io/badge/License-GNU--3..0-blue)](#license)

Simple Drone are ROS2 packages designed for simulating drones in a Gazebo environment. This package provides integration between the drone models and Gazebo simulator.

Drone models by [OpenRobotics on Gazebo Fuel](https://app.gazebosim.org/OpenRobotics/fuel/models/X3%20UAV)

## Associated packages
- [simple_drone_description](https://github.com/simplealpin/simple_drone_description)
- [simple_drone_gazebo](https://github.com/simplealpin/simple_drone_gazebo) (this package)

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