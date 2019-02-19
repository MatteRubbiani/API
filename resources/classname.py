from flask_jwt_extended import jwt_required, get_jwt_identity
from models.users import UserModel
from models.classes import ClassModel, find_by_id
from flask_restful import Resource, request
class ClassName(Resource):


    @jwt_required
    def get(self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            classe=find_by_id(user.classe_id)
            if classe:
                return {"username":classe.nome}
            return {"message":"user has no class"}, 200
        return {"message":"user does not exist"}, 500
