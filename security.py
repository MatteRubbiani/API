from models.users import UserModel


def authenticate(username, password):
    user = UserModel.find_by_mail(username)
    if user and user.password==password and user.confirmed==True:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
