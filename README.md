#Flask Foundation

Flask Foundation is a solid foundation for flask applications, built with best practices, that you can easily construct your website/webapp off of. Flask Foundation is different from most Flask frameworks as it does not assume anything about your development or production environments. Flask Foundation is platform agnostic in this respect.

Develop a flask application using Flask Foundation template (hint: use cookiecutter, db can be either mysql/postgres) with the following features:
1. Email admin(random hard coded email is fine) every time user logs in using async task queue with IP of the user. Free to use email api like mandrill or sparkpost API instead of using a mail server or use gmail SMTP and log this data on db.
Plot various kinds of charts using the data that you stored in point a. and serve it on homepage(use D3/C3, google charts, its fine to use highcharts but refrain from using it).
Bonus points for using frontend MVC like Angular/React or backbone but not required.
