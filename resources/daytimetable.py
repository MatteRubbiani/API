from db import db
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.classes import ClassModel, find_by_id
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id
from models.subjects import SubjectModel, find_subject_id

class OrarioGiorno(Resource):

    @jwt_required
    def get(self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        giorno=request.args.get('day')
        if user:
            if user.classe_id:
                materie_id=find_by_giorno_id(user.classe_id, giorno)
                if materie_id:
                    elenco=[]
                    for i in materie_id:
                        materia=SubjectModel.find_by_id(i)
                        if i=="":
                            elenco.append("")
                        else:
                            elenco.append(materia.materia)

                    return {"elenco":elenco},200
                return {"elenco":""},200
            return {"message":"user has no class"}, 500
        return {"message":"user does not exist"},500
