from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_admin, find_by_tag
from models.randomtag import randomtag
from models.users import UserModel, add_to_class

class CreateClass(Resource):

    #@jwt_required()
    def post(self):
        data=request.get_json()
        mail=data[0]
        classe=data[1]
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                return {"message": "you are already in a class"}

            tag=randomtag()
            class_to_add=ClassModel(None, tag, user.id, None, classe)
            class_to_add.save_to_db()
            class_added=find_by_tag(tag)
            add_to_class(mail, class_added.id)
            return {"class tag": tag}, 200
        return {"message":"user does not exist"},400
