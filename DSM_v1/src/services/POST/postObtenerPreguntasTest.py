from src.database.db import connection
from src.models.Pregunta import Pregunta

def postObtenerPreguntasTest(id_test):
  try:
    conn = connection()
    preguntas = []
    inst =  '''
                SELECT TPREG.id_test_preg, TPREG.id_test, TE.desc_test, PREG.id_preg, PREG.desc_preg, PREG.min_valor, PREG.max_valor as max_valor
                  FROM Pregunta PREG, TestPregunta TPREG, Test TE
                  WHERE PREG.id_preg = TPREG.id_preg AND TE.id_test = TPREG.id_test
                    AND TPREG.id_test = %(id_test)s
                  ORDER BY PREG.id_preg;
            '''
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test': id_test})
      for row in cursor.fetchall():
        pregunta = Pregunta(row[1], row[2], row[3], row[4], row[5], row[6])
        pregunta.id_test_preg = row[0]
        preguntas.append(pregunta.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    return preguntas
  except Exception as e:
    print("(SISTEMA)   Error: "+e)
    return ''