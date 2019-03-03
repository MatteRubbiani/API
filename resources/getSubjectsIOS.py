from db import db
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

from models.classes import ClassModel, find_by_tag
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id, find_id_by_giorno_id
from models.subjects import SubjectModel, find_subject_id
from models.friends import FriendModel

class PutIOS (Resource):

    @jwt_required
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        giorno=request.args.get('day')
        if user:
            if user.classe_id:
                time=datetime.now().date()
                ora=(datetime.now().time())
                data=str([time.year, time.month, time.day])
                data1=str([time.year, time.month, (time.day-1)])

                orari=TimetableModel.find_by_classe_id(user.classe_id, giorno)

                if orari:
                    final=[]
                    orari1=sorted(orari, key=lambda x: x.ora)
                    for i in orari1:
                        if user.friendship==True:
                            riga=FriendModel.find_by_orario_id(user.friend_id, i.id)
                            if riga:
                                if riga.data==data or riga.data==data1:
                                    mate=True
                                else:
                                    mate=False
                            else:
                                mate=False
                        else:
                            mate=None



                        riga=FriendModel.find_by_orario_id(user.id, i.id)
                        if riga:
                            if riga.data==data or riga.data==data1:
                                you=True
                            else:
                                you=False
                        else:
                            you=False
                        if i.materia_id:
                            materia=(SubjectModel.find_by_id(i.materia_id)).materia
                        else:
                            materia=None

                        final.append({"subject":materia,
                                    "you":you,
                                    "mate":mate})
                    return {"slenco":final}
                return []
            return {"message":"you are not in a class"}, 403
        return "user does not exist", 402
