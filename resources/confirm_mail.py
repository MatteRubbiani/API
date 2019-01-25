import smtplib
from flask_restful import Resource
from itsdangerous import URLSafeTimedSerializer
from models.users import UserModel



class ConfirmMail (Resource):
    def get (self, token):
        s = URLSafeTimedSerializer("password1")
        try:
            mail=s.loads(token, salt="emailconfirm")
            user=UserModel.find_by_mail(mail)
            if user.confirmed==False:
                user.confirmed=True
                user.save_to_db()
                return "user confirmed"
            return "user already confirmed"

        except:
            return "your token is expired"
