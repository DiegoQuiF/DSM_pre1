from flask import Blueprint, jsonify, request
from src.services.POST.postRegister import postRegister
from src.services.POST.postLogin import postLogin
from src.services.POST.postObtenerTest import postObtenerTest
from src.services.POST.postRegTest import postRegTest
from src.services.POST.postCompletarRegister import postCompletarRegister
from src.services.POST.postObtenerPersona import postObtenerPersona
from src.services.POST.postObtenerProvincias import postObtenerProvincias
from src.services.POST.postObtenerUbigeos import postObtenerUbigeos
from src.services.POST.postRegisterDiagEsp import postRegisterDiagEsp
from src.services.GET.getObtenerDepartamentos import getObtenerDepartamentos
from src.services.GET.getTest import getTests
from src.services.GET.getObtenerTestsEvaluables import getObtenerTestsEvaluables

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

@main.route("/obtenerPersona", methods = ['POST'])
def obtenerPersona():
  try:
    data = request.get_json()
    id_pers = data['id_pers']
    
    result = postObtenerPersona(id_pers)
    if(result!=''):
      data = {'persona': result.to_json()}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':data})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False, 'error': str(e)})

@main.route("/obtenerDepartamentos")
def obtenerDepartamento():
  try:
    result = getObtenerDepartamentos()
    if(result!=''):
      data = {'departamentos': result}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':data})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False, 'error': str(e)})

@main.route("/obtenerProvincias", methods = ['POST'])
def obtenerProvincia():
  try:
    data = request.get_json()
    id_dep = data['id_dep']
    
    result = postObtenerProvincias(id_dep)
    if(result!=''):
      data = {'provincias': result}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':data})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False, 'error': str(e)})

@main.route("/obtenerUbigeos", methods = ['POST'])
def obtenerUbigeos():
  try:
    data = request.get_json()
    id_prov = data['id_prov']
    
    result = postObtenerUbigeos(id_prov)
    if(result!=''):
      data = {'ubigeos': result}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':data})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False, 'error': str(e)})

@main.route("/obtenerTestsEvaluables")
def obtenerTestsEvaluables():
  try:
    result = getObtenerTestsEvaluables()
    if(result!=''):
      data = {'tests': result}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':data})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False, 'error': str(e)})

@main.route("/registerDiagEsp", methods = ['POST'])
def registerDiagEsp():
  try:
    data = request.get_json()
    id_esp = data['id_usu']
    id_test_res = data['id_test_res']
    descripcion = data['descripcion']
    resultado = data['resultado']
    recomendacion = data['recomendacion']
    tratamiento = data['tratamiento']
    notas = data['notas']
    
    result = postRegisterDiagEsp(id_esp, id_test_res, descripcion, resultado, recomendacion, tratamiento, notas)
    if(result):
      return jsonify({'message':'COMPLETE', 'success':True})
    else:
      return jsonify({'message':'ERROR', 'success':False})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False, 'error': str(e)})