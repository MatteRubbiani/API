from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_admin, find_by_id
from models.users import UserModel, add_to_class
from models.subjects import SubjectModel, find_subject_id

class CreateSubject(Resource):

    @jwt_required()
    def post(self):
        data=request.get_json()
        mail=data[0]
        materia=data[1]
        user=UserModel.find_by_mail(mail)
        if user:
            if user.admin==True:
                    if find_subject_id(user.classe_id, materia):
                        return "subject already exists"
                    classe=find_by_id(user.classe_id)
                    materia_to_add=SubjectModel(None, classe.id, materia)
                    materia_to_add.save_to_db()
                    return "suject created successfully"
            return "user is not admin or is not in a class"
        return "user does not exist"

    def delete (self):
        data=request.get_json()
        mail=data[0]
        materia=data[1]
        user =UserModel.find_by_mail(mail)
        if user:
            if user.admin==True:
                test=find_subject_id(user.classe_id, materia)
                if test:
                    test.delete_from_db()
                    return "subject deleted successfully"
                return "subject does not exist"
            return "user is not admin or is not in a class"
        return "user does not exist"
