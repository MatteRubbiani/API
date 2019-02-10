from models.users import UserModel
from flask_restful import Resource, request

class Name(Resource):
    def get (self):
        mail=request.args.get('mail')
        user=UserModel.find_by_mail(mail)
        if user:
            return {"username":user.username}, 200

        return {"meassege":"user does not exist"}, 500
