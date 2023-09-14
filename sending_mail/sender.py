import smtplib, socket, ssl
import time, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas


# Define the HTML document

def html_template(file_num):
    with open(f"templates/file-{file_num}.html", 'r') as f:
        html_data = f.read()
    return html_data


ds = pandas.read_csv('senders_list.csv')
dr = pandas.read_csv('receivers_list.csv')
sender_email = ds['username']
password = ds['password']
receiver_email = dr['email']
i = 0
failure_counter = 0
date_str = pandas.Timestamp.today().strftime('%Y-%m-%d')


# Below code are working with single sender to multiple receivers
try:

    while i < len(receiver_email):
        sender_mail = 'tryan6745@gmail.com'
        sender_password = 'papxetftgyewdtar'
        receivers_mail = receiver_email[i]

        email_message = MIMEMultipart()
        email_message['From'] = sender_mail
        email_message['To'] = receiver_email[i]
        email_message['Subject'] = f'Report email - {date_str}'

        # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
        file_num = random.choice(range(1, 5))
        html = html_template(file_num)

        email_message.attach(MIMEText(html, "html"))
        # Convert it as a string
        email_string = email_message.as_string().format(email=receiver_email[i])

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_mail, sender_password)
            server.sendmail(sender_mail, receiver_email[i], email_string)
        print(f"Successfully sent email to {receiver_email[i]}")
        number = range(1, 6)
        time.sleep(random.choice(number))
        i += 1
except socket.error as e:
    failure_counter += 1
    print(f"Error: failure to send email: {failure_counter}")
    print(f"Error: unable to send email: {e}")
    pass
