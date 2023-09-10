import pandas

dt = pandas.read_csv('email.csv').to_dict()
email = dt['Email']
i = 0
while i < len(dt['Email']):
    l = v.verify(email[i])
    print(l['address'][1] + ' ... ' + str(l['deliverable']))
    i += 1
