from src.database.db import connection

def postLogin(correo, contra):
  try:
    conn = connection()
    id_usu = ''
    inst =  '''
                SELECT id_usu
                  FROM Usuario
                  WHERE email_usu = %(email)s
                    AND contra_usu = %(contra)s;
            '''
    with conn.cursor() as cursor:
      cursor.execute(inst, {'email': correo, 'contra':contra})
      for row in cursor.fetchall():
        id_usu = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    return id_usu
  except Exception as e:
    print("(SISTEMA)   Error: "+e)
    return ''