from db import db

def add_to_class (mail, classe):
    user=UserModel.query.filter_by(mail=mail).first()
    user.classe_id=classe
    UserModel.save_to_db(user)


class MaterieModel(db.Model):
    __tablename__="materie"

    id = db.Column(db.Integer, primary_key=True)
    orario_id=db.Column(db.Integer)
    classe_id=db.Column(db.Integer)
    materia=db.Column(db.String(30))





    def __init__(self, id, orario_id, classe_id, materia):
        self.id=id
        self.orario_id=orario_id
        self.classe_id=classe_id
        self.materia=materia



    @classmethod
    def find_by_id(cls, id):
        return MaterieModel.query.filter_by(id=id).first()


    @classmethod
    def find_by_mail(cls, mail):
        return UserModel.query.filter_by(mail=mail).first()








    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
