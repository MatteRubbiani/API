from flask_restful import Resource, request
from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id
from flask_jwt_extended import jwt_required, get_jwt_identity


class MakeAdmin (Resource):

    @jwt_required
    def post (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        friendusername=request.args.get('friend') 
        if user:
            if user.classe_id:
                if user.admin==True:
                    friend=find_friend_by_username(user.classe_id, friendusername)
                    if friend:
                        friend.admin=True
                        friend.save_to_db()
                        return {"message":"user made admin"}, 200
                    return "mate does not exist", 409
                return "user is not admin", 405
            return "user is not in a class", 403
        return "user does not exist", 402
