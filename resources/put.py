from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required
from datetime import datetime

from models.classes import ClassModel, find_by_tag
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id, find_id_by_giorno_id
from models.subjects import SubjectModel, find_subject_id
from models.friends import FriendModel

class Put (Resource):

    @jwt_required
    def post (self):
        data=request.get_json()
        mail=data[0]
        giorno=data[1]
        ora1=data[2]
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                time=datetime.now().date()
                ora=(datetime.now().time())
                data=str([time.year, time.month, time.day, ora.hour])
                orario=find_by_ora(user.classe_id, giorno, ora1)
                if orario:
                    riga=FriendModel.find_by_orario_id(user.id, orario.id)
                    if riga:
                        riga.data=data
                        riga.save_to_db()
                        return "subject put in bag"
                    newriga=FriendModel(None, user.id, orario.id, data)
                    newriga.save_to_db()
                    return "slot created, subject put in bag"
                return "slot hour does not exist"
            return "user has no class"
        return "user does not exist"


    @jwt_required
    def delete (self):
        data=request.get_json()
        mail=data[0]
        giorno=data[1]
        ora1=data[2]
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                time=datetime.now().date()
                ora=(datetime.now().time())
                data=str([time.year, time.month, time.day, ora.hour])
                orario=find_by_ora(user.classe_id, giorno, ora1)
                if orario:
                    riga=FriendModel.find_by_orario_id(user.id, orario.id)
                    if riga:
                        riga.data=None
                        riga.save_to_db()
                        return "removed from in bag"
                    return "subject was removed from bag"
                return "slot hour does not exist"
            return "user has no class"
        return "user does not exist"

    @jwt_required
    def get (self):
        data=request.get_json()
        mail=data[0]
        giorno=data[1]
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                if user.friendship==True:
                    time=datetime.now().date()
                    ora=(datetime.now().time())
                    data=str([time.year, time.month, time.day, ora.hour])

                    orari_id=find_id_by_giorno_id(user.classe_id, giorno)
                    messe=[]

                    for i in orari_id:
                        riga=FriendModel.find_by_orario_id(user.friend_id, i)
                        if riga:
                            if riga.data==data:
                                messe.append(i)
                    final=[]
                    for i in messe:
                        ore=TimetableModel.find_by_id(i)
                        final.append(ore.ora)
                    return final
                return "user has no mate"
            return "user has no class"
        return "user does not exist"
