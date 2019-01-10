from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id
from flask_restful import Resource, request
from flask_jwt import jwt_required

class Tag (Resource):
    def get (self):
        data= request.get_json()
        mail=data[0]
        user=UserModel.find_by_mail(mail)
        if user:

            classe=find_by_id(user.classe_id)
            if classe:
                return classe.tag
            return "user not in a class"
        return "user does not exist"
