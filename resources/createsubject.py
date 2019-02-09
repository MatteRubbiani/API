from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_admin, find_by_id
from models.users import UserModel, add_to_class
from models.subjects import SubjectModel, find_subject_id
from models.timetable import TimetableModel

class CreateSubject(Resource):

    #@jwt_required()
    def post(self):
        mail=request.args.get('mail')
        materia=request.args.get('subject')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.admin==True:
                    if find_subject_id(user.classe_id, materia):
                        return {"message":"subject already exists"}, 500
                    classe=find_by_id(user.classe_id)
                    materia_to_add=SubjectModel(None, classe.id, materia)
                    materia_to_add.save_to_db()
                    return {"message":"suject created successfully"}, 200
            return {"message":"user is not admin or is not in a class"}, 500
        return {"message":"user does not exist"}, 500

    #@jwt_required()
    def delete (self):
        mail=request.args.get('mail')
        materia=request.args.get('subject')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.admin==True:
                subject=find_subject_id(user.classe_id, materia)
                if subject:
                    slots=TimetableModel.find_by_materia_id(subject.id)
                    for i in slots:
                        i.materia_id=None
                        i.save_to_db()
                    subject.delete_from_db()
                    return {"message":"subject deleted successfully"},200
                return {"message":"subject does not exist"}, 500
            return {"message":"user is not admin or is not in a class"},500
        return {"message":"user does not exist"}, 500
