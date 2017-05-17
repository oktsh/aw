import subprocess
import os
import sys
import re

scriptDir = sys.path[0]
hosts = os.path.join(scriptDir, 'hosts.txt')
hostname = open(hosts, "r")
lines = hostname.readlines()

if os.path.exists('ping.txt'):
    os.remove('ping.txt')
    print ("ping.txt FOUND \n")
    print ("Removing old file:  ping.txt \n")
    print ("Writing clean file:  ping.txt \n")
else:
    print ("Writing new file: ping.txt \n")

for line in lines:
    line = line.strip()
    # args = ["ping", "-n", "1", line]

    """ping = subprocess.Popen(
        #args,
        ['ping','-n','1',line],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

    out, error = ping.communicate()"""

    output = subprocess.Popen(["ping", "-n", "1", line], stdout=subprocess.PIPE).communicate()[0]
    regex = re.compile(r"from\s(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)")
    r = regex.findall(output)

    print(r)

    # print(out.decode('ASCII'))

    f = open('ping.txt', 'a')
    f.write("Hostname:  " + line + " " + str(r) + "\n")
