import smtplib
from flask import url_for
from flask_restful import request, Resource
from itsdangerous import URLSafeTimedSerializer
from models.users import UserModel



class ConfirmMail (Resource):




    def get (self, token):
        s = URLSafeTimedSerializer("password1")
        mail=s.loads(token, salt="emailconfirm", max_age=1800)
        user=UserModel.find_by_mail(mail)
        if user:
            if user.confirmed==False:
                user.confirmed=True
                user.save_to_db()
                return "user confirmed"
            return "MELA"
        return "banana"
