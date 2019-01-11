from flask_restful import Resource, request
from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id, find_by_admin

class MakeAdmin (Resource):
    def post (self):
        data = request.get_json()
        mail=data[0]
        friendusername=data[1]
        user=UserModel.find_by_mail(mail)
        if user:
            classe=find_by_id(user.classe_id)
            if classe:
                if (classe.admin_id == str(user.id)):
                        friend=find_friend_by_username(user.classe_id, friendusername)
                        if friend:
                            classe.admin_id=friend.id
                            classe.save_to_db()
                            return "changed admin"
                        return "mate does not exist"
                return "user is not admin"
            return "user is not in a class"
        return "user does not exist"
