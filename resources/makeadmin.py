from flask_restful import Resource, request
from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id
from flask_jwt import jwt_required


class MakeAdmin (Resource):

    @jwt_required()
    def post (self):
        mail=request.args.get('mail')
        friendusername=request.args.get('friendusername')
        user=UserModel.find_by_mail(mail)
        if user:
            if user.classe_id:
                if user.admin==True:
                    friend=find_friend_by_username(user.classe_id, friendusername)
                    if friend:
                        friend.admin=True
                        friend.save_to_db()
                        return {"message":"user made admin"}, 200
                    return "mate does not exist", 500
                return "user is not admin", 500
            return "user is not in a class", 500
        return "user does not exist", 500
