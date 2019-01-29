from db import db

class UserModel(db.Model):
    __tablename__="utenti"

    id = db.Column(db.Integer, primary_key=True)
    mail=db.Column(db.String(80))
    username=db.Column(db.String(80))
    password=db.Column(db.String(140))
    friend_id=db.Column(db.Integer)
    classe_id=db.Column(db.Integer)
    creation_date=db.Column(db.String(30))
    friendship=db.Column(db.Boolean)
    admin=db.Column(db.Boolean)
    confirmed=db.Column(db.Boolean)


    def __init__(self, id, mail, username, password, classe_id, friend_id, creation_date, friendship, admin, confirmed):
        self.id=id
        self.mail=mail
        self.username=username
        self.password=password
        self.classe_id=classe_id
        self.friend_id=friend_id
        self.creation_date=creation_date
        self.friendship=friendship
        self.admin=admin
        self.confirmed=confirmed


    @classmethod
    def find_by_id(cls, id):
        return UserModel.query.filter_by(id=id).first()

    @classmethod
    def find_by_mail(cls, mail):
        return UserModel.query.filter_by(mail=mail).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"id":self.id, "mail":self.mail, "username":self.username, "password":self.password, "class":self.classe_id, "friend":self.friend_id}




def add_to_class (mail, classe_id):
    user=UserModel.query.filter_by(mail=mail).first()
    user.classe_id=classe_id
    user.save_to_db()

def class_users (classe_id):
    users= UserModel.query.filter_by(classe_id=classe_id)
    list=[]
    if users:
        for i in  users:
            list.append(i.username)
        return list

def class_mates (classe_id):
    users= UserModel.query.filter_by(classe_id=classe_id)
    list=[]
    if users:
        for i in  users:
            list.append(i.id)
        return list
    return None



def find_friend_by_username(classe_id, friendname):
    return UserModel.query.filter_by(classe_id=classe_id, username=friendname).first()
