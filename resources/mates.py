from flask_restful import Resource, request
from models.users import UserModel, class_mates
from models.classes import find_by_id
from flask_jwt import jwt_required

class Mates (Resource):
    #@jwt_required()
    def get (self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
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
