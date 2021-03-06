from db import db
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.classes import ClassModel, find_by_tag
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id
from models.subjects import SubjectModel, find_subject_id

class CreateOrario(Resource):

    @jwt_required
    def post(self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        giorno=request.args.get('day')
        ora=request.args.get('hour')
        materia=request.args.get('subject')
        if user:
            if user.admin==True:
                    existing=find_by_ora(user.classe_id, giorno, ora)
                    materia_id=find_subject_id(user.classe_id, materia)
                    if existing:
                        if materia==None:
                            existing.materia_id=None
                            existing.save_to_db()
                            return {"message":"slot subject set to empty"}, 200
                        if materia_id:
                            existing.materia_id=materia_id.id
                            existing.save_to_db()
                            return {"message":"slot updated"},200
                        return {"message":"subject does not exist"}, 500
                    if materia==None:
                        nuovo=TimetableModel(None,user.classe_id, giorno, ora, None)
                        nuovo.save_to_db()
                        return {"message":"empty slot created"}, 200
                    if materia_id:
                        nuovo=TimetableModel(None,user.classe_id, giorno, ora, materia_id.id)
                        nuovo.save_to_db()
                        return {"message":"stot created successfully"}, 200
                    return {"message":"subject does not exist"},408
            return {"message":"user is not in a class or is not an admin"},405
        return {"message":"user does not exist"},402
