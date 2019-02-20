from flask_restful import Resource, request
from models.users import UserModel, class_mates
from models.classes import find_by_id
from flask_jwt_extended import jwt_required, get_jwt_identity

class Admins (Resource):
    @jwt_required
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            classe=user.classe_id
            if classe:
                users=class_mates(classe)
                a=""
                for i in users:
                    if i.admin==True:
                        a=a+i.username+","
                b=a[:-1]
                return {"username":b}, 200
            return "user not in a class", 403
        return "user does not exist", 500
