from src.database.db import db

class Pregunta(db.Model):
  id_test_preg = db.Column(db.Integer, primary_key=True)
  id_test = db.Column(db.Integer)
  desc_test = db.Column(db.Text)
  id_preg = db.Column(db.Integer)
  desc_preg = db.Column(db.Text)
  min_valor = db.Column(db.Integer)
  max_valor = db.Column(db.Integer)

  def __init__(self, id_test, desc_test, id_preg, desc_preg, min_valor, max_valor) -> None:
    self.id_test = id_test
    self.desc_test = desc_test
    self.id_preg = id_preg
    self.desc_preg = desc_preg
    self.min_valor = min_valor
    self.max_valor = max_valor
  
  def to_json(self):
    return {
      'id_test_preg': self.id_test_preg,
      'id_test': self.id_test,
      'desc_test': self.desc_test,
      'id_preg': self.id_preg,
      'desc_preg': self.desc_preg,
      'min_valor': self.min_valor,
      'max_valor': self.max_valor
    }