#!/bin/bash

# 设置安装路径
INSTALL_DIR=/usr/local/amazon_monitor

# 下载程序压缩包
wget https://github.com/yunze7373/ammonitor/releases/download/v1.0.1/amazon_monitor.tar

# 创建安装目录
sudo mkdir -p $INSTALL_DIR

# 解压程序到安装目录
sudo tar -xf amazon_monitor.tar -C $INSTALL_DIR --strip-components=1

# 安装依赖库
sudo apt-get update
sudo apt-get install python3-pip -y
sudo pip3 install -r $INSTALL_DIR/requirements.txt

# 启动程序
sudo python3 $INSTALL_DIR/amazon_monitor.py
