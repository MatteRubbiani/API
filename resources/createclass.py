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
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        classe=request.args.get('classe')
        if user:
            if user.classe_id:
                return{"message": "You are already in a class"}, 407
            tag=randomtag()
            class_to_add=ClassModel(None, tag, None, "classe")
            class_to_add.save_to_db()
            class_added=find_by_tag(tag)
            user.admin=True
            user.classe_id=class_added.id
            user.save_to_db()
            return {"tag":tag}
        return {"message":"user does not exist"},402
