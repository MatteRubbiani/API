from flask_restful import Resource, request
import datetime
from itsdangerous import URLSafeTimedSerializer
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from db import db

from models.users import UserModel

class Register(Resource):



    def post(self):
        data=request.get_json()
        mail=data[0]
        username=data[1]
        password=data[2]
        user=UserModel.find_by_mail(mail)
        #if user:
            #return "mail already taken", 400

        now = datetime.datetime.now()

        user=UserModel(None, mail, username, password, None, None, now, None, False, False)

        user.save_to_db()

        s = URLSafeTimedSerializer("password1")
        token=s.dumps(mail, salt="emailconfirm")

        link="http://127.0.0.1:5000/confirm/"+token
        #link="https://smartmates.herokuapp.com/confirm/"+token

        text = """
/n/n
Hello!
Thanks for signing up!
Click the link below to confirm your email adress and start using your account!


{}

If you didn't ask for an account don't worry, someone probably mispelt their email address.


Kind Regards,

Team SmartMates


         """.format(link)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("smartmates2018@gmail.com", "smartmates1")
        server.sendmail("smartmates2018gmail.com", mail, text)

        return "user created, to be confirmed", 200



        """fromaddr = "smartmates2018@gmail.com"
        toaddr = mail
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Confirm your account on SmartMates"
        body = text
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("smartmates2018@gmail.com", "smartmates1")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)"""
