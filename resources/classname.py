from flask_jwt import jwt_required
from models.users import UserModel
from models.classes import ClassModel, find_by_id
from flask_restful import Resource, request
class ClassName(Resource):


    #@jwt_required()
    def get(self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            classe=find_by_id(user.classe_id)
            if classe:
                return classe.nome
            return {"message":"user has no class"}, 200
        return {"message":"user does not exist"}, 500
