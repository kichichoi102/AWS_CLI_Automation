# AWS_CLI_Automation
This script is a set of functions to generate instances and hosted zones on AWS via automation of its CLI console.

## Requirements
There are no explicit package requirements for this software as all the packages used are native python and work with Unix based operating systems. However, AWS console installation is required.

## AWS Console Installation:
[AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install/)  
Follow the steps outlined in their docs. Can use either **curl** or download the **zip file**.  
**IMPORTANT**: Please make sure to either update to the latest version or install it (Any version >= 2 is fine).

## AWS Console Configuration
1. Open the command line
2. use the command:
'''bash
aws configure
'''
3. Enter in the following. If you do not have access to the access keys, please get in touch with myself or the project owner.  
  a) Access Key ID,  
  b)	Secret Access Key,  
  c)	Default region name: this should be ca-central-1  
  d)	Default output format (I prefer json, but its up to the user)  


