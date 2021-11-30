# gameweb
Web service for game.
use django

Nginx+Gunicorn+Supervisor 部署 Django
fabric自动化部署
相关信息见doc文件下


安装python3.6
安装可能的依赖
yum install -y openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
yum install mysql-devel
yum install python-devel
yum install -y python36-devel
下载源码
wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
tar -zxvf Python-3.6.4.tgz
cd Python-3.6.4
./configure LD_RUN_PATH=/usr/lib LDFLAGS="-L/usr/lib" CPPFLAGS="-I/usr/include"
make LD_RUN_PATH=/usr/lib
make install

安装pip
yum -y install python3-pip
强制安装pip
pip install -U --force-reinstall pip
hash -r
安装django
pip3 install Django -i https://pypi.tuna.tsinghua.edu.cn/simple
启动django
python3 manage.py runserver 0.0.0.0:8000
安装mysql驱动
pip3 install pymysql


安装虚拟环境
pip install --force-reinstall pipenv
pip install --force-reinstall dataclasses
pip install --force-reinstall wheel
pip install --force-reinstall mysqlclient
pip uninstall Setuptools
pip install --force-reinstall setuptools==57.5.0
pip install --upgrade setuptools==57.5.0
pip install demjson==2.2.4
pipenv --python 3.6 install --upgrade setuptools==57.5.0
pipenv --python 3.6 install demjson==2.2.4
pipenv --python 3.6 install --deploy --ignore-pipfile -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py collectstatic --noinput

pip install supervisor
== 创建日志目录
mkdir /home/slgweb/supervisor/var/log
sudo chmod 777 /home/slgweb/supervisor/var
== 终端启动
pipenv run python manage.py runserver 0.0.0.0:8001
== 后台方式启动
pipenv run supervisord -c /home/slgweb/supervisord.conf
supervisorctl -c /home/slgweb/supervisord.conf  restart wasteland
supervisorctl -c /home/slgweb/supervisord.conf  stop wasteland
== 网页样式混乱
setting.py中DEBUG选项为True

django
django日志
使用django开发、调试时，如果log使用了RotatingFileHandler输出日志，当第一个日志文件写满(设置了每个日志文件为5MB）产生第二个文件时，会出现如下的错误，导致无法生成后续的日志文件：
Django RotatingFileHandler产生的错误：PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。
使用python manager.py runserver --noreload


安装mysqlclient报错：MySQLdb/_mysql.c:501: error: ‘MYSQL_DEFAULT_AUTH’ undeclared， mysql版本过低，不支持mysql5.1，安装mysql5.7或更高


export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv

部署需要改的配置
1. mysql配置，搜索 "django.db.backends.mysql"
2. supervisord.conf 里面的路径配置
3. 后台配置, 搜索"BACK_STAGE"