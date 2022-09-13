import os
import smtplib, ssl

  
def check_ping(hostname, descr):

    response = os.system("ping -c 3 " + hostname)
    print(response)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
        email('ping failed for ' + hostname +"(" + descr + ")")
    
    return pingstatus

def email(msg):
  port = 465  # For SSL
  password = "asdf*888" 

  # Create a secure SSL context
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login("ejamnadas@datuma.io", password)
      server.sendmail("ejamnadas@datuma.io", "ejamnadas@datuma.io", msg)


