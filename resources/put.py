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

    #@jwt_required()
    def post (self):
        mail=request.args.get('mail')
        giorno=request.args.get('day')
        ora1=request.args.get('hour')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                time=datetime.now().date()
                ora=(datetime.now().time())
                data=str([time.year, time.month, time.day])
                orario=find_by_ora(user.classe_id, giorno, ora1)
                if orario:
                    riga=FriendModel.find_by_orario_id(user.id, orario.id)
                    if riga:
                        riga.data=data
                        riga.save_to_db()
                        return {"message":"subject put in bag"}, 200
                    newriga=FriendModel(None, user.id, orario.id, data)
                    newriga.save_to_db()
                    return {"message":"subject put in bag"}, 200
                return "slot hour does not exist", 500
            return "user has no class", 500
        return "user does not exist", 500


    #@jwt_required()
    def delete (self):
        mail=request.args.get('mail')
        giorno=request.args.get('day')
        ora1=request.args.get('hour')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                time=datetime.now().date()
                ora=(datetime.now().time())
                data=str([time.year, time.month, time.day])
                orario=find_by_ora(user.classe_id, giorno, ora1)
                if orario:
                    riga=FriendModel.find_by_orario_id(user.id, orario.id)
                    if riga:
                        riga.data=None
                        riga.save_to_db()
                        return {"message":"removed from bag"}, 200
                    return {"message":"subject was not in bag"}, 200
                return {"message":"slot hour does not exist"}, 500
            return "user has no class",500
        return "user does not exist", 500

    @jwt_required()
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
                    data1=str([time.year, time.month, time.day].timedelta(days=-1))

                    orari_id=find_id_by_giorno_id(user.classe_id, giorno)
                    messe=[]

                    for i in orari_id:
                        riga=FriendModel.find_by_orario_id(user.friend_id, i)
                        if riga:
                            if riga.data==data or riga.data==data1:
                                messe.append(i)
                    final=[]
                    for i in messe:
                        ore=TimetableModel.find_by_id(i)
                        final.append(ore.ora)
                    return {"messicompagno": final}, 200
                return "user has no mate", 500
            return "user has no class", 500
        return "user does not exist", 500
