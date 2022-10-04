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
### Mail ip
### 開發環境