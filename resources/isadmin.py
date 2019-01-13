from flask_restful import Resource, request
from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id

class IsAdmin (Resource):
    def get (self):
        data =request.get_json()
        mail=data[0]
        user=UserModel.find_by_mail(mail)
        if user:
            return user.admin
        return "user does not exist"