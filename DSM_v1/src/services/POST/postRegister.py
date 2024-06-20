from src.database.db import connection
from src.models.Estudiante import Estudiante
from src.models.Especialista import Especialista

def postRegister(data):
  try:
    conn = connection()
    
    tipo_usuario = data['tipo_usuario']
    nombre = data['nombre']
    aPaterno = data['aPaterno']
    aMaterno = data['aMaterno']
    correo = data['correo']
    contrasenia = data['contrasenia']
    inst = ''
    
    if tipo_usuario == 'estudiante' or tipo_usuario == 'especialista':
      
      if tipo_usuario == 'estudiante':
        
        inst =  '''
                do $$
                declare
                    nuevo_id_usu int;
                begin
                    insert into usuario(nom_usu, pat_usu, mat_usu, tipo_usu, email_usu, contra_usu)
                      values (%(nombre)s, %(aPaterno)s, %(aMaterno)s, %(tipo_usuario)s, %(correo)s, %(contrasenia)s)
                      returning id_usu into nuevo_id_usu;
                    
                    insert into estudiante(id_usu)
                      values(nuevo_id_usu);
                end $$;
              '''
      
      elif tipo_usuario == 'especialista':
        
        inst =  '''
                do $$
                declare
                    nuevo_id_usu int;
                begin
                    insert into usuario(nom_usu, pat_usu, mat_usu, tipo_usu, email_usu, contra_usu)
                      values (%(nombre)s, %(aPaterno)s, %(aMaterno)s, %(tipo_usuario)s, %(correo)s, %(contrasenia)s)
                      returning id_usu into nuevo_id_usu;

                    insert into especialista(id_usu)
                      values(nuevo_id_usu);
                end $$;
              '''
      
      with conn.cursor() as cursor:
        cursor.execute(inst, {'nombre': nombre, 'aPaterno': aPaterno, 'aMaterno': aMaterno, 'tipo_usuario': tipo_usuario, 'correo': correo, 'contrasenia': contrasenia})
        conn.commit()
        cursor.close()
      conn.close()
      
      return True
      
    else:
      return False
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return False