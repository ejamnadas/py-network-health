import pg_conn

def save_hb(device, property):
  conn = pg_conn.get_conn()
  cursor = conn.cursor()
  cursor.execute("INSERT INTO ntw_hb_log(hb_device, property, hb_datetime) VALUES(%s, %s, current_timestamp)", (device, property))
  #cursor.execute("INSERT INTO ntw_hb_log(hb_device, property) VALUES('test', 'test')")
  conn.commit()
  cursor.close()
  conn.close()

def get_last_hb_in_min(property):
  conn = pg_conn.get_conn()
  cursor = conn.cursor()
  cursor.execute("select property, minutes from ntw_last_hb_in_min where property = %s", (property,))
  res = cursor.fetchone()
  #cursor.execute("INSERT INTO ntw_hb_log(hb_device, property) VALUES('test', 'test')")
  cursor.close()
  conn.close()
  return res[1]



def clear_hb():
  conn = pg_conn.get_conn()
  cursor = conn.cursor()
  cursor.execute("delete from ntw_hb_log where hb_datetime < NOW() - INTERVAL '2 DAY'")
  #cursor.execute("INSERT INTO ntw_hb_log(hb_device, property) VALUES('test', 'test')")
  conn.commit()
  cursor.close()
  conn.close()