# AWS_CLI_Automation
This script is a set of functions to generate instances and hosted zones on AWS via automation of its CLI console.

## Requirements
There are no explicit package requirements for this software as all the packages used are native python and work with Unix based operating systems. However, AWS console installation is required.

## Installation

### AWS Console Installation:
[AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install/)  
Follow the steps outlined in their docs. Can use either **curl** or download the **zip file**.  
**IMPORTANT**: Please make sure to either update to the latest version or install it (Any version >= 2 is fine).

### AWS Console Configuration
1. Open the command line
2. use the command:
```bash
aws configure
```
3. Enter in the following. If you do not have access to the access keys, please get in touch with myself or the project owner.  
  a) Access Key ID,  
  b)	Secret Access Key,  
  c)	Default region name: this should be **ca-central-1**  
  d)	Default output format (I prefer json, but its up to the user)  

### Installing git
Ignore this step if you already have git installed on your machine.
1. install:  
```bash
sudo apt-get update
sudo apt-get install git -y
```
2. Configure your username (replace "First Last")  
```bash
git config --global user.name "First Last"
```
3. Configure your email (replace the email)  
```bash
git config --global user.email "example@example.com"
```

### Install the software
1. Install:
```bash
git clone https://github.com/kichichoi102/AWS_CLI_Automation.git
```
2. Change directories
```bash
cd ~/AWS_CLI_Automation
```
3.	Occasionally use pull command to make sure your version is up to date!
```bash
git pull https://github.com/kichichoi102/AWS_CLI_Automation.git master
```
That’s all the steps. Open command and test if main.py works!

## Usage
### main.py
```python
python main.py -i instance1 instance2 instance3 -p micro_2_0 -t tag1 tag2 tag3 -w trial.onecourt.com -c test comment
```
### createInstance.py
```python
python createInstance.py -i instance1 instance2 instance3 -p micro_2_0 -t tag1 tag2 tag3
```
### createHostedZone.py
```python
python createHostedZone.py -w trial.onecourt.com -c test comment
```

## Full Document
[See Full Document here](https://drive.google.com/file/d/11oq92o08Wjav_fSqHv2T3HqGkYrxa6sx/view?usp=sharing)
