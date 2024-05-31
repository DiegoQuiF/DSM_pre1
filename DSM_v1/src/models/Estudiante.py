from src.database.db import db

class Estudiante(db.Model):
  id_usu = db.Column(db.Integer, primary_key=True)
  nom_usu = db.Column(db.String(50))
  pat_usu = db.Column(db.String(50))
  mat_usu = db.Column(db.String(50))
  nacion_usu = db.Column(db.String(50))
  tipo_doc_usu = db.Column(db.String(50))
  num_doc_us = db.Column(db.Integer)
  sexo_usu = db.Column(db.String(50))
  edad_usu = db.Column(db.Integer)
  cel_us = db.Column(db.Integer)
  email_us = db.Column(db.String(120))
  contra_usu = db.Column(db.Text)
  id_est = db.Column(db.Integer)
  est_civ_es = db.Column(db.String(50))
  nom_univ_est = db.Column(db.String(120))

  def __init__(self, nombre, paterno, materno, nacionalidad, tipo_doc,
                num_doc, sexo, edad, celular, email, contra, id_estudiante,
                est_civil, nom_universidad) -> None:
    self.nom_usu = nombre
    self.pat_usu = paterno
    self.mat_usu = materno
    self.nacion_usu = nacionalidad
    self.tipo_doc_usu = tipo_doc
    self.num_doc_us = num_doc
    self.sexo_usu = sexo
    self.edad_usu = edad
    self.cel_us = celular
    self.email_us = email
    self.contra_usu = contra
    self.id_est = id_estudiante
    self.est_civ_es = est_civil
    self.nom_univ_est = nom_universidad
  
  def to_json(self):
    return {
      'id_usu': self.id_usu,
      'nom_usu' : self.nom_usu,
      'pat_usu' : self.pat_usu,
      'mat_usu' : self.mat_usu,
      'nacion_usu' : self.nacion_usu,
      'tipo_doc_usu' : self.tipo_doc_usu,
      'num_doc_us' : self.num_doc_us,
      'sexo_usu' : self.sexo_usu,
      'edad_usu' : self.edad_usu,
      'cel_us' : self.cel_us,
      'email_us' : self.email_us,
      'contra_usu' : self.contra_usu,
      'id_est' : self.id_est,
      'est_civ_es' : self.est_civ_es,
      'nom_univ_est' : self.nom_univ_est
    }