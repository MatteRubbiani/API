from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_tag
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id
from models.subjects import SubjectModel, find_subject_id

class CreateOrario(Resource):

    #@jwt_required()
    def post(self):
        data=request.get_json()
        mail=data[0]
        giorno=data[1]
        ora=data[2]
        materia=data[3]
        user=UserModel.find_by_mail(mail)
        if user:
            if user.admin==True:
                    existing=find_by_ora(user.classe_id, giorno, ora)
                    materia_id=find_subject_id(user.classe_id, materia)
                    if existing:
                        if materia=="":
                            existing.materia_id=""
                            existing.save_to_db()
                            return "slot subject set to empty"
                        if materia_id:
                            existing.materia_id=materia_id.id
                            existing.save_to_db()
                            return "slot updated"


                        return "subject does not exist"

                    if materia=="":
                        nuovo=TimetableModel(None,user.classe_id, giorno, ora, "")
                        nuovo.save_to_db()
                        return "empty slot created"


                    if materia_id:
                        nuovo=TimetableModel(None,user.classe_id, giorno, ora, materia_id.id)
                        nuovo.save_to_db()
                        return "stot created successfully"
                    return "subject does not exist"
            return "user is not in a class or is not an admin"
        return "user does not exist"
