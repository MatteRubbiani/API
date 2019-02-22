from flask_restful import Resource, request
from models.users import UserModel, class_users, find_friend_by_username
from models.classes import find_by_id
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.classes import ClassModel, find_by_tag, find_by_id
from models.users import UserModel, add_to_class, find_friend_by_username, class_mates, find_mates_id
from models.timetable import delete_timetable_by_classe_id, find_id_by_giorno_id
from models.subjects import delete_subjects_by_class_id
from models.friends import delete_slots_by_user_id


class RemoveFromClass (Resource):

    @jwt_required
    def delete (self):
        current_user=get_jwt_identity()
        user=UserModel.find_by_id(current_user)
        friendusername=request.args.get('friend')
        if user:
            if user.classe_id:
                if user.admin==True:
                    mate=find_friend_by_username(user.classe_id, friendusername)
                    delete_slots_by_user_id(mate.id)
                    mateMate=UserModel.find_by_id(mate.friend_id)
                    if mateMate:
                        if mateMate.friend_id==mate.id:
                            mateMate.friend_id=None
                            mateMate.friendship=False
                            mateMate.save_to_db()
                    mate.friend_id=None
                    mate.friendship=False
                    mate.classe_id=None
                    mate.admin=False
                    mate.save_to_db()
                    return "user removed correctly", 200
                return "user is not admin", 405
            return "user is not in a class", 403
        return "user does not exist", 402
