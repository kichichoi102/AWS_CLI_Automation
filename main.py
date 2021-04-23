import os
import sys
from subprocess import Popen
from datetime import datetime
from config import keys, bin

'''
arg1: createInstance.py
arg2: <instance names, list>
arg3: <bundle ID, string>
arg4: <tags, list>
arg5: <domain name, string>
arg6: <comment, list>
'''

# Change binaries if tags exist
for i in range(len(sys.argv)):
    if sys.argv[i] == "-i":
        bin["inst"] = True
        bin["instPos"] = i
    if sys.argv[i] == "-p":
        bin["bundPos"] = i
        bin["bund"] = True
    if sys.argv[i] == "-t":
        bin["tagPos"] = i
        bin["tag"] = True
    if sys.argv[i] == "-w":
        bin["webPos"] = i
        bin["web"] = True
    if sys.argv[i] == "-c":
        bin["commPos"] = i
        bin["comm"] = True


# Initial Variables
instanceList = ''
keyList = ''
for i in range(len(keys["keyValue"])):
        keyList = keyList + "key=" '"'  + keys["keyValue"][i] + '" '

commentList = ''
keys["callerReference"] = datetime.now().strftime("%Y-%m-%d-%H:%M")
# keys["PRIVATEZONE"] = '"' + keys["PRIVATEZONE"] + '"'


# Case 1: Default
# Usage: python createInstance.py

if (bin["inst"] + bin["bund"] + bin["tag"]) == 0 and len(sys.argv) < 2:
    ''' Default case '''
    cmd1 = "aws lightsail create-instances"  + " --instance-names " + keys["instanceName"] + " --availability-zone " + keys["AVAILIBILITY_ZONE"] + " --region " + keys["REGION"] + " --blueprint-id " + keys["BLUEPRINT_ID"] + " --bundle-id " + keys["bundleID"] + " --tags " + keyList
    pStart = Popen(cmd1, shell=True)
    pStart.wait()

    # cmd1 = "aws lightsail --instance-names {0} {1} --available-zone {2}".format(var1, var2, var3)

# Case 2: Help function.
# Usage: python createInstance.py -h

elif sys.argv[1] == "-h":
    ''' help function '''
    print("help function here")


elif (bin["inst"] + bin["bund"] + bin["tag"]) >= 1 and len(sys.argv) >= 3:

    # Case 3: With instance name edits <-i>
    # Usage: python createInstance.py -i instance-1 instance-2 ...

    if bin["inst"] == True:

        if bin["bund"] == True:
            vector = bin["bundPos"]
        elif bin["tag"] == True:
            vector = bin["tagPos"]
        else:
            vector = len(sys.argv)

        for i in range(vector - (bin["instPos"]+1)):
            instanceList = instanceList + sys.argv[i+2] + ' '

    # Case 4: With Price bundle edit <-p>
    # Usage: python createInstance.py -p micro_2_0

    if bin["bund"] == True:
        keys["bundleID"] = sys.argv[bin["bundPos"]+1]

    # Case 5: Custom Key Values <-t>
    # Usage python createInstance.py -t CFNOC Sprint Email Phishing ...

    # --tags key="cfnoc" key="hello" key="tag3"
    
    if bin["tag"] == True:
        keyList = ''
        # if (bin["tag"] or bin["comm"]) == True:
        #     if bin["web"] == 0:
        #         for i in range(bin["commPos"] - (bin["tagPos"])):
        #             keyList = keyList + "key=" '"'  + sys.argv[i+(bin["tagPos"]+1)] + '" '
        #     if bin["comm"] == 0:
        #         for i in range(bin["webPos"] - (bin["tagPos"])):
        #             keyList = keyList + "key=" '"'  + sys.argv[i+(bin["tagPos"]+1)] + '" '
        # else:
        if (bin["web"] or bin["comm"]) == True:
            if bin["web"] == 0:
                for i in range(bin["commPos"] - (bin["tagPos"]+1)):
                    keyList = keyList + "key=" '"'  + sys.argv[i+(bin["tagPos"]+1)] + '" '
            if bin["comm"] == 0:
                for i in range(bin["webPos"] - (bin["tagPos"]+1)):
                    keyList = keyList + "key=" '"'  + sys.argv[i+(bin["tagPos"]+1)] + '" '
        else:
            for i in range(len(sys.argv) - (bin["tagPos"]+1)):
                keyList = keyList + "key=" '"'  + sys.argv[i+(bin["tagPos"]+1)] + '" '

    cmd1 = "aws lightsail create-instances"  + " --instance-names " + instanceList + " --availability-zone " + keys["AVAILIBILITY_ZONE"] + " --region " + keys["REGION"] + " --blueprint-id " + keys["BLUEPRINT_ID"] + " --bundle-id " + keys["bundleID"] + " --tags " + keyList
    pStart = Popen(cmd1, shell=True)
    pStart.wait()
    # print(cmd1)

else:
    print("Refer to manual for usage or -help or -h")
    print("Usage: python createInstance.py -i <instance name> -p <bundleID> -t <tags>")


if (bin["web"] + bin["comm"]) == 0 :
    keys["PRIVATEZONE"] = '"' + keys["PRIVATEZONE"] + '"'
    cmd2 = "aws route53 create-hosted-zone" + " --name " + keys["domainName"] + " --caller-reference " + keys["callerReference"] + " --hosted-zone-config PrivateZone=" + keys["PRIVATEZONE"]
    pStart = Popen(cmd2, shell=True)
    pStart.wait()

elif (bin["web"] + bin["comm"]) > 0:
    if bin["web"] == True:
        keys["domainName"] = sys.argv[bin["webPos"]+1]
        keys["PRIVATEZONE"] = '"' + keys["PRIVATEZONE"] + '"'
        cmd2 = "aws route53 create-hosted-zone" + " --name " + keys["domainName"] + " --caller-reference " + keys["callerReference"] + " --hosted-zone-config PrivateZone=" + keys["PRIVATEZONE"]
        pStart = Popen(cmd2, shell=True)
        pStart.wait()

    if bin["comm"] == True:
        for i in range(len(sys.argv)-(bin["commPos"]+1)):
            commentList = commentList + sys.argv[i+bin["commPos"] + 1] + ' '
        keys["comment"] = ",Comment=" + '"' + commentList + '"'
    
    
    cmd2 = "aws route53 create-hosted-zone" + " --name " + keys["domainName"] + " --caller-reference " + keys["callerReference"] + " --hosted-zone-config PrivateZone=" + keys["PRIVATEZONE"] + keys["comment"]
    # print(cmd2)
    pStart = Popen(cmd2, shell=True)
    pStart.wait()






# if __name__ == "__main__":
#     createInstance(keys)