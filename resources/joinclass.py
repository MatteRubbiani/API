from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_tag, find_by_id
from models.users import UserModel, add_to_class, find_friend_by_username, class_mates

class JoinClass(Resource):

    #@jwt_required()
    def post(self):
        data=request.get_json()
        mail=data[0]
        tag=data[1]
        user=UserModel.find_by_mail(mail)
        if user:
            classe=find_by_tag(tag)
            if classe:
                mate= find_friend_by_username(classe.id, user.username)
                if mate:
                    return "change name"

                user.classe_id=classe.id
                user.save_to_db()
                return "user added to class succesfully", 200

            return "class does not exist" , 400
        return "user does not exist", 400

    def delete (self):
        data=request.get_json()
        mail=data[0]
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                mate=UserModel.find_by_id(user.friend_id)
                user.friend_id=None
                user.friendship=True
                user.save_to_db
                if mate:
                    if mate.friend_id==user.id:
                        mate.friend_id=None
                        mate.friendship=False
                        mate.save_to_db()
                if user.admin==True:
                    amici=class_mates(user.classe_id)
                    if len(amici)>1:
                        for i in amici:
                            friend=UserModel.find_by_id(i)
                            if i !=user.id:
                                if friend.admin==True:
                                    user.classe_id=None
                                    user.admin=False
                                    user.save_to_db()
                                    return "user was removed, was admin, there were other admins"
                        for i in  amici:
                            friend=UserModel.find_by_id(i)
                            if friend.id!=user.id:
                                friend.admin=True
                                friend.save_to_db()
                                user.classe_id=None
                                user.admin=False
                                user.save_to_db()
                                return "user was admin, there were no other admin, one was created, user correctly removed from class "
                    classe=find_by_id(user.classe_id)
                    classe.delete_from_db()
                    user.classe_id=None
                    user.admin=False
                    user.save_to_db()
                    return "user had no classmates, was admin, class was deleted"
                user.classe_id=None
                user.save_to_db()
                return "user was not admin, user removed correctly"
            return "user not in a class"
        return "user does not exist"
