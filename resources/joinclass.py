from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_tag
from models.randomtag import randomtag
from models.users import UserModel, add_to_class, find_friend_by_username

class JoinClass(Resource):

    #@jwt_required()
    def post(self):
        data=request.get_json()
        mail=data[0]
        tag=data[1]
        user=UserModel.find_by_mail(mail)
        if user:
            classe=find_by_tag(tag)
            if classe:
                mate= find_friend_by_username(classe.id, user.username)
                if mate:
                    return "change name"

                user.classe_id=classe.id
                user.save_to_db()
                return {"message": "user added to class succesfully"}, 200

            return {"message":"class does not exist"},400
        return {"message":"user does not exist"},400

        #ricorda di aggiungere che automaticamente si crea l'orario

    def delete (self):
        data=request.get_json()
        mail=data[0]
        user=UserModel.find_by_mail(mail)
        if user:
            user.classe_id=None
            user.save_to_db()

            return {"message": "user removed from class correctly"}, 200
        return {"message": "user does not exist"}, 400
