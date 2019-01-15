from db import db


class TimetableModel(db.Model):
    __tablename__="orario"

    id = db.Column(db.Integer, primary_key=True)
    classe_id=db.Column(db.Integer)
    ora=db.Column(db.Integer)
    giorno_id=db.Column(db.Integer)
    materia_id=db.Column(db.Integer)





    def __init__(self, id, classe_id, giorno_id,ora,  materia_id):
        self.id=id
        self.classe_id=classe_id
        self.giorno_id=giorno_id
        self.ora=ora
        self.materia_id=materia_id

    @classmethod
    def find_by_id (cls, id):
        a=TimetableModel.query.filter_by(id=id).first()
        return a






    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

def find_id_by_giorno_id(classe_id, giorno_id):
    materie=TimetableModel.query.filter_by(classe_id=classe_id, giorno_id=giorno_id)
    orario_del_giorno=[]
    for i in materie:
        orario_del_giorno.append(i.id)
    return orario_del_giorno


def find_by_giorno_id(classe_id, giorno_id):
    materie=TimetableModel.query.filter_by(classe_id=classe_id, giorno_id=giorno_id)
    orario_del_giorno=[]
    for i in materie:
        orario_del_giorno.append(i.materia_id)
    return orario_del_giorno

def find_by_ora(classe_id, giorno_id, ora):
    materia=TimetableModel.query.filter_by(classe_id=classe_id, giorno_id=giorno_id, ora=ora).first()
    return materia
