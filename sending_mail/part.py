import datetime
import time,random

import pandas
from verifier import Verifier
ds = pandas.read_csv('senders_list.csv')
dr = pandas.read_csv('receivers_list.csv')
sender_email = ds['username']
password = ds['password']
receiver_email = dr['email']
# for i in range(len(email)):
#     print(f"email : {email[i]} and password :{password[i]}")

print("Email is sending, Be patient")
number = range(1,10)
# print(len(receiver_email))
print(random.choice(number))


i = 0

while i < len(receiver_email):
    # l = v.verify(email[i])
    # verified = l['deliverable'] == True and 'Verified' or 'Not Verified'
    # valid = l['valid_format'] == True and 'Valid' or 'Not Valid'
    # print(l['address'][1] + ' is  ' + str(valid) + ' and  ' + str(verified))
    # print(f"email : {sender_email[i]} and password :{password[i]}")
    print(f"email : {receiver_email[i]} ")
    i += 1
print("Verification completed, Thanks for your patience")


