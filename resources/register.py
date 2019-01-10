from flask_restful import Resource, reqparse, request
from flask_jwt import jwt_required
import datetime


from db import db

from models.users import UserModel

class Register(Resource):



    def post(self):
        data=request.get_json()
        mail=data[0]
        username=data[1]
        password=data[2]
        user=UserModel.find_by_mail(mail)
        if user:
            return {"message":"mail already taken"}, 400

        now = datetime.datetime.now()

        user=UserModel(None, mail, username, password, None, None, now, None)

        user.save_to_db()
        return "user created successfully", 200
