from models.users import UserModel, class_users, find_friend_by_username
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity



class Friend(Resource):

    @jwt_required
    def post (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        amico=request.args.get('friend')
        mate= find_friend_by_username(user.classe_id, amico)
        if user:
            if user.friend_id:
                return "hai gia' un amico", 407
            if mate:
                if mate.id==user.id:
                    return "sei un poveraccio", 413
                user.friend_id=mate.id
                user.save_to_db()
                if mate.friend_id==user.id:
                    user.friendship=True
                    mate.friendship=True
                    mate.save_to_db()
                    user.save_to_db()
                    return {"message":"friendship confirmed"},200
                user.friendship=False
                user.save_to_db
                return {"message":"friendship requested"},200
            return {"message":"mate does not exist"}, 409
        return {"message":"user does not exist"}, 402


    @jwt_required
    def delete(self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            mate= UserModel.find_by_id(user.friend_id)
            if mate:
                if mate.friend_id==user.id:
                    user.friend_id=None
                    user.friendship=False
                    mate.friendship=False
                    mate.save_to_db()
                    user.save_to_db()
                    return {"message":"friendship removed"},200
                user.friend_id=None
                user.friendship=False
                user.save_to_db()
                return {"message":"friend was removed but there was no friendship"}, 200
            return {"message":"you don't have a mate"}, 404
        return {"message":"user does not exist"}, 402
