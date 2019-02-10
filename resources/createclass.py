from db import db
from flask_restful import Resource, request
#from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.classes import ClassModel, find_by_tag
from models.randomtag import randomtag
from models.users import UserModel
from security import identity

class CreateClass(Resource):


    @jwt_required
    def post(self):
        mail=request.args.get('mail')
        classe=request.args.get('class')
        token=request.headers.get('Authorization')
        return get_jwt_identity()
        #return get_jwt_identity()

        #return request.headers.get('Authorization')
        #user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                return "You are already in a class"
            tag=randomtag()
            class_to_add=ClassModel(None, tag, None, classe)
            class_to_add.save_to_db()
            class_added=find_by_tag(tag)
            user.admin=True
            user.classe_id=class_added.id
            user.save_to_db()
            return {"tag":tag}
        return {"message":"user does not exist"},400
