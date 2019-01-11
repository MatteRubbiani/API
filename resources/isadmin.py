from flask_restful import Resource, request
from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id, find_by_admin

class IsAdmin (Resource):
    def get (self):
        data =request.get_json()
        mail=data[0]
        user=UserModel.find_by_mail(mail)
        if user:
            classe=find_by_id(user.classe_id)
            if classe:
                if classe.admin_id==str(user.id):
                    return True

        return False 
