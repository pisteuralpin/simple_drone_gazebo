# Pisteur's Drone - Gazebo integration package
Pisteur's Drone are ROS2 packages designed for simulating drones in a Gazebo environment. This package provides integration between the drone models and Gazebo simulator.

Drone models from [NovoG93/sjtu_drone](https://github.com/NovoG93/sjtu_drone/tree/ros2)

## Associated packages
- [pisteur_drone_description](https://github.com/pisteuralpin/pisteur_drone_description)
- [pisteur_drone_gazebo](https://github.com/pisteuralpin/pisteur_drone_gazebo)
- [pisteur_drone_control](https://github.com/pisteuralpin/pisteur_drone_control)
- [pisteur_drone_bringup](https://github.com/pisteuralpin/pisteur_drone_bringup)

## Features
- [ ] Gazebo bridges for drone control.

## Tested configuration
- ROS2 Kilted
- Gazebo Harmonic

# Usage
To launch the Gazebo simulation, use the following command:
```bash
ros2 launch pisteur_drone_gazebo start_gz.launch.py
```