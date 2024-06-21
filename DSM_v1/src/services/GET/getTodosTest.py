from src.database.db import connection
from src.models.TestEstudiante import TestEstudiante

def getObtenerTodosTest():
  try:
    conn = connection()
    
    tests = []
    inst =  '''
            select distinct (tr.*), t.tipo_test, t.desc_test
              from test_resuelto tr, historia_test_resuelto htr, test_resuelto_detalle trd , test_detalle td, test_pregunta tp, test t
              where tr.id_test_res = htr.id_test_res and htr.id_test_res = trd.id_test_res and td.id_test_det = trd.id_test_det
                and tp.id_test_preg = td.id_test_preg and t.id_test = tp.id_test;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        test = TestEstudiante(row[1], row[2], row[3])
        test.id_test_res = row[0]
        tests.append(test.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    
    return tests
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''