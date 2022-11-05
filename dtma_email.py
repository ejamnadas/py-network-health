import smtplib, ssl

def send(msg):
  port = 465  # For SSL
  password = "asdf*888" 

  # Create a secure SSL context
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login("ejamnadas@datuma.io", password)
      server.sendmail("ejamnadas@datuma.io", "ejamnadas@datuma.io", msg)