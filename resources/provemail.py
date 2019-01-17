import smtplib
from flask import url_for
from flask_restful import request, Resource
from itsdangerous import URLSafeTimedSerializer

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Prove(Resource):
    def get(self):
        data=request.get_json()
        mail=data[0]
        subject="ciao"

        s = URLSafeTimedSerializer("password1")
        token=s.dumps(mail, salt="emailconfirm")



        link="http://127.0.0.1:5000/"+token

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("smartmates2018@gmail.com", "cognento")
        text = """
    Hello!
    Thanks for signing up!
    Click the link below to confirm your email adress and start using your account!

    {}


    If you didn't ask for an account dont't worry, someone probably mispelt their email address.

    Team SmartMates


            """.format(link)
        server.sendmail("smartmates2018@gmail.com", mail, text)
