import os
import sys
from datetime import datetime
from config import keys, bin

# Change binaries if tags exist.
for i in range(len(sys.argv)):
    if sys.argv[i] == "-w":
        bin["webPos"] = i
        bin["web"] = True
    if sys.argv[i] == "-c":
        bin["commPos"] = i
        bin["comm"] = True

# Initial Variables
commentList = ''
keys["callerReference"] = datetime.now().strftime("%Y-%m-%d-%H:%M")

# Case 1: Default Case. 
# Usage: python createHostedZone.py

if (bin["web"] + bin["comm"]) == 0 :
    keys["PRIVATEZONE"] = '"' + keys["PRIVATEZONE"] + '"'
    cmd2 = "aws route53 create-hosted-zone" + " --name " + keys["domainName"] + " --caller-reference " + keys["callerReference"] + " --hosted-zone-config PrivateZone=" + keys["PRIVATEZONE"]

# Case 2: tags exist

if (bin["web"] + bin["comm"]) > 0:

    # Case 2a: custom web tag
    # Usage: python createHostedZone.py -w <domain name>

    if bin["web"] == True:
        keys["domainName"] = sys.argv[bin["webPos"]+1]
        keys["PRIVATEZONE"] = '"' + keys["PRIVATEZONE"] + '"'
        cmd2 = "aws route53 create-hosted-zone" + " --name " + keys["domainName"] + " --caller-reference " + keys["callerReference"] + " --hosted-zone-config PrivateZone=" + keys["PRIVATEZONE"]

    # Case 2b: Add comment tag  
    # Usage python createdHostedZone.py -c <comments>

    if bin["comm"] == True:
        for i in range(len(sys.argv)-(bin["commPos"]+1)):
            commentList = commentList + sys.argv[i+bin["commPos"] + 1] + ' '
        keys["comment"] = ",Comment=" + '"' + commentList + '"'
        cmd2 = "aws route53 create-hosted-zone" + " --name " + keys["domainName"] + " --caller-reference " + keys["callerReference"] + " --hosted-zone-config PrivateZone=" + keys["PRIVATEZONE"] + keys["comment"]
    
# Run command/debug

pStart = Popen(cmd2, shell=True)
pStart.wait()
# print(cmd2)