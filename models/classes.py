from db import db


def find_by_admin(ciao):
    return ClassModel.query.filter_by(admin_id=ciao).first()

def find_by_tag(tag):
    return ClassModel.query.filter_by(tag=tag).first()


def find_by_id(id):
    return ClassModel.query.filter_by(id=id).first()




class ClassModel(db.Model):
    __tablename__="classi"

    id = db.Column(db.Integer, primary_key=True)
    tag=db.Column(db.String(10))
    admin_id=db.Column(db.String(30))
    orario_id=db.Column(db.String(30))
    nome=db.Column(db.String(30))



    def __init__(self, id, tag, admin_id, orario_id, nome):
        self.id=id
        self.tag=tag
        self.admin_id=admin_id
        self.orario_id=orario_id
        self.nome=nome








    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    def json(self):
        return {"id":self.id, "mail":self.mail, "username":self.username, "password":self.password, "class":self.classe, "friend":self.friendid}
