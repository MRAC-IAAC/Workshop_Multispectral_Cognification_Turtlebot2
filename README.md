# MRAC Multispectral Cognification workshop

## Hardware
- Turtlebot 2  
- Slamtec A2M8 lidar   
- Orbecc Astra  
- Flir Lepton 3.5  
- Pure Thermal2 board  


## ROS install
Follow instructions [here](http://wiki.ros.org/noetic/Installation/Ubuntu)  
Install ros-noetic-desktop-full
Install catkin tools
```shell
sudo apt install python3-catkin-tools
```
install all dependencies
```shell
sudo apt install libuvc-dev ros-noetic-rgbd-launch ros-noetic-joy ros-noetic-openni2-launch ros-noetic-gmapping ros-noetic-gmapping ros-noetic-slam-gmapping ros-noetic-move-base ros-noetic-amcl ros-noetic-navigation v4l-util
```
- create a catkin workspace  
- clone this repo to the source folder

```shell
rosdep install --from-paths src --ignore-src -r -y
```

```shell
catkin build
```
---
## Required ROS packages

### Asta camera
install dependencies
```shell
sudo apt install libuvc-dev
sudo apt install ros-noetic-rgbd-launch
```
clone pkg to ws
```shell
git clone https://github.com/orbbec/ros_astra_camera
```

### Turtlebot 2

install dependencies
```shell
sudo apt install ros-noetic-joy ros-noetic-openni2-launch ros-noetic-gmapping ros-noetic-slam-gmapping ros-noetic-move-base ros-noetic-amcl ros-noetic-navigation ros-$ROS_DISTRO-realsense2-camera
```
```shell
git clone https://github.com/turtlebot/turtlebot.git
git clone https://github.com/turtlebot/turtlebot_apps.git
git clone https://github.com/yujinrobot/kobuki.git
git clone https://github.com/yujinrobot/yujin_ocs
```
In the turtlebot_apps pkg, delete turtlebot_follower
In the yujin_ocs pkg, delete everything except 'yocs_cmd_vel_mux', 'yocs_controllers', and 'yocs_velocity_smoother'.

```shell
rosdep install --from-paths src --ignore-src -r -y
```
### Realsense
Follow instructions [here](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md#installing-the-packages)
```shell
sudo apt install ros-$ROS_DISTRO-realsense2-camera
```

launch
```shell
roslaunch realsense2_camera rs_camera.launch
roslaunch realsense2_camera rs_camera.launch filters:=pointcloud
roslaunch realsense2_camera rs_camera.launch clip_distance:=2
```
See GitHub page for more launch parameters

### Lepton PureThermal
install dependencies
```shell
sudo apt install v4l-utils
```
Set udev rules
```shell
sudo sh -c "echo 'SUBSYSTEMS==\"usb\", ATTRS{idVendor}==\"1e4e\", ATTRS{idProduct}==\"0100\", SYMLINK+=\"pt1\", GROUP=\"usb\", MODE=\"666\"' > /etc/udev/rules.d/99-pt1.rules"
sudo service udev reload
sudo service udev restart
```
Determine index of Lepton_pt, and set index /lepton_pt_capture/scripts/capture.py
```shell
v4l2-ctl --list-devices

```
and look for 
```shell
Video Capture 255 (usb-0000:00:14.0-1):
	/dev/video0
	/dev/video1
	/dev/media0
```

### laser_assembler
usage astra turtlebot
```shell
roslaunch laser_assembler ptcl2_assembler.launch
rosrun laser_assembler ptcl2_assembler
```

usage realsense
```shell
roslaunch laser_assembler ptcl2thermal_assembler.launch
rosrun laser_assembler ptcl2_assembler
```
