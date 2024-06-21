from src.database.db import connection
from src.models.Historia import Historia

def postObtenerHistorias(id_est):
  try:
    conn = connection()
    
    historias = []
    inst =  '''
            select hi.id_hist, hi.estado_hist, to_char(hi.apertura_hist, 'DD-MM-YYYY') as apertura_hist,
                to_char(hi.alta_hist, 'DD-MM-YYYY') as alta_hist
              from historia hi, estudiante_historia eh
              where hi.id_hist = eh.id_hist and eh.id_est = %(id_est)s;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_est': id_est})
      for row in cursor.fetchall():
        historia = Historia(row[1], row[2], row[3])
        historia.id_hist = row[0]
        historias.append(historia.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    
    return historias
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return ''