from flask_restful import Resource, request
from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id
from flask_jwt_extended import jwt_required, get_jwt_identity

class IsAdmin (Resource):
    #@jwt_required()
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            return {"message":user.admin}, 200
        return {"message":"user does not exist"}, 500
