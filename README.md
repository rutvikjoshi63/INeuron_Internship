# INeuron_Internship
Start Date: 23rd March 2024

# Table of Content:


# 1. Description of work:
| Project                    	| Description                              	|
|----------------------------	|------------------------------------------	|
| Title                      	| Concrete Compressive Strength Prediction 	|
| Technologies               	| Machine Learning Technology              	|
| Domain                     	| Infra                                    	|
| Project Difficulties level 	| Intermediate                             	|

# 2. Problem Statement:
The quality of concrete is determined by its compressive strength, which is measured
using a conventional crushing test on a concrete cylinder. The strength of the concrete
is also a vital aspect in achieving the requisite longevity. It will take 28 days to test
strength, which is a long period. So, what will we do now? We can save a lot of time and
effort by using Data Science to estimate how much quantity of which raw material we
need for acceptable compressive strength.

# 3. Software and Tools Requirements
1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Heroku Account](https://heroku.com)
4. [Git Cli](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

# 4. Workflow & Environment Setup 
## 4.1 Create a repository on github and connect with your local and add Readme.md file
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
## 4.2 Create a account on [DagsHub([]](https://dagshub.com/rutvikjoshi63/INeuron_Internship)) and connect with your Github
Add details of Experiments from Remote
Open Git Bash and Export Tracking, username, password,etc by entering below command
 ```
export text
```
## 4.3 Create a new virtual environment
### Deactivate current(base) environment
```
conda create -p CCStrength_Prediction python==3.9 -y
```
Activate new environment
## 4.4 Create template.py file to automate files & folder creation
```
python template.py
```
## 4.5 Add require libraries in requirement.txt file 
eg DVC for large dats sets(ref: https://youtu.be/mHQPzVse2oA?si=jlFSTR4FnSqXcHHP)
-e. will look for setup.py
```
pip install -r requirements.txt
# if applicable
dvc init
```
## 4.6 Make changes to setup.py file
## 4.7 Install requirements.txt & commit changes
```
pip install -r requirements.txt
```
To include all the basic functionality required in all End-to-End ML Projects
___
**Start of Logging Imprementation**
## 4.8 Make changes to src/mlProject/__init__.py file
## 4.9 Make changes to main.py file
## 4.10 Make changes to src/mlProject/utlis/common.py file 
1. Look into new libraries like ConfigBox from box library to recall dictionary value using "." operator
2. Check use of ensure_annotations to restrict usuage of datatype 
We have research/trials.ipynb to check functionalities or code checking
___
# 5. Data Ingestion
## 5.1 Setup 
Create 01_data_ingestion.ipynb file in research folder & Update files in below order
- config.yaml
- params.yaml # skip initially
- entity (data_ingestion.ipynb, constants/__init__.py)
- configuration manager in src config
- components
- pipeline
- main.py
- dvc.yaml
- app.py
Now **Run main.py**

# 6. Data Validation
## 6.1 Setup
Create 01_data_ingestion.ipynb file in research folder & Update files in below order
- schema.yaml
- entity (data_validation.ipynb, constants/__init__.py)
- config.yaml
- components
- pipeline
- main.py
## 6.2 Exploratory Data Analysis
Note insights in the data and manage **NULL** values

# 7. Data Transformation
## 7.1 Setup
Create 01_data_ingestion.ipynb file in research folder & Update files in below order
- entity (data_validation.ipynb, constants/__init__.py)
- config.yaml
- components
- pipeline
- main.py
## 7.2 Create Train and Test data

# 8. Model Trainer
## 8.1 Setup
Create 01_data_ingestion.ipynb file in research folder & Update files in below order
- entity (data_validation.ipynb, constants/__init__.py)
- config.yaml
- components
- pipeline
- main.py

## 8.2 Create Train and Test data
- config.yaml

# 9. Model Evaluation
Here we add mlflow code
## MLflow [Documentation](https://mlflow.org/docs/latest/index.html)
 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model
##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/rutvikjoshi63/INeuron_Internship.mlflow \
MLFLOW_TRACKING_USERNAME=rutvikjoshi63 \
MLFLOW_TRACKING_PASSWORD=257a616cf210c0f00c447611343adbe61470744c \
python script.py

## 7.1 Setup
Create 01_data_ingestion.ipynb file in research folder & Update files in below order
- entity
- config.yaml
- components
- pipeline
- main.py

## 7.2 Create Train and Test data
- config.yaml


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



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```
Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/rutvikjoshi63/INeuron_Internship.mlflow \
export MLFLOW_TRACKING_USERNAME=rutvikjoshi63 \
export MLFLOW_TRACKING_PASSWORD=257a616cf210c0f00c447611343adbe61470744c \
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
