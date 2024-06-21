from flask import Blueprint, jsonify, request
from src.services.POST.postRegister import postRegister
from src.services.POST.postLogin import postLogin
from src.services.POST.postObtenerTest import postObtenerTest
from src.services.POST.postRegTest import postRegTest
from src.services.GET.getTest import getTests

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
    result = postRegister(data)
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
    id_est = data['id_est']    
    matrizPreg = data['preguntas']
    
    matriz = []
    for item in matrizPreg:
      fila = [item["id_preg"], item["puntaje"]]
      matriz.append(fila)
    
    result = postRegTest(id_est, matriz)
    if(result):
      return jsonify({'message':'COMPLETE', 'success':True})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False, 'error': str(e)})
