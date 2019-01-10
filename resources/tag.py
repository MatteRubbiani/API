from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id, find_by_admin
from flask_restful import Resource, request
from flask_jwt import jwt_required
from models.randomtag import randomtag

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

    def post (self):
        data= request.get_json()
        mail=data[0]
        user=UserModel.find_by_mail(mail)
        if user:
            classe=find_by_id(user.classe_id)
            if classe:


                if (classe.admin_id == str(user.id)):
                    classe.tag=randomtag()
                    classe.save_to_db()
                    return classe.tag
                return "user is not admin"
            return "user not in a class"
        return "user does not exist"
