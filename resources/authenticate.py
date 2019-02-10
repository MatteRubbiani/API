from flask_restful import Resource, request
from flask_jwt_extended import create_access_token, create_refresh_token
from models.users import UserModel
import hashlib, uuid
class UserLogin(Resource):
    def post(self):
        #mail=request.args.get('mail')
        #password=request.args.get('password')
        data=request.get_json()
        mail=data["mail"]
        password=data["password"]

        user=UserModel.find_by_mail(mail)
        epsw=password.encode('utf-8')
        if user: #and user.password==hashlib.sha512(epsw).hexdigest() and user.confirmed==True:
            access_token=create_access_token(identity=user.id, fresh=True)
            refresh_token=create_refresh_token(user.id)
            return {"access_token":access_token,
                "refresh_token":refresh_token
                }, 200
        return {"message":"invalid cresdentials"}, 401
