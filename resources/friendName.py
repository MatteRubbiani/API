from models.users import UserModel
from flask_restful import Resource, request

class FriendName(Resource):
    def get (self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            friend=UserModel.find_by_id(user.friend_id)
            return {"username":friend.username}, 200

        return {"meassege":"user does not exist"}, 500
