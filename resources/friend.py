from models.users import UserModel, class_users, find_friend_by_username
from flask_restful import Resource, request
from flask_jwt import jwt_required



class Friend(Resource):

    @jwt_required()
    def post (self):
        mail=request.args.get('mail')
        amico=request.args.get('friend')
        user=UserModel.find_by_mail(mail)
        if user:
            mate= find_friend_by_username(user.classe_id, amico)
            if mate:
                if mate.id==user.id:
                    return "sei un poveraccio"
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
            return {"message":"mate does not exist"}, 500
        return {"message":"user does not exist"}, 500


    @jwt_required()
    def delete(self):
        mail=request.args.get('mail')
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
                    return {"message":"friendship removed"},200
                user.friend_id=None
                user.friendship=False
                user.save_to_db()
                return {"message":"friend was removed but there was no friendship"}, 200
            return {"message":"you don't have any friends"}, 500
        return {"message":"user does not exist"}, 500
