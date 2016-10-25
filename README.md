Problem Statement
Develop a flask application using Flask Foundation template (hint: use cookiecutter, db can be either mysql/postgres) with the following features:
  1. Email admin(random hard coded email is fine) every time user logs in using async task queue with IP of the user. Free to use email api like mandrill or sparkpost API instead of using a mail server or use gmail SMTP and log this data on db.
  2. Plot various kinds of charts using the data that you stored in point a. and serve it on homepage(use D3/C3, google charts, its fine to use highcharts but refrain from using it).
  3.Bonus points for using frontend MVC like Angular/React or backbone but not required.

Flask Foundation Template imported from
    URL: : https://github.com/JackStouffer/Flask-Foundation.git

Environment Setup:
IDE: JetBrains PyCharm
    Most of the required flask extensions required for the project are mentioned in requirements.txt file and PyCarms should be able to setup the environment using this file.

Below are some additional packages required for the project:
1. Install cookiecutter
      pip install cookiecutter
2. Celery
      pip install celery
3. Redis server: to support async calls from celery
      Download from https://github.com/ServiceStack/redis-windows/raw/master/downloads/redis-latest.zip
      Extract redis64-latest.zip in any folder, e.g. in c:\redis
      Run the redis-server.exe using the local configuration
	      cd c:\redis
	      redis-server.exe redis.windows.conf
4. Upon opening the project in  PyCharm
      1. Set the “manage.py” script as the run configuration
      2. Add parameter “server” to the run configuration
