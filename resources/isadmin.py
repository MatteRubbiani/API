from flask_restful import Resource, request
from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id
from flask_jwt import jwt_required

class IsAdmin (Resource):
    @jwt_required()
    def get (self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            return {"message":user.admin}, 200
        return {"message":"user does not exist"}, 500
