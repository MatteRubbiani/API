from flask_restful import Resource, request
from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id, find_by_admin
from flask_jwt import jwt_required

class GotMate (Resource):
    @jwt_required
    def get (self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.friendship==True:
                    return {"frienship":True},200
            if user.friend_id:
                return {"message":"friendship requested"}, 200
            return{"message": False}, 200
        return {"message": "user does not exist"}, 500
