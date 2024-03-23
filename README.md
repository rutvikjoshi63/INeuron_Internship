# INeuron_Internship
Start Date: 23rd March 2024

# Table of Content:


# Description of work:
| Project                    	| Description                              	|
|----------------------------	|------------------------------------------	|
| Title                      	| Concrete Compressive Strength Prediction 	|
| Technologies               	| Machine Learning Technology              	|
| Domain                     	| Infra                                    	|
| Project Difficulties level 	| Intermediate                             	|

# Problem Statement:
The quality of concrete is determined by its compressive strength, which is measured
using a conventional crushing test on a concrete cylinder. The strength of the concrete
is also a vital aspect in achieving the requisite longevity. It will take 28 days to test
strength, which is a long period. So, what will we do now? We can save a lot of time and
effort by using Data Science to estimate how much quantity of which raw material we
need for acceptable compressive strength.

# Software and Tools Requirements
1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Heroku Account](https://heroku.com)
4. [Git Cli](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

# Workflow & Environment Setup 
## Create a repository on github and connect with your local and add Readme.md file
```
git init
git add .
git commit -m "first commit"
git branch -M main
git status
git remote add origin git@github.com:rutvikjoshi63/INeuron_Internship.git
git pull origin

```
Add environment name in .gitignore file and push to remote
## Create a account on DagsHub and connect with your Github
Add details of Experiments from Remote
Open Git Bash and Export Tracking, username, password,etc by entering below command
 ```
export text
```
## Create a new virtual environment
### Deactivate current(base) environment
```
conda create -p CCStrength_Prediction python==3.9 -y
```
Activate new environment

## Create a new requirement.txt file and add require libraries
eg DVC for large dats sets(ref: https://youtu.be/mHQPzVse2oA?si=jlFSTR4FnSqXcHHP)
```
pip install -r requirements.txt
# if applicable
dvc init
```
## Create template.py file to automate files & folder creation
```
```

## Create app.py file to either taking template from MLflow website
to add remote server like DAGShub, GCP, AWS, Azure add below code
```
# For Remotee server only(servername)
remote_server_uri = "{url}"
mlflow.set_tracking_uri(remote_server_uri)
```
Open git bash and type
```
python app.py
```
# 
