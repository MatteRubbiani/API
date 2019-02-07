from flask_restful import Resource, request
import datetime
from itsdangerous import URLSafeTimedSerializer
import smtplib
import hashlib, uuid


from db import db

from models.users import UserModel

class Register(Resource):
    def post(self):
        mail=request.args.get('mail')
        username=request.args.get('username')
        password=request.args.get('password')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.confirmed==True:
                return "mail already taken", 400
        now = datetime.datetime.now()
        epsw=password.encode('utf-8')
        hashed_password = hashlib.sha512(epsw).hexdigest()
        user=UserModel(None, mail, username, hashed_password, None, None, now, False, False, False)
        user.save_to_db()
        s = URLSafeTimedSerializer("password1")
        token=s.dumps(mail, salt="emailconfirm")
        #link="http://127.0.0.1:5000/confirm/"+token
        link="https://smartmates.herokuapp.com/confirm/"+token
        subject="Confirm your account on SmartMates"

        text = """

Hi {}!
Thanks for signing up!
Click the link below to confirm your email adress and start using your account!


{}

If you didn't ask for an account don't worry, someone probably misspelt their email address.


Kind Regards,

Team SmartMates


         """.format(username,link)
        message = 'Subject: {}\n\n{}'.format(subject, text)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        server.login("smartmates2018@gmail.com", "smartmates1")
        #server.sendmail("smartmates2018gmail.com", mail, message)

        return "user created, to be confirmed", 200
