### Google-> 管理你的帳戶
![安全性](https://github.com/jumbokh/csu1111-class/blob/main/robots/images/secure1.PNG)
### 安全性-->應用程式密碼
![應用程式](https://github.com/jumbokh/csu1111-class/blob/main/robots/images/secure2.PNG)
### 選取應用程式
![選取應用程式](https://github.com/jumbokh/csu1111-class/blob/main/robots/images/secure3.PNG)
### 選取裝置
![選取裝置](https://github.com/jumbokh/csu1111-class/blob/main/robots/images/secure4.PNG)
### 取名
![取名](https://github.com/jumbokh/csu1111-class/blob/main/robots/images/secure5.PNG)
### 系統產生密碼
![密碼](https://github.com/jumbokh/csu1111-class/blob/main/robots/images/secure6a.PNG)
### 修改 `~/msmtprc`
'''
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
'''
