from db import db
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.classes import ClassModel, find_by_id
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id
from models.subjects import SubjectModel, find_subject_id


class OrarioTotale(Resource):

    @jwt_required
    def get(self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            if user.classe_id:
                orario2=TimetableModel.find_all_by_classe_id(user.classe_id)
                orario1=sorted(orario2, key=lambda x: int(x.giorno_id) if x.giorno_id is not None  else 0)
                orario=sorted(orario1, key=lambda x:  int(x.ora) if x.ora is not None  else 0)
                a=[]
                b={}
                for i in range(1,8):
                    a=[]
                    for x in orario:
                        if x.giorno_id==i:
                            a.append(x.materia_id)
                    materie=[]
                    for y in a:
                        materia=SubjectModel.find_by_id(y)
                        if materia:
                            if materia.materia:
                                materie.append(materia.materia)
                        else:
                            materie.append("")
                    b.update({i: materie})
                return b
