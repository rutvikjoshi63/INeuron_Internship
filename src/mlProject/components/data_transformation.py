import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from mlProject.entity.config_entity import DataTransformationConfig
import numpy as np



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
        
        train = np.hstack((X_train,np.atleast_2d(np.array(y_train)).T))
        test = np.hstack((x_test,np.atleast_2d(np.array(y_test)).T))
        
        arr = [i for i in data.columns]
        train_df = pd.DataFrame(train,columns=arr[:])
        test_df = pd.DataFrame(test,columns=arr[:])
        train_df.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test_df.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)
        
        logger.info("Splited data into training and test sets")
        logger.info(train_df.shape)
        logger.info(test_df.shape)

        print(train_df.shape)
        print(test_df.shape)
        