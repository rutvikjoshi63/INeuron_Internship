import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from mlProject.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        x = data.iloc[:,:-1]
        y = data.iloc[:,-1]
        x.head()
        y.head()
        # Split the data into training and test sets. (0.75, 0.25) split.
        X_train, x_test,y_train,y_test = train_test_split(x, y,test_size =0.3, random_state = 42)
        ## Standardize the Dataset
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        ## Not fit_transform...but transform only bcoz we need to transformed as per train model
        x_test = scaler.transform(x_test)
        
        # train, test = train_test_split(data)
        print('X_train',X_train)
        print('y_train',y_train)
        print('x_test',x_test)
        print('y_test',y_test) 
        
        arr = [i for i in data.columns]
        X_train_df = pd.DataFrame(X_train,columns=arr[:-1])
        y_train_df = pd.DataFrame(y_train,columns=[arr[-1]])
        x_test_df = pd.DataFrame(x_test,columns=arr[:-1])
        y_test_df = pd.DataFrame(y_test,columns=[arr[-1]])
        
        X_train_df.to_csv(os.path.join(self.config.root_dir, "x_train.csv"),index = False)
        y_train_df.to_csv(os.path.join(self.config.root_dir, "x_test.csv"),index = False)
        x_test_df.to_csv(os.path.join(self.config.root_dir, "y_train.csv"),index = False)
        y_test_df.to_csv(os.path.join(self.config.root_dir, "y_test.csv"),index = False)
        
        logger.info("Splited data into training and test sets")
        logger.info(X_train.shape)
        logger.info(x_test.shape)
        logger.info(y_train.shape)
        logger.info(y_test.shape)

        print(X_train.shape)
        print(y_train.shape)
        print(x_test.shape)
        print(y_test.shape)
        