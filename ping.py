import os
import smtplib, ssl
import email
import variables
  
property = variables.getProperty()

def check_ping(hostname, descr):

    response = os.system("ping -c 3 " + hostname)
    print(response)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
        email(property + ' ping failed for ' + hostname +"(" + descr + ")")
    
    return pingstatus


