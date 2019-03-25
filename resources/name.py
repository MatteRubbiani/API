from models.users import UserModel
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity

class Name(Resource):
    @jwt_required
    def get (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        if user:
            if user.confirmed==True:
                return {"username":user.username}, 200
        return {"meassege":"user does not exist"}, 402

    @jwt_required
    def post (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        name=request.args.get('name')
        if user:
            if user.confirmed==True:
                user.username = name
                user.save_to_db()
                return {"username":user.username}, 200
        return {"meassege":"user does not exist"}, 402
