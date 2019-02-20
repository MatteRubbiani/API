from db import db
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.classes import ClassModel, find_by_tag, find_by_id
from models.users import UserModel, add_to_class, find_friend_by_username, class_mates, find_mates_id
from models.timetable import delete_timetable_by_classe_id, find_id_by_giorno_id
from models.subjects import delete_subjects_by_class_id
from models.friends import delete_slots_by_user_id



class JoinClass(Resource):

    @jwt_required
    def post(self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        tag=request.args.get('tag')
        if user:
            classe=find_by_tag(tag)
            if classe:
                mate= find_friend_by_username(classe.id, user.username)
                if mate:
                    return {"message":"change name"}, 410

                user.classe_id=classe.id
                user.save_to_db()
                return {"message":"user added to class succesfully"}, 200

            return {"message":"class does not exist"}, 411
        return {"message":"user does not exist"}, 402

    @jwt_required
    def delete (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            if user.classe_id:
                delete_slots_by_user_id(user.id)
                mate=UserModel.find_by_id(user.friend_id)
                user.friend_id=None
                user.friendship=False
                user.save_to_db()
                if mate:
                    if mate.friend_id==user.id:
                        mate.friend_id=None
                        mate.friendship=False
                        mate.save_to_db()
                if user.admin==True:
                    amici=class_mates_id(user.classe_id)
                    if len(amici)>1:
                        for i in amici:
                            friend=UserModel.find_by_id(i)
                            if i !=user.id:
                                if friend.admin==True:
                                    user.classe_id=None
                                    user.admin=False
                                    user.save_to_db()
                                    return "user was removed, was admin, there were other admins", 200
                        for i in  amici:
                            friend=UserModel.find_by_id(i)
                            if friend.id!=user.id:
                                friend.admin=True
                                friend.save_to_db()
                                user.classe_id=None
                                user.admin=False
                                user.save_to_db()
                                return "user was admin, there were no other admin, one was created, user correctly removed from class ", 200
                    classe=find_by_id(user.classe_id)
                    delete_subjects_by_class_id(user.classe_id)
                    delete_timetable_by_classe_id(user.classe_id)
                    classe.delete_from_db()
                    user.classe_id=None
                    user.admin=False
                    user.save_to_db()
                    return "user had no classmates, class was deleted", 200
                user.classe_id=None
                user.save_to_db()
                return "user was not admin, user removed correctly", 200
            return {"message":"user not in a class"}, 403
        return {"message":"user does not exist"}, 402
