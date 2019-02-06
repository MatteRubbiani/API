from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_id
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id
from models.subjects import SubjectModel, find_subject_id

class OrarioGiorno(Resource):


    def get(self):
        mail=request.args.get('mail')
        giorno=request.args.get('day')
        return[{"subject":"geometria","you":True, "yourMate":True}, {"subject":"italiano","you":False, "yourMate":True},{"subject":"ciao","you":False, "yourMate":True},{"subject":"banana","you":False, "yourMate":False}]
        user=UserModel.find_by_mail(mail)
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
                return[{"subject":"geometria","you":True, "yourMate":True}, {"subject":"italiano","you":False, "yourMate":True},{"subject":"ciao","you":False, "yourMate":True},{"subject":"banana","you":False, "yourMate":False}]
                    return {"elenco":elenco},200
                return {"elenco":""},200
            return {"message":"user has no class"}, 500
        return {"message":"user does not exist"},500
