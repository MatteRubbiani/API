from models.users import UserModel
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity

class FriendName(Resource):
    @jwt_required
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            if user.friend_id:
                friend=UserModel.find_by_id(user.friend_id)
                return {"username":friend.username}, 200
            return {"message":"user has no mate"}, 404
        return {"meassege":"user does not exist"}, 402
