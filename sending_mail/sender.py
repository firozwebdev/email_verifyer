import smtplib,socket

# sender_mail = 'scottrhodes2496@gmail.com'
# receivers_mail = ['everythingkst@gmail.com']
message = """From: From Person %s  
To: To Person %s  

MIME-Version:1.0  
Content-type:text/html  


Subject: Sending SMTP e-mail   

<h3>Python SMTP</h3>  
<strong>This is a test e-mail message.</strong>  
"""
try:
    sender_mail = 'islamshajibul86@gmail.com'
    receivers_mail = ['everythingkst@gmail.com']
    password ='aoosovmlptbfisqw'
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.login(sender_mail, password)
    # smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully sent email")
except socket.error as e:
    print(f"Error: unable to send email: {e}")