from flask_restful import Resource, request
from models.users import UserModel, class_users
from models.classes import find_by_id, find_by_admin

class Mates (Resource):
    def get (self):
        data=request.get_json()
        mail=data[0]
        user=UserModel.find_by_mail(mail)
        if user:
            classe=user.classe_id
            if classe:
                users=class_users(classe)
                return  users
            return "user not in a class"
        return "user does not exist"
