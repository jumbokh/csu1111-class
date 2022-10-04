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
Test it:

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
