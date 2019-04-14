#### 项目介绍


#### 软件架构

#### 安装教程


位置: 120.79.223.29:8000



netstat -tunlp|grep 8000
python3 manage.py runserver 0.0.0.0:8000
nohup python3 manage.py runserver 0.0.0.0:8000 &

nohup python -m SimpleHTTPServer 80 &

数据库启动命令
systemctl start mariadb  #启动MariaDB
systemctl stop mariadb  #停止MariaDB
systemctl restart mariadb  #重启MariaDB
systemctl enable mariadb  #设置开机启动

安装模块的命令
pip3 install Django
pip3 install pymysql
pip3 install django_crontab  # 系统定时任务模块

pip3 install apscheduler  # python 定时任务模块
pip3 install django-apscheduler

pip3 install requests
pip3 install bs4

pip3 install django-cors-headers  # 跨域

安装数据库的命令
python3 manage.py makemigrations
python3 manage.py migrate

D:\Anaconda3\envs\python36\python manage.py runserver_plus --cert server.crt localhost:8000
python36 manage.py runserver_plus --cert server.crt 0.0.0.0:8000
python36 manage.py runserver 0.0.0.0:8000

## 安装
pip install git+git://github.com/sshwsfc/xadmin.git@django2

pip install django-werkzeug-debugger-runserver

pip install django_extensions

#### 使用说明

1. xxxx
2. xxxx
3. xxxx

#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)