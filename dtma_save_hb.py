import pg_conn

def save_hb(device, property):
  conn = pg_conn.get_conn()
  cursor = conn.cursor()
  cursor.execute("INSERT INTO ntw_hb_log(hb_device, property, hb_datetime) VALUES(%s, %s, current_timestamp)", (device, property))
  #cursor.execute("INSERT INTO ntw_hb_log(hb_device, property) VALUES('test', 'test')")
  conn.commit()
  cursor.close()
  conn.close()