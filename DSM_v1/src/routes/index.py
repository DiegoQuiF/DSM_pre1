from flask import Blueprint, jsonify, request
from src.services.POST.postRegister import postRegister
from src.services.POST.postLogin import postLogin
from src.services.POST.postObtenerTest import postObtenerTest
from src.services.POST.postRegTest import postRegTest
from src.services.POST.postObtenerHistorias import postObtenerHistorias
from src.services.POST.postObtenerTestHistoria import postObtenerTestHistoria
from src.services.POST.postCompletarRegister import postCompletarRegister
from src.services.GET.getTest import getTests
from src.services.GET.getTodosTest import getObtenerTodosTest

main = Blueprint('index_blueprint', __name__)

@main.route("/login", methods = ['POST'])
def login():
  try:
    data = request.get_json()
    email = data['email']
    contra = data['contra']
    usuario = postLogin(email, contra)
    if(usuario!=''):
      datos = {'usuario':usuario}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/register", methods = ['POST'])
def register():
  try:
    data = request.get_json()
    nombre = data['nombre']
    paterno = data['aPaterno']
    materno = data['aMaterno']
    correo = data['correo']
    contra = data['contrasenia']
    tipo = data['tipo_usuario']
    result = postRegister(nombre, paterno, materno, correo, contra, tipo)
    if(result):
      return jsonify({'message':'COMPLETE', 'success':True})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/completarRegister", methods = ['POST'])
def completar_register():
  try:
    data = request.get_json()
    
    id_pers = data['id_pers']
    nombre = data['nombre']
    paterno = data['aPaterno']
    materno = data['aMaterno']
    num_documento = data['num_documento']
    sexo = data['sexo']
    edad = data['edad']
    num_celular = data['num_celular']
    id_ubi = data['id_ubi']
    
    result = postCompletarRegister(id_pers, nombre, paterno, materno, num_documento, sexo, edad, num_celular, id_ubi)
    if(result):
      return jsonify({'message':'COMPLETE', 'success':True})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/tests", methods = ['GET'])
def tests():
  try:
    tests = getTests()
    if(len(tests)>0):
      datos = tests
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/obtenerTest", methods = ['POST'])
def obtenerTest():
  try:
    data = request.get_json()
    id_test = data['id_test']
    datos = postObtenerTest(id_test)
    if(datos):
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False, 'error': str(e)})

@main.route("/registerTest", methods = ['POST'])
def registerTest():
  try:
    data = request.get_json()
    id_est = data['id_usu']    
    matrizPreg = data['preguntas']
    
    matriz = []
    for item in matrizPreg:
      fila = [item["id_preg"], item["puntaje"]]
      matriz.append(fila)
    
    result = postRegTest(id_est, matriz)
    if(result!=''):
      data = {'diagnostico_automatico': result.to_json()}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':data})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False, 'error': str(e)})

