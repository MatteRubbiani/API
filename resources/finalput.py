from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required
from datetime import datetime

from models.classes import ClassModel, find_by_tag
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id, find_id_by_giorno_id
from models.subjects import SubjectModel, find_subject_id
from models.friends import FriendModel


class FinalPut(Resource):
    def get (self):
        mail=request.args.get('mail')
        giorno=request.args.get('day')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                if user.friendship==True:
                    time=datetime.now().date()
                    ora=(datetime.now().time())
                    data=str([time.year, time.month, time.day])
                    data1=str([time.year, time.month, (time.day-1)])

                    orari_id=find_id_by_giorno_id(user.classe_id, giorno)
                    mate=[]
                    for i in orari_id:
                        riga=FriendModel.find_by_orario_id(user.friend_id, i)
                        if riga:
                            if riga.data==data or riga.data==data1:
                                mate.append(True)
                            else:
                                mate.append(False)

                    you=[]
                    for i in orari_id:
                        riga=FriendModel.find_by_orario_id(user.id, i)
                        if riga:
                            if riga.data==data or riga.data==data1:
                                you.append(True)
                            else:
                                you.append(False)

                    materie_id=find_by_giorno_id(user.classe_id, giorno)
                    elenco=[]
                    if materie_id:
                        for i in materie_id:
                            if i:
                                materia=SubjectModel.find_by_id(i)
                                elenco.append(materia.materia)
                            else:
                                elenco.append(None)
                    final=[]

                    for i in range(len(elenco)):
                        try:
                            a=you[i]
                        except:
                            a=False
                        try:
                            b=mate[i]
                        except:
                            b=False
                        final.append({"subject":elenco[i],
                                      "you":a,
                                      "mate":b})


                    return final
                return "user has no mate", 500
            return "user has no class", 500
        return "user does not exist", 500