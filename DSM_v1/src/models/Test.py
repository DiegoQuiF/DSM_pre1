from src.database.db import db

class Test(db.Model):
  id_test = db.Column(db.Integer, primary_key=True)
  tipo_test = db.Column(db.String(50))
  desc_test = db.Column(db.Text)

  def __init__(self, tipo, descripcion) -> None:
    self.tipo_test = tipo
    self.desc_test = descripcion
  
  def to_json(self):
    return {
      'id_test': self.id_test,
      'tipo_test' : self.tipo_test,
      'desc_test' : self.desc_test
    }