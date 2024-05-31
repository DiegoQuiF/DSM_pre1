from src.database.db import connection

def postRegistrarEstudiante(nom_usu, pat_usu, mat_usu, email_usu, contra_usu):
  try:
    conn = connection()
    id_usu = ''
    inst =  '''
                DO $$
                DECLARE
                    nuevo_id_usu INT;
                BEGIN
                    -- Insertar un nuevo usuario y capturar el id generado
                    INSERT INTO Usuario(nom_usu, pat_usu, mat_usu, email_usu, contra_usu)
                      VALUES (%(nombre)s, %(paterno)s, %(materno)s, %(correo)s, %(contra)s)
                      RETURNING id_usu INTO nuevo_id_usu;
                    
                    -- Insertar en la tabla Estudiante utilizando el id capturado
                    INSERT INTO Estudiante(id_usu)
                      VALUES (nuevo_id_usu);
                END $$;
                SELECT id_usu FROM Usuario WHERE email_usu = %(correo)s AND contra_usu = %(contra)s;
            '''
    with conn.cursor() as cursor:
      cursor.execute(inst, {'nombre': nom_usu, 'paterno':pat_usu, 'materno':mat_usu, 'correo':email_usu, 'contra':contra_usu})
      for row in cursor.fetchall():
        id_usu = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    return id_usu
  except Exception as e:
    print("(SISTEMA)   Error: "+e)
    return ''