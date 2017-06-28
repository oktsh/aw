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
    attributes = ["displayname", "mail"], #"distinguishedName"
    where_clause = "objectClass = '*'",
    #base_dn = "OU = Users, OU=921_Office, DC=domainru,DC=ru,DC=auchan,DC=com"
    base_dn = "OU = Users,OU = "+line+", DC = domainru, DC = ru, DC = auchan, DC = com"
    )

    for row in q.get_results():
        print row
