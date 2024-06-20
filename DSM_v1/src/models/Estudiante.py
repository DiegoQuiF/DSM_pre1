from src.database.db import db

class Estudiante(db.Model):
  id_usuario = db.Column(db.Integer, primary_key = True)
  tipo_usuario = db.Column(db.String(50))
  id_estudiante = db.Column(db.Integer)
  nombre_completo = db.Column(db.Text)
  pais = db.Column(db.String(50))
  departamento = db.Column(db.Text)
  distrito = db.Column(db.Text)
  universidad = db.Column(db.String(120))
  tipo_documento = db.Column(db.String(50))
  numero_documento = db.Column(db.Integer)
  sexo = db.Column(db.String(50))
  edad = db.Column(db.Integer)
  numero_celular = db.Column(db.Integer)
  correo = db.Column(db.String(120))
  contrasenia = db.Column(db.Text)

  def __init__(self, tipo_usuario, id_estudiante, nombre_completo, pais, departamento, distrito,
               universidad, tipo_documento, numero_documento, sexo, edad, numero_celular, correo, contrasenia) -> None:
    self.tipo_usuario = tipo_usuario
    self.id_estudiante = id_estudiante
    self.nombre_completo = nombre_completo
    self.pais = pais
    self.departamento = departamento
    self.distrito = distrito
    self.universidad = universidad
    self.tipo_documento = tipo_documento
    self.numero_documento = numero_documento
    self.sexo = sexo
    self.edad = edad
    self.numero_celular = numero_celular
    self.correo = correo
    self.contrasenia = contrasenia
    
  def to_json(self):
    return {
      'id_usuario': self.id_usuario,
      'tipo_usuario' : self.tipo_usuario,
      'id_estudiante' : self.id_estudiante,
      'nombre_completo' : self.nombre_completo,
      'pais' : self.pais,
      'departamento' : self.departamento,
      'distrito' : self.distrito,
      'universidad' : self.universidad,
      'tipo_documento' : self.tipo_documento,
      'numero_documento' : self.numero_documento,
      'sexo' : self.sexo,
      'edad' : self.edad,
      'numero_celular' : self.numero_celular,
      'correo' : self.correo,
      'contrasenia' : self.contrasenia
    }