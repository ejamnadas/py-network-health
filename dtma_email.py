from email.message import EmailMessage
import smtplib, ssl

def send(subject, body):
  port = 465  # For SSL
  password = "asdf*888" 

  # Create a secure SSL context
  context = ssl.create_default_context()

  msg = EmailMessage()
  msg.set_content(body)
  msg['Subject'] = subject
  msg['From'] =  "ejamnadas@datuma.io"
  msg['To'] ="ejamnadas@datuma.io" 

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login("ejamnadas@datuma.io", password)
      server.send_message(msg)
      server.quit()

      #server.sendmail("ejamnadas@datuma.io", "ejamnadas@datuma.io", msg)