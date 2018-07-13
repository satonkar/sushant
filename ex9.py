import smtplib

sender = 'sushantsatonkar23@gmail.com'
receivers = ['sushant.satonkar@nagra.com']

message = """From: From Person <sushantsatonkar23@gmail.com>
To: To Person <sushant.satonkar@nagra.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
