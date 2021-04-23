keys = {
    "instanceName"      : 'CFNOC-Sprint7-Email',
    "AVAILIBILITY_ZONE" : "us-east-2a",
    "REGION"            : "us-east-2",
    "BLUEPRINT_ID"      : "ubuntu_20_04",
    "bundleID"          : "micro_2_0",
    
    # Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
    "keyValue" : [
        "CFNOC", 
        "Sprint", 
        "Email", 
        "Phishing", 
        "etc"
    ],

    "domainName"        : "trial.onecourt.ca",
    "callerReference"   : '',
    "PRIVATEZONE"       : 'false',
    "comment"           : ''
}

bin = {
    "inst"    : False,
    "instPos" : 0,

    "bund"     : False,
    "bundPos" : 0,

    "tag"      : False,
    "tagPos"   : 0,

    "web"      : False,
    "webPos"   : 0,

    "comm"     : False,
    "commPos"  : 0
}



# "aws lightsail create-instances 
# --instance-names test1 
# --availability-zone ca-central-1a 
# --region ca-central-1 
# --blueprint-id ubuntu_20_04 
# --bundle-id micro_2_0
# [--tags <value>]"
# --tags key=cfnoc key=sprint

#   create-instances
# --instance-names <value>
# --availability-zone <value>
# [--custom-image-name <value>]
# --blueprint-id <value>
# --bundle-id <value>
# [--user-data <value>]
# [--key-pair-name <value>]
# [--tags <value>]
# [--add-ons <value>]
# [--ip-address-type <value>]
# [--cli-input-json | --cli-input-yaml]
# [--generate-cli-skeleton <value>]