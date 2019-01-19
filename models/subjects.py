from db import db


class SubjectModel(db.Model):
    __tablename__="materie"

    id = db.Column(db.Integer, primary_key=True)
    classe_id=db.Column(db.Integer)
    materia=db.Column(db.String(30))





    def __init__(self, id, classe_id, materia):
        self.id=id
        self.classe_id=classe_id
        self.materia=materia


    @classmethod
    def find_by_id(cls, id):
        return SubjectModel.query.filter_by(id=id).first()



    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

def delete_subjects_by_class_id(classe_id):
    materie=SubjectModel.query.filter_by(classe_id=classe_id)
    for i in materie:
        i.delete_from_db()


def find_by_classe_id(classe_id):
    materie=SubjectModel.query.filter_by(classe_id=classe_id)
    materielist=[]
    for i in materie:
        materielist.append(i.materia)
    return materielist


def find_subject_id (classe_id, materia):
    materie=SubjectModel.query.filter_by(classe_id=classe_id, materia=materia).first()
    return materie
