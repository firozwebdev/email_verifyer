import smtplib, socket
import time, random
import pandas

message = """From: From Person %s  
    To: To Person %s  

    MIME-Version:1.0  
    Content-type:text/html  


    Subject: Sending SMTP e-mail   

    <h3>Python SMTP</h3>  
    <strong>This is a test e-mail message.</strong>  
    """


ds = pandas.read_csv('senders_list.csv')
dr = pandas.read_csv('receivers_list.csv')
sender_email = ds['username']
password = ds['password']
receiver_email = dr['email']
i = 0
failure_counter = 0
try:
    while i < len(receiver_email):
        sender_mail = 'tryan6745@gmail.com'
        sender_password = 'papxetftgyewdtar'
        receivers_mail = receiver_email[i]
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpObj.login(sender_mail, sender_password)
        # smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender_mail, receiver_email[i], message)  # single sender to multiple receivers
        print(f"Successfully sent email to {receiver_email[i]}")
        number = range(1, 6)
        time.sleep(random.choice(number))
        i += 1
except socket.error as e:
    failure_counter += 1
    print(f"Error: failure to send email: {failure_counter}")
    print(f"Error: unable to send email: {e}")
    pass
