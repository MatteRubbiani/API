from db import db


class TimetableModel(db.Model):
    __tablename__="orario"

    id = db.Column(db.Integer, primary_key=True)
    classe_id=db.Column(db.Integer)
    ora=db.Column(db.Integer)
    giorno_id=db.Column(db.Integer)
    materia_id=db.Column(db.integer)





    def __init__(self, id, classe_id, ora, giorno_id, materia_id):
        self.id=id
        self.classe_id=classe_id
        self.ora=ora
        self.giorno_id=giorno_id
        self.materia_id=materia_id


    @classmethod
    def find_by_giorno_id(cls, classe_id, giorno_id):
        materie=TimetableModel.query.filter_by(classe_id=classe_id, giorno_id=giorno_id)
        orario_del_giorno=[]
        for i in materie:
            orario_del_giorno.append(i.materia_id)
        return orario_del_giorno

    def find_by_ora(cls, classe_id, giorno_id, ora):
        materia=TimetableModel.query.filter_by(classe_id=classe_id, giorno_id=giorno_id, ora=ora).first()
        return materia

        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
