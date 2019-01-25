from models.users import UserModel, class_users, find_friend_by_username
from flask_restful import Resource, request
from flask_jwt import jwt_required



class Friend (Resource):

    @jwt_required
    def post (self):
        data=request.get_json()
        mail=data[0]
        amico=data[1]
        user=UserModel.find_by_mail(mail)
        if user:
            mate= find_friend_by_username(user.classe_id, amico)
            if mate:
                user.friend_id=mate.id
                user.save_to_db()
                if mate.friend_id==user.id:
                    user.friendship=True
                    mate.friendship=True
                    mate.save_to_db()
                    user.save_to_db()
                    return "friendship confirmed"
                user.friendship=False
                user.save_to_db
                return "friendship requested"
            return "mate does not exist"
        return "user does not exist"


    @jwt_required
    def delete(self):
        data=request.get_json()
        mail=data[0]
        user=UserModel.find_by_mail(mail)
        if user:
            mate= UserModel.find_by_id(user.friend_id)
            if mate:
                if mate.friend_id==user.id:
                    user.friend_id=None
                    user.friendship=False
                    mate.friendship=False
                    mate.save_to_db()
                    user.save_to_db()
                    return "friendship removed"
                user.friend_id=None
                user.friendship=False
                user.save_to_db()
                return "friend was removed but there was no friendship"
            return "you don't have any friends"
        return "user does not exist"
