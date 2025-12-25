# Pisteur's Drone - Gazebo integration package
Pisteur's Drone are ROS2 packages designed for simulating drones in a Gazebo environment. This package provides integration between the drone models and Gazebo simulator.

Drone models from [NovoG93/sjtu_drone](https://github.com/NovoG93/sjtu_drone/tree/ros2)

## Associated packages
- [pisteur_drone_description](https://github.com/pisteuralpin/pisteur_drone_description)
- [pisteur_drone_gazebo](https://github.com/pisteuralpin/pisteur_drone_gazebo) (this package)

## Features
- [x] Start Gazebo with a predefined world
- [x] Spawn multiple drones models in the Gazebo simulation

## Tested configuration
- ROS2 Kilted
- Gazebo Harmonic

# Usage
To launch the Gazebo simulation, use the following command:
```bash
ros2 launch pisteur_drone_gazebo start_gz.launch.py
```

To spawn drones in the simulation, run the following command:
```bash
ros2 launch pisteur_drone_gazebo drones.launch.py
```