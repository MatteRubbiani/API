from models.users import UserModel
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity

class Name(Resource):
    @jwt_required
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            return {"username":user.username}, 200
        return {"meassege":"user does not exist"}, 402
