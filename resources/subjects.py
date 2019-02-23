from flask_restful import Resource, request
from models.users import UserModel, class_mates
from models.classes import find_by_id
from models.subjects import find_by_classe_id
from flask_jwt_extended import jwt_required, get_jwt_identity

class GetSubjects (Resource):
    @jwt_required
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:

            return find_by_classe_id(user.classe_id), 403
        return "user does not exist", 402
