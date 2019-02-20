from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.users import UserModel

class IsInClass (Resource):

    @jwt_required
    def post (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            if user.classe_id:
                return{"message":True}
            return {"message":False}
        return "user does not exist", 402
