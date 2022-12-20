
#### 
* [Google Vision API example](https://ikala.cloud/cloud-automl-vision-application-1/)
* [GCP class](https://github.com/jumbokh/gcp_class/tree/master/VISION)
* [使用 Bing 影像搜尋](https://learn.microsoft.com/zh-tw/azure/cognitive-services/bing-image-search/quickstarts/python)
#### search url update:
#### search_url = "https://api.bing.microsoft.com/v7.0/images/search"
#### [Face recognition with OpenCV, Python, and deep learning](https://pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)
#### [How to (quickly) build a deep learning image dataset](https://pyimagesearch.com/2018/04/09/how-to-quickly-build-a-deep-learning-image-dataset/)
#### [Mediapipe](https://github.com/8-DK/MediapipeUsefullNotebooks)
## Machine Learning 使用 Tensorflow2 and Keras
##
#### https://github.com/klauspa/Yolov4-tensorflow
* Yolov4-tensorflow $ python detect.py --image ./data/000000493952.jpg 
#### https://pjreddie.com/darknet/yolo/
* darknet $ ./darknet detect cfg/yolov3.cfg yolov3.weights ../cocoimg/000000528299.jpg
### [Tensorflow 2 入門](https://github.com/czy36mengfei/tensorflow2_tutorials_chinese)
### [官方教材](https://github.com/czy36mengfei/tensorflow2_tutorials_chinese)
### [簡單粗暴 TensorFlow 2 ](https://tf.wiki/zh_hant/)
### [第一章 簡報](https://github.com/jumbokh/class1091/blob/master/ML/docs/tf2-class.pptx)
### [第二章 簡報](https://github.com/jumbokh/class1091/blob/master/ML/docs/CH02.ppt)
### [第三章 簡報](https://github.com/jumbokh/class1091/blob/master/ML/docs/CH03a.ppt)
##
### [Lab for TF2](https://github.com/jumbokh/class1091/tree/master/ML/MMSLAB-TF2/MMSLAB-TF2)
##
* [DonkeyCar for PiRacer Pro](https://pan.baidu.com/s/1xvlqA2Ct0mxiUfOzekcFaA) 
#### 提取密碼: wsdz
### Default Login
```
login: pi
password: raspbarry
```
### 系統安裝
* [參考1.](https://github.com/jumbokh/rpi_class/tree/master/Linux2021#readme)
* [微雪wiki](https://www.waveshare.net/wiki/PiRacer_AI_Kit)
* [docx](https://github.com/jumbokh/csu1111-class/blob/main/robots/%E6%A8%B9%E8%8E%93%E6%B4%BE%E5%85%A5%E9%96%80%E6%95%99%E6%9D%90.docx)
* [交大講義](https://github.com/jumbokh/csu1111-class/blob/main/robots/Raspberry%20Pi_day%201.pdf)
### Kali Linux
### [kali for Raspberry pi](https://linuxhint.com/install_kali_linux_raspberry_pi_4/)
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install kali-linux-everything
sudo dpkg-reconfigure locales
中文化, 參考 https://github.com/jumbokh/Network-class/blob/main/kaliChinese.md
```
* ![github list](https://github.com/jumbokh/csu1111-class/blob/main/robots/images/Github-list.jpg)
### 首次設定
* [first time](https://github.com/jumbokh/rpi_class/blob/master/Installation/first_time_setting.md)

#### [UBUNTU 安裝ssh](https://www.ewdna.com/2012/06/ubuntu-ssh-server.html)
```
要安裝 ssh server, 以下兩行指令都可以
# apt-get install ssh
# apt-get install openssh-server

安裝後可以修改一些 ssh 的設定, 如port, 密碼認證, root登入等
# vim /etc/ssh/sshd_config
Port 22
PasswordAuthentication yes
PermitRootLogin yes -> 是否開放 root 登入

更改完存檔後記得重啟服務
# /etc/init.d/ssh restart
```
#### [遠端桌面連線](https://www.ichiayi.com/tech/ubuntu_xrdp)
```
sudo apt install xfce4 xrdp
echo xfce4-session > ~/.xsession
sudo vi /etc/xrdp/startwm.sh
```
```
:
if test -r /etc/profile; then
        . /etc/profile
fi

startxfce4
test -x /etc/X11/Xsession && exec /etc/X11/Xsession
exec /bin/sh /etc/X11/Xsession
sudo service xrdp restart
netstat -na | grep 3389
```
#### 中文設定
```
sudo apt-get install  language-pack-zh-han*
sudo apt install $(check-language-support)
sudo apt-get install font-manager
更改預設為中文環境
sudo vi /etc/default/locale
LANG="zh_TW.UTF-8"
LANGUAGE="zh_TW:zh:en_US:en"
sudo vi /etc/environment
LANG="zh_TW.UTF-8"
LANGUAGE="zh_TW:zh"
LC_NUMERIC="zh_TW"
LC_TIME="zh_TW"
LC_MONETARY="zh_TW"
LC_PAPER="zh_TW"
LC_NAME="zh_TW"
LC_ADDRESS="zh_TW"
LC_TELEPHONE="zh_TW"
LC_MEASUREMENT="zh_TW"
LC_IDENTIFICATION="zh_TW"
LC_ALL="zh_TW.UTF-8"
sudo dpkg-reconfigure locales
選擇 zh_TW.UTF-8 UTF-8

sudo fc-cache -fv
重新開機讓設定生效
```
### Jupyter-Lab 安裝
* [Reference 1](https://medium.com/analytics-vidhya/jupyter-lab-on-raspberry-pi-22876591b227)
* [Reference 2](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
#### 準備
<pre>
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo pip3 install setuptools
$ sudo apt install libffi-dev
$ sudo pip3 install cffi
</pre>
#### 安裝 jupyterlab
* pip3 install jupyterlab
<pre>
$ mkdir notebooks
$ jupyter lab --notebook-dir=~/notebooks
</pre>
#### Setup Jupyter lab as a service
<pre>
$ which jupyter-lab
/home/pi/.local/bin/jupyter-lab
</pre>
#### Create Service
<pre>
$ sudo nano /etc/systemd/system/jupyter.service
</pre>
##
<pre>
[Unit]
Description=Jupyter Lab
[Service]
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/bin/bash -c "/home/pi/.local/bin/jupyter-lab --ip="0.0.0.0" --no-browser --notebook-dir=/home/pi/notebooks"
User=pi
Group=pi
WorkingDirectory=/home/pi/notebooks
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
</pre>
##
<pre>
$ sudo systemctl enable jupyter.service
$ sudo systemctl daemon-reload
</pre>
##
#### Add password
<pre>
jupyter notebook --generate-config
</pre>
#### 產生config檔：/home/pi/.jupyter/jupyter_notebook_config.py
<pre>
jupyter notebook password
# $ jupyter notebook password
# Enter password:  ****
# Verify password: ****
# [NotebookPasswordApp] Wrote hashed password to /Users/you/.jupyter/jupyter_notebook_config.json
</pre>
##
<pre>
<file:/home/pi/.jupyter/jupyter_notebook_config.py>
...
ExecStart=/bin/bash -c "/usr/local/bin/jupyter-lab --no-browser --notebook-dir=/home/pi/notebooks"
...
</pre>
##
### Mail ip [gmail 認證密碼](https://github.com/jumbokh/csu1111-class/blob/main/robots/gmailAuth.md)
* [Reference 1](https://github.com/jumbokh/raspberrypi-get-ip)
#### Install and configure msmtp
<pre>
sudo apt-get install msmtp msmtp-mta
</pre>
####  add your credentials:  `~/.msmtprc` or `$XDG_CONFIG_HOME/msmtp/config`
```
# Generics
defaults
auth           on
tls            on
# following is different from ssmtp:
tls_trust_file /etc/ssl/certs/ca-certificates.crt
# user specific log location, otherwise use /var/log/msmtp.log, however, 
# this will create an access violation if you are user pi, and have not changes the access rights
logfile        ~/.msmtp.log

# Gmail specifics
account        gmail
host           smtp.gmail.com
port           587

from          root@raspi-buster
user           your-gmail-accountname@gmail.com
password       your-gmail-account-password

# Default
account default : gmail
```
#### chmod 600 ~/.msmtprc
#### Test it:

```
$ echo "Hello world!" | msmtp you@example.com
```
## Create the email sending script

Create a file named `mail_ip.sh` (or whatever you prefer) and edit it adding your email address:

```
mailto="you@example.com"
ip=`ip route list | awk '{print NR,$(NF-2)}'`

{
	echo To: $mailto
       	echo "Subject: [RasPi] My IP"
	echo "$ip"
} | /usr/bin/msmtp $mailto
echo "$ip"
echo "Finished running at `date`"
```
#### change file to executable mode
```
$ chmod +x mail_ip.sh
$ ./mail_ip.sh
```
## Set your script to run on reboot

There are different ways to do this, we'll use `crontab` here.

```
$ crontab -e
```

Add the following line to the end of the file (make sure to use the absolute path to the script):

```
MAILTO=you@example.com
@reboot sleep 120 && /home/pi/mail_ip.sh > /home/pi/mail_ip.log 2>&1
```
##
### 開發環境
#### 安裝 Node-Red [參考](https://atceiling.blogspot.com/2019/07/raspberry-pi-51node-reddashboard.html)
```
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
```
#### 安裝 nodejs
```
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
node -v
npm -v
```
* 手動
```
sudo apt-get install nodejs-legacy
sudo apt-get install npm
```
#### 安裝 node red
```
sudo npm install -g --unsafe-perm node-red node-red-admin 
```
#### 啟動
```
node-red-pi --max-old-space-size=256
```
* 或
```
node-red-start
```
* 瀏覽器輸入: http://ip:1880  例； http://192.168.1.128:1880
#### 設定開機啟動
* sudo systemctl enable nodered.service
#### 安裝 dashboard
```
$ node-red-stop
$ cd ~/.node-red
$ npm install node-red-dashboard
```
* http://192.168.1.128:1880/ui
