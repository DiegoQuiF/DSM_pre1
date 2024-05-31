from flask import Blueprint, jsonify, request
from src.services.POST.postLogin import postLogin
from src.services.POST.postObtenerDatosEstudiante import postObtenerDatosEstudiante
from src.services.POST.postRegistrarEstudiante import postRegistrarEstudiante
from src.services.POST.postCompletarRegistroEstudiante import postCompletarRegistroEstudiante
from src.services.POST.postObtenerPreguntasTest import postObtenerPreguntasTest
from src.services.GET.getTest import getTests

main = Blueprint('index_blueprint', __name__)

@main.route("/login", methods = ['POST'])
def login():
  try:
    data = request.get_json()
    email = data['email_usu']
    contra = data['contra_usu']
    id_usu = postLogin(email, contra)
    if(id_usu!=""):
      datos = {'id_usu':id_usu,}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/estudiante", methods = ['POST'])
def obtenerDatosEstudiante():
  try:
    data = request.get_json()
    id_usu = data['id_usu']
    user = postObtenerDatosEstudiante(id_usu)
    if(len(user)>0):
      datos = user[0]
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/regEstudiante", methods = ['POST'])
def registrarEstudiante():
  try:
    data = request.get_json()
    nom = data['nom_usu']
    pat = data['pat_usu']
    mat = data['mat_usu']
    email = data['email_usu']
    contra = data['contra_usu']
    id_usu = postRegistrarEstudiante(nom, pat, mat, email, contra)
    if(id_usu!=""):
      datos = {'id_usu':id_usu,}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/actEstudiante", methods = ['POST'])
def completarRegistroEstudiante():
  try:
    data = request.get_json()
    id_usu = data['id_usu']
    nacionalidad = data['nacion_usu']
    tipo_doc = data['tipo_doc_usu']
    num_doc = data['num_doc_usu']
    sexo = data['sexo_usu']
    edad = data['edad_usu']
    celular = data['cel_usu']
    estado_civil = data['est_civ_est']
    nom_univ = data['nom_univ_est']
    result = postCompletarRegistroEstudiante(id_usu, nacionalidad, tipo_doc, num_doc, sexo, edad, celular, estado_civil, nom_univ)
    if(result):
      datos = {'id_usu':id_usu,}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/tests", methods = ['GET'])
def obtenerTests():
  try:
    tests = getTests()
    if(len(tests)>0):
      datos = tests
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/testCompleto", methods = ['POST'])
def obtenerPreguntasTest():
  try:
    data = request.get_json()
    id_test = data['id_test']
    preguntas = postObtenerPreguntasTest(id_test)
    if(len(preguntas)>0):
      datos = preguntas
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})