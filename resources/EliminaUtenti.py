from models.users import UserModel, class_users, find_friend_by_username
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity



class EliminaUtenti(Resource):

    def delete (self):
        a=UserModel.find_all()
        for i in a:
            i.delete_from_db()
