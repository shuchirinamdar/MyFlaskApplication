import pygal

from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required
from celery import Celery
import smtplib

from webapp.extensions import cache
from webapp.forms import LoginForm
from webapp.models import User
from webapp.models import Charts

app = Flask(__name__)

gmail_user = 'emailid@gmail.com'
gmail_password = 'password'

emailfrom = gmail_user
emailto = ['receiver1', 'receiver2']

main = Blueprint('main', __name__)
simple_page = Blueprint('simple_page', __name__, template_folder='simple')

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    graph_Data = getHalfGaugeChartData()
    return render_template("index.html", graph_Data=graph_Data)
    pass

def getHorizontalGraphData():
    chartOb = Charts()
    userLogData = Charts.getUserLogStats(chartOb)

    # Horizontal Bar charts
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'User login counts'

    for element in userLogData:
        line_chart.add(element[0], element[1])

    graph_Data = line_chart.render_data_uri()
    return graph_Data
    pass

def getHalfGaugeChartData():
    chartOb = Charts()
    userLogData = Charts.getUserLogStats(chartOb)

    gauge = pygal.SolidGauge(
        half_pie=True, inner_radius=0.70,
        style=pygal.style.styles['default'](value_font_size=10))

    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter

    for element in userLogData:
        gauge.add(str(element[0]), [{'value': element[1], 'max_value': 100}],
                  formatter=percent_formatter)

    graph_Data = gauge.render_data_uri()
    return graph_Data
    pass

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        try:
            #Send Async mail
            send_async_email.apply_async(countdown=60)
            #send_async_email()
        except:
            flash("Error occured! Check the redis server.")
        return redirect(request.args.get("next") or url_for(".home"))


    return render_template("login.html", form=form)

@main.route("/pygalChart/")
def pygalChart():
    graph_Data = getHorizontalGraphData()
    return render_template("pygalChart.html", graph_Data = graph_Data)

@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")

    return redirect(url_for(".home"))


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200

@celery.task
def send_async_email():
    """Background task to send an email with Flask-Mail."""
    subject = 'OMG Super Important Message'
    body = 'User login detected'

    email_text = """\
            From: %s
            To: %s
            Subject: %s
            %s
            """ % (emailfrom, ", ".join(emailto), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(emailfrom, emailto, email_text)
        server.close()
        print 'Email sent!'
    except:
        print 'Something went wrong...'