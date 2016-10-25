import smtplib

class mailer(object):

    def __init__(self):
        pass

    def sendmailtoadmin(loggedinuser):
        gmail_user = 'inamdar.shuchir77@gmail.com'
        gmail_password = 'Calculator@17'

        emailfrom = gmail_user
        emailto = ['inamdar.shuchir@gmail.com', 'sinamda@gmail.com']
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