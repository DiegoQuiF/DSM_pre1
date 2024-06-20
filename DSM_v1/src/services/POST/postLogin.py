from src.database.db import connection
from src.models.Estudiante import Estudiante
from src.models.Especialista import Especialista

def postLogin(correo, contra):
  try:
    conn = connection()
    
    id_usuario = ''
    tipo_usuario = ''
    inst =  '''
            select usu.id_usu as id_usuario, usu.tipo_usu as tipo_usuario
              from usuario usu
              where usu.email_usu = %(email)s
                and usu.contra_usu = %(contra)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'email': correo, 'contra':contra})
      for row in cursor.fetchall():
        id_usuario = row[0]
        tipo_usuario = row[1]
      conn.commit()
      cursor.close()
    
    if tipo_usuario == 'estudiante':
      estudiante = ''
      inst =  '''
              select usu.id_usu as id_usuario, usu.tipo_usu as tipo_usuario, est.id_est as id_estudiante,
                concat(usu.nom_usu, ' ', usu.pat_usu, ' ', usu.mat_usu) as nombre_completo, usu.nacion_usu as pais,
                est.departamento_est as departamento, est.distrito_est as distrito, est.nom_univ_est as universidad,
                usu.tipo_doc_usu as tipo_documento, usu.num_doc_usu as numero_documento, usu.sexo_usu as sexo,
                usu.edad_usu as edad, usu.cel_usu as numero_celular, usu.email_usu as correo, usu.contra_usu as contrasenia
              from usuario usu, estudiante est
              where usu.id_usu = est.id_usu
                and usu.id_usu = %(id_usu)s;
              '''
      
      with conn.cursor() as cursor:
        cursor.execute(inst, {'id_usu': id_usuario})
        
        for row in cursor.fetchall():
          estudiante = Estudiante(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
          estudiante.id_usuario = row[0]
        conn.commit()
        cursor.close()
      conn.close()
      
      return estudiante.to_json()
    
    
    elif tipo_usuario == 'especialista':
      especialista = ''
      inst =  '''
              select usu.id_usu as id_usuario, usu.tipo_usu as tipo_usuario, esp.id_esp as id_especialista,
                concat(usu.nom_usu, ' ', usu.pat_usu, ' ', usu.mat_usu) as nombre_completo, usu.nacion_usu as pais,
                usu.tipo_doc_usu as tipo_documento, usu.num_doc_usu as numero_documento, usu.sexo_usu as sexo,
                usu.edad_usu as edad, usu.cel_usu as numero_celular, usu.email_usu as correo, usu.contra_usu as contrasenia
              from usuario usu, especialista esp
              where usu.id_usu = esp.id_usu
                and usu.id_usu = %(id_usu)s;
              '''
      
      with conn.cursor() as cursor:
        cursor.execute(inst, {'id_usu': id_usuario})
        
        for row in cursor.fetchall():
          especialista = Especialista(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
          especialista.id_usuario = row[0]
        conn.commit()
        cursor.close()
      conn.close()
      
      return especialista.to_json()
      
    else:
      conn.close()
      return ''
  
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''