from src.database.db import connection
from src.models.Estudiante import Estudiante

def postObtenerDatosEstudiante(id_usu):
  try:
    conn = connection()
    estudiantes = []
    inst =  '''
                SELECT USU.*, EST.*
                  FROM Usuario USU, Estudiante EST
                  WHERE USU.id_usu = EST.id_usu
                    AND USU.id_usu = %(id_usu)s;
            '''
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_usu': id_usu})
      for row in cursor.fetchall():
        estudiante = Estudiante(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
        estudiante.id_usu = row[0]
        estudiantes.append(estudiante.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    return estudiantes
  except Exception as e:
    print("(SISTEMA)   Error: "+e)
    return ''