#!python3
import pyad.adquery
import os
import sys

scriptDir = sys.path[0]
uname= os.path.join(scriptDir, 'uname.txt')
OU = open(uname, "r")
lines = OU.readlines()

for line in lines:
    line = line.strip()
    q = pyad.adquery.ADQuery()

#ORG = raw_input('Enter OU:')

    q.execute_query(
    attributes = ["name", "description".decode('utf-8')], #"distinguishedName"
    where_clause = "objectClass = '*'",
    #base_dn = "OU = Users, OU=921_Office, DC=domainru,DC=ru,DC=auchan,DC=com"
    base_dn = "OU = Computers,OU = "+line+", DC = domainru, DC = ru, DC = auchan, DC = com"
    )

    for row in q.get_results():
        try:
          print (row["name"]),
          print (row ["description"][0])
        except TypeError:
            print(row["description"])
