from flask_restful import Resource, request
from models.users import UserModel, class_mates
from models.classes import find_by_id
from flask_jwt_extended import jwt_required, get_jwt_identity

class Mates (Resource):
    @jwt_required
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            classe=user.classe_id
            if classe:
                users=class_mates(classe)
                a=[]
                for i in users:
                    a.append({"Username":i.username,
                              "Mail":"banana",
                              "IsAdmin":i.admin})
                return a, 200
            return "user not in a class", 500
        return "user does not exist", 500
