from models.users import UserModel
import hashlib, uuid


def authenticate(username, password):
    user = UserModel.find_by_mail(username)
    if user and user.password==hashlib.sha512(password).hexdigest() :#and user.confirmed==True:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
