import os
import sys
from subprocess import Popen
from config import keys, bin

'''
arg1: createInstance.py
arg2: <instance names, list>
arg3: <bundle ID, string>
arg4: <tags, list>
'''


# Change binaries if tags exist
for i in range(len(sys.argv)):
    if sys.argv[i] == "-i":
        bin["inst"] = True
        bin["namePos"] = i
    if sys.argv[i] == "-p":
        bin["pricePos"] = i
        bin["bund"] = True
    if sys.argv[i] == "-t":
        bin["tagPos"] = i
        bin["tag"] = True


# Initial Variables
instanceList = ''
keyList = ''
for i in range(len(keys["keyValue"])):
        keyList = keyList + "key=" '"'  + keys["keyValue"][i] + '" '


# Case 1: Default
# Usage: python createInstance.py

# --tags key="cfnoc" key="hello" key="tag3"

if (bin["inst"] + bin["bund"] + bin["tag"]) == 0 and len(sys.argv) < 2:
    ''' Default case '''
    cmd1 = "aws lightsail create-instances"  + " --instance-names " + keys["instanceName"] + " --availability-zone " + keys["AVAILIBILITY_ZONE"] + " --region " + keys["REGION"] + " --blueprint-id " + keys["BLUEPRINT_ID"] + " --bundle-id " + keys["bundleID"] + " --tags " + keyList

elif (bin["inst"] + bin["bund"] + bin["tag"]) >= 1 and len(sys.argv) >= 3:

    # Case 3: With instance name edits <-i>
    # Usage: python createInstance.py -i instance-1 instance-2 ...

    if bin["inst"] == True:

        if bin["bund"] == True:
            vector = bin["pricePos"]
        elif bin["tag"] == True:
            vector = bin["tagPos"]
        elif (bin["tag"] and bin["bund"]) == True:
            vector = bin["pricePos"]
        else:
            vector = len(sys.argv)

        for i in range(vector - (bin["namePos"]+1)):
            instanceList = instanceList + sys.argv[i+2] + ' '

    # Case 4: With Price bundle edit <-p>
    # Usage: python createInstance.py -p micro_2_0

    if bin["bund"] == True:
        keys["bundleID"] = sys.argv[bin["pricePos"]+1]

    # Case 5: Custom Key Values <-t>
    # Usage python createInstance.py -t CFNOC Sprint Email Phishing ...

    # --tags key="cfnoc" key="hello" key="tag3"
    
    if bin["tag"] == True:
        keyList = ''
        for i in range(len(sys.argv) - (bin["tagPos"]+1)):
            keyList = keyList + "key=" '"'  + sys.argv[i+(bin["tagPos"]+1)] + '" '
    cmd1 = "aws lightsail create-instances"  + " --instance-names " + instanceList + " --availability-zone " + keys["AVAILIBILITY_ZONE"] + " --region " + keys["REGION"] + " --blueprint-id " + keys["BLUEPRINT_ID"] + " --bundle-id " + keys["bundleID"] + " --tags " + keyList

else:
    print("Refer to manual for usage or -help or -h")
    print("Usage: python createInstance.py -i <instance name> -p <bundleID> -t <tags>")

# Run command/debug
pStart = Popen(cmd1, shell=True)
pStart.wait()

# print(cmd1)
