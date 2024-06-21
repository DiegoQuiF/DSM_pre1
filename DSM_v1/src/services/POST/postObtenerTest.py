from src.database.db import connection
from src.models.Test import Test
from src.models.Pregunta import Pregunta

def postObtenerTest(id_test):
  try:
    conn = connection()
    
    test = ''
    preguntas = []
    inst =  '''
            select preg.id_preg, preg.desc_preg as descripcion, preg.min_preg as puntaje_minimo, preg.max_preg as puntaje_maximo
              from pregunta preg, test_pregunta tpreg
              where preg.id_preg = tpreg.id_preg and tpreg.id_test = %(id_test)s
              order by preg.id_preg;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test': id_test})
      for row in cursor.fetchall():
        pregunta = Pregunta(row[1], row[2], row[3])
        pregunta.id_preg = row[0]
        preguntas.append(pregunta.to_json())
      conn.commit()
      cursor.close()
    
    inst =  '''
            select tes.id_test, tes.tipo_test as tipo, tes.desc_test as descripcion, tes.recom_test as recomendacion
              from test tes
              where tes.id_test = %(id_test)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test': id_test})
      for row in cursor.fetchall():
        test = Test(row[1], row[2], row[3])
        test.id_test = row[0]
      conn.commit()
      cursor.close()
    conn.close()
    
    result = {'test':test.to_json(), 'preguntas':preguntas}
    
    return result
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''