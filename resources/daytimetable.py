from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_id
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id
from models.subjects import SubjectModel, find_subject_id

class OrarioGiorno(Resource):

    #@jwt_required()
    def get(self):
        data=request.get_json()
        mail=data[0]
        giorno=data[1]
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                materie_id=find_by_giorno_id(user.classe_id, giorno)

                if materie_id:
                    elenco=[]
                    for i in materie_id:
                        materia=SubjectModel.find_by_id(i)
                        #return materie_id
                        if i=="":
                            elenco.append("")
                        else:
                            elenco.append(materia.materia)


                    return elenco
                return "user has no subjects today"
            return "user has no class"
        return "user does not exist"
