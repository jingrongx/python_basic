操作系统 Ubuntu 18.04

# 安装Python3
apt instll python3

# 查看python版本
~ $ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 

# 安装pip3
sudo apt-get install python3-pip

# 安装虚拟环境
pip3 install virtualenv

# 创建虚拟环境 .env
python3 -m virtualenv .env

# 激活虚拟环境
source .env/bin/activate

# 安装需要的python模块
pip install *

# 退出虚拟环境
deactivate