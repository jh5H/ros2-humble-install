## 0. 터미네이터 설치

sudo apt install terminator -y


## 1. Locale 설정

locale

sudo apt update && sudo apt install locales

sudo locale-gen en_US en_US.UTF-8

sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

export LANG=en_US.UTF-8

locale

## 2. ROS2 Repo 추가

sudo apt install software-properties-common

sudo add-apt-repository universe

sudo apt update && sudo apt install curl -y

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

## 3. ROS2 humble 패키지 설치

sudo apt update && sudo apt upgrade

sudo apt install ros-humble-desktop

source /opt/ros/humble/setup.bash

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc


## 4. 테스트 명령어

ros2 run demo_nodes_cpp talker
ros2 run demo_nodes_py listener


## 5. 부가적 설치

sudo apt install -y python3-pip

pip3 install -U argcomplete

sudo apt install python3-colcon-common-extensions

sudo apt install git


## 6. workspace 생성

mkdir -p ~/ros2_ws/src


## 7. code 설치

sudo snap install code --classic

## 8. alias 세팅

gedit ~/.bashrc

아래 문장 추가
alias humble='source /opt/ros/humble/setup.bash && source install/setup.bash && source install/local_setup.bash'

alias cb='colcon build --packages-select'

alias cba='colcon build --symlink-install'

alias cbp='colcon build --symlink-install --packages-select'
