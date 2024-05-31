from src.database.db import connection

def postCompletarRegistroEstudiante(id_usu, nacionalidad, tipo_doc, num_doc, sexo, edad, celular, estado_civil, nom_univ):
  try:
    conn = connection()
    inst =  '''
                UPDATE Usuario
                  SET	nacion_usu=%(nacion_usu)s, tipo_doc_usu=%(tipo_doc_usu)s, num_doc_usu=%(num_doc_usu)s, sexo_usu=%(sexo_usu)s, edad_usu=%(edad_usu)s, cel_usu=%(cel_usu)s
                  WHERE id_usu=%(id_usuario)s;

                UPDATE Estudiante
                  SET	est_civ_est=%(est_civ_est)s, nom_univ_est=%(nom_univ_est)s
                  WHERE id_usu=%(id_usuario)s;
            '''
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_usuario': id_usu, 'nacion_usu': nacionalidad, 'tipo_doc_usu': tipo_doc,
                            'num_doc_usu': num_doc, 'sexo_usu': sexo, 'edad_usu': edad,
                            'cel_usu': celular, 'est_civ_est': estado_civil, 'nom_univ_est': nom_univ})
      conn.commit()
    cursor.close()
    conn.close()
    return True
  except Exception as e:
    print("(SISTEMA)   Error: "+e)
    return False