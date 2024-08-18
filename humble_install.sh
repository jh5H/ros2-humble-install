echo "This script will install ros humble on your PC"
echo ""
echo "PRESS [ENTER] TO CONTINUE THE INSTALLATION"
echo "IF YOU WANT TO CANCEL, PRESS [CTRL] + [C]"
echo ""
echo ""
read

locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings


sudo apt install software-properties-common -y
sudo add-apt-repository universe -y

sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update

sudo apt upgrade -y

sudo apt install ros-humble-desktop -y

sudo apt install ros-dev-tools -y

sudo apt install ros-humble-rqt-* -y

sudo apt install ros-humble-rmw-cyclonedds-cpp -y

sudo apt install terminator -y

sudo apt install -y python3-pip

pip3 install -U argcomplete

sudo apt install python3-colcon-common-extensions -y

sudo apt install git -y


source /opt/ros/humble/setup.bash

sudo rosdep init
rosdep update

sh -c "echo \"source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash\" >> ~/.bashrc"
sh -c "echo \"source /usr/share/vcstool-completion/vcs.bash\" >> ~/.bashrc"
sh -c "echo \"source /usr/share/colcon_cd/function/colcon_cd.sh\" >> ~/.bashrc"

sh -c "echo \"export ROS_DOMAIN_ID=0\" >> ~/.bashrc"
sh -c "echo \"export ROS_LOCALHOST_ONLY=0\" >> ~/.bashrc"
sh -c "echo \"export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp\" >> ~/.bashrc"

sh -c "echo \"alias cbp='colcon build --symlink-install --packages-select'\" >> ~/.bashrc"
sh -c "echo \"alias rosdinstall='rosdep install -y -r -q --from-paths src --ignore-src --rosdistro'\" >> ~/.bashrc"
sh -c "echo \"alias humble='source /opt/ros/humble/setup.bash && source ./install/setup.bash && source ./install/local_setup.bash'\" >> ~/.bashrc"

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}==== Finish && Delete file ===="
echo -e "==== good luck to you ===="

cd ~
rm -rf ~/ros2_humble_install/
cd
