from flask_restful import Resource, reqparse, request
from flask_jwt import jwt_required
import datetime
from itsdangerous import URLSafeTimedSerializer
import smtplib

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


        link="https://smartmates.herokuapp.com/confirm/confirm/"+token

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


        return "user created, to be confirmed", 200
