from db import db
from flask_restful import Resource, request

from itsdangerous import URLSafeTimedSerializer
import smtplib
import hashlib, uuid

class ConfirmPassword(Resource):


    def post(self):
        link=request.args.get('link')
        psw1=request.args.get('password')
        psw2=request.args.get('password1')
        return psw1
        hashed_password = hashlib.sha512(epsw).hexdigest()
        if psw1==pws2:
            token=link[47:]
            s = URLSafeTimedSerializer("password1")
            mail=s.loads(token, salt="emailconfirm")
            return token
