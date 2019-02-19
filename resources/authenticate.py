from flask_restful import Resource, request
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_refresh_token_required,
                                get_jwt_identity,
                                get_raw_jwt)
from models.users import UserModel
import hashlib, uuid
class UserLogin(Resource):
    def post(self):
        mail=request.args.get('mail')
        password=request.args.get('password')
        user=UserModel.find_by_mail(mail)
        epsw=password.encode('utf-8')
        if user: #and user.password==hashlib.sha512(epsw).hexdigest() and user.confirmed==True:
            access_token=create_access_token(identity=user.id, fresh=True)
            refresh_token=create_refresh_token(user.id)
            return {"access_token":access_token,
                "refresh_token":refresh_token
                }, 200
        return {"message":"invalid cresdentials"}, 401

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user=get_jwt_identity()
        #a=get_raw_jwt()
        #return a["iat"] questo E' PER PENDERE DATA DI CRAZIONE REFRESH TOKEN
        new_token=create_access_token(identity=current_user, fresh=False)
        return {"access_token":new_token}
