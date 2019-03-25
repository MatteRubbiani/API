from db import db
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import hashlib, uuid

from models.classes import ClassModel, find_by_tag
from models.users import UserModel
from models.timetable import TimetableModel, find_by_ora, find_by_giorno_id
from models.subjects import SubjectModel, find_subject_id

class ChangePassword(Resource):
    @jwt_required
    def post(self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        old=request.args.get('oldPassword')
        new=request.args.get('newPassword')
        if old==None:
            return "", 450
        if new==None:
            return "", 450
        epsw=old.encode('utf-8')
        newpsw=new.encode('utf-8')
        if user:
            if True:#user.password==hashlib.sha512(epsw).hexdigest():
                user.password=hashlib.sha512(newpsw).hexdigest()

                return {"message":"ok"}, 200
            return {"message":"wrong password"}, 414
        return {"nope"}, 413
