import smtplib
from flask_restful import Resource
from itsdangerous import URLSafeTimedSerializer
from models.users import UserModel
import os.path
from flask_restful import Resource
from flask import Flask, Response



class ConfirmMail (Resource):
    def get (self, token):
        def root_dir():
            return os.path.abspath(os.path.dirname(__file__))

        def get_file(filename):
            try:
                src = os.path.join(root_dir(), filename)
                return open(src).read()
            except IOError as exc:
                return str(exc)
        s = URLSafeTimedSerializer("password1")
        try:
            mail=s.loads(token, salt="emailconfirm")
            user=UserModel.find_by_mail(mail)
            if user.confirmed==False:
                user.confirmed=True
                user.save_to_db()

                content = get_file('userConfirmed.html')
                return Response(content, mimetype="text/html")

            content = get_file('userAlreadyConfirmed.html')
            return Response(content, mimetype="text/html")
        except:
            if token:
                content = get_file('tokenExpired.html')
                return Response(content, mimetype="text/html")
            content = get_file('noToken.html')
            return Response(content, mimetype="text/html")
