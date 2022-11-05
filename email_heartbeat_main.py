import variables
import dtma_save_hb
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localhost = s.getsockname()[0]
s.close()

property = variables.getProperty()

msg = variables.getProperty() + " alert device heartbeat"

dtma_save_hb.save_hb('alert_device ' + localhost, property)

