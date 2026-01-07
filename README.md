# Simple Drone - Gazebo integration package
[![ROS2](https://img.shields.io/badge/ROS2-Jazzy-green)](https://docs.ros.org/en/jazzy/index.html)
[![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-orange)](http://gazebosim.org/)
[![License](https://img.shields.io/badge/License-GNU--3..0-blue)](#license)

Simple Drone are ROS2 packages designed for simulating drones in a Gazebo environment. This package provides integration between the drone models and Gazebo simulator.

Drone models by [OpenRobotics on Gazebo Fuel](https://app.gazebosim.org/OpenRobotics/fuel/models/X3%20UAV)

## Associated packages
- [simple_drone_description](https://github.com/pisteuralpin/simple_drone_description)
- [simple_drone_gazebo](https://github.com/pisteuralpin/simple_drone_gazebo) (this package)

## Features
- [x] Start Gazebo with a predefined world
- [x] Spawn multiple drones models in the Gazebo simulation

## Tested configuration
- ROS2 Kilted
- Gazebo Harmonic

# Installation
1. Be sure to have ROS2 Jazzy and Gazebo Harmonic installed and configured on your system.
2. Clone the repository into your ROS2 workspace:
   ```bash
   cd ~/ros2_ws/src
   git clone https://github.com/pisteuralpin/simple_drone_gazebo.git
    ```
3. Clone simple_drone_description package if not already done:
   ```bash
   git clone https://github.com/pisteuralpin/simple_drone_description.git
   ```
4. Clone simple_launch, thruster_manager and pose_to_tf packages if not already done:
   ```bash
   git clone https://github.com/oKermorgant/simple_launch.git
   git clone https://github.com/CentraleNantesROV/thruster_manager.git
   git clone https://github.com/oKermorgant/pose_to_tf.git
   ```
5. Build your ROS2 workspace:
   ```bash
   cd ~/ros2_ws
   colcon build --symlink-install
   ```
6. Source your workspace:
   ```bash
   source ~/ros2_ws/install/setup.bash
   ```

# Usage
To launch the Gazebo simulation, use the following command:
```bash
ros2 launch simple_drone_gazebo start_gz.launch.py
```

To spawn drones in the simulation, run the following command:
```bash
ros2 launch simple_drone_gazebo drones.launch.py
```
You can modify the number of drones and their initial positions in the `config/simulation.yaml` file.