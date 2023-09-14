import pandas
ds = pandas.read_csv('senders_list.csv')
dr = pandas.read_csv('receivers_list.csv')
sender_email = ds['username']
password = ds['password']
receiver_email = dr['email']
# for i in range(len(email)):
#     print(f"email : {email[i]} and password :{password[i]}")

# Collecting Receivers Email from list


