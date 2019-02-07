from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_tag
from models.randomtag import randomtag
from models.users import UserModel

class CreateClass(Resource):


    def post(self):
        mail=request.args.get('mail')
        classe=request.args.get('class')
        user=UserModel.find_by_mail(mail)
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
