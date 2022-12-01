import variables
import dtma_ntw_pg as pg
import socket
import dtma_email as em

def hb_save(property):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    localhost = s.getsockname()[0]
    s.close()


    msg = property + " alert device heartbeat"

    pg.save_hb('alert_device ' + localhost, property)
  except Exception as e:
    pg.save_hb('(exception {e} ) alert_device ' + localhost, property)

def hb_clear():
  try:
    pg.clear_hb()
  except Exception as e:
    pg.save_hb('(exception {e} ) alert_device', 'all')

def last_hb_in_min_fail(property):
  healthy = False

  try:
    minutes = pg.get_last_hb_in_min(property)
    if(minutes > 1):
      healthy =False 
    else:
      healthy =True 
  except Exception as e:
    healthy = False
    em.send(property + ' Heart Beat Fail', property + '(Exception {e}) Last communication from ' + property + ' greater than 2 minutes')

  if healthy == False:
    em.send(property + ' Heart Beat Fail', property + ' Last communication from ' + property + 'greater than 2 minutes')