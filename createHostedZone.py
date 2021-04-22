import os
import sys
from datetime import datetime
from config import keys


#  $ aws route53 create-hosted-zone 
# --name trial.onecourt.com 
# --caller-reference 2014-04-01-18:47 
# --hosted-zone-config 
# PrivateZone="false",
# Comment="hello"

commentList = ''
keys["callerReference"] = datetime.now().strftime("%Y-%m-%d-%H:%M")

if len(sys.argv) == 2:
    keys["domainName"] = sys.argv[1]
    keys["PRIVATEZONE"] = '"' + keys["PRIVATEZONE"] + '"'
    cmd = "aws route53 create-hosted-zone" + " --name " + keys["domainName"] + " --caller-reference " + keys["callerReference"] + " --hosted-zone-config PrivateZone=" + keys["PRIVATEZONE"]
    print(cmd)

elif len(sys.argv) > 2:
    keys["domainName"] = sys.argv[1]
    keys["PRIVATEZONE"] = '"' + keys["PRIVATEZONE"] + '"'

    for i in range(len(sys.argv)-2):
        commentList = commentList + sys.argv[i+2] + ' '
    keys["comment"] = '"' + commentList + '"'
    cmd = "aws route53 create-hosted-zone" + " --name " + keys["domainName"] + " --caller-reference " + keys["callerReference"] + " --hosted-zone-config PrivateZone=" + keys["PRIVATEZONE"] + ",Comment=" + keys["comment"]
    print(cmd)
else:
    cmd = "aws route53 create-hosted-zone" + " --name " + keys["domainName"] + " --caller-reference " + keys["callerReference"]
    print(cmd)
