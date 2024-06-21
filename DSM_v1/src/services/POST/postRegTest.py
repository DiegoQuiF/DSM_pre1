from src.database.db import connection

def postRegTest(id_est, matrizPreg):
  try:
    conn = connection()
    
    id_hist = 0
    id_test_res = 0
    id_test_det_array = []
    
    inst =  '''
            select h.id_hist
              from historia h, estudiante_historia eh
              where h.id_hist = eh.id_hist and eh.id_est = %(id_est)s
                and h.apertura_hist = (select max(apertura_hist) from historia)
                and h.id_hist = (select max(id_hist) from historia)
                and h.estado_hist = 'proceso';
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_est': id_est})
      for row in cursor.fetchall():
        id_hist = row[0]
      cursor.close()
    
    print(id_hist)
    
    if (id_hist == 0):
      inst =  '''
              do $$
              declare
                nuevo_id_hist int;
              begin
                -- Generar nueva historia
                insert into historia(estado_hist, apertura_hist)
                  values ('proceso', to_date(current_date::text, 'YYYY-MM-DD'))
                  returning id_hist into nuevo_id_hist;
                -- Asociar historia al estudiante
                insert into estudiante_historia(id_est, id_hist)
                  values (%(id_est)s, nuevo_id_hist);
              end $$;
              '''
      with conn.cursor() as cursor:
        cursor.execute(inst, {'id_est': id_est})
        cursor.close()
      inst =  '''
              select h.id_hist
                from historia h, estudiante_historia eh
                where h.id_hist = eh.id_hist and eh.id_est = %(id_est)s
                  and h.apertura_hist = (select max(apertura_hist) from historia)
                  and h.id_hist = (select max(id_hist) from historia)
                  and h.estado_hist = 'proceso';
              '''
      with conn.cursor() as cursor:
        cursor.execute(inst, {'id_est': id_est})
        for row in cursor.fetchall():
          id_hist = row[0]
        cursor.close()
    
    inst =  '''
            insert into test_resuelto(puntaje_total)
              values (0)
              returning id_test_res;
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        id_test_res = row[0]
      cursor.close()
    
    print(id_test_res)
    
    inst =  '''
            insert into historia_test_resuelto(id_hist, id_test_res)
	            values (%(id_hist)s, %(id_test_res)s);
            '''
    
    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_hist':id_hist, 'id_test_res':id_test_res})
      cursor.close()
    
    result = ''
    
    for fila in matrizPreg:
      result += "\n"
      id_pregunta = fila[0]
      puntaje = fila[1]
      result += f'((select id_test_preg from test_pregunta where id_preg = {id_pregunta}), {puntaje}),'
      
    result = result.rstrip(result[-1]) + "\n"
    
    inst =  'insert into test_detalle(id_test_preg, puntaje)\n values ' + result + '\nreturning id_test_det;'
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        id_test_det_array.append(row[0])
      cursor.close()
    
    print(id_test_det_array)
    
    result = ''
    
    for id in id_test_det_array:
      result += "\n"
      result += f'({id_test_res}, {id}),'
    
    result = result.rstrip(result[-1]) + "\n"
    
    inst =  'insert into test_resuelto_detalle(id_test_res, id_test_det)\n values ' + result + ';'
    
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      cursor.close()
    
    inst =  '''
            update test_resuelto
              set puntaje_total = (
                select sum(td.puntaje) from test_resuelto_detalle trd, test_detalle td
                where trd.id_test_det = td.id_test_det and trd.id_test_res = %(id_test_res)s
              )
              where id_test_res = %(id_test_res)s;
            '''

    with conn.cursor() as cursor:
      cursor.execute(inst, {'id_test_res': id_test_res})
      conn.commit()
      cursor.close()
    conn.close()
    
    return True
  
  except Exception as e:
    print("(SISTEMA)   Error: "+str(e))
    return False