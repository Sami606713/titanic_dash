from src.exception import Coustom_exception
from src.logger import logging
import os,sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngesitionConfig:
    raw_data_path:str=os.path.join("data","data.csv")
    train_data_path:str=os.path.join("data","train_data.csv")
    test_data_path:str=os.path.join("data","test_data.csv")

class DataIngesition:
    def __init__(self):
        self.data_ingesition=DataIngesitionConfig()

    def Inilize_Data(self):
        try:
            logging.info("Enter the data ingesition")

            data=pd.read_csv("Notebooks\\tested.csv")
            logging.info("reading the dataset as dataframe")

            logging.info("make a folder for raw data path")
            os.makedirs(os.path.dirname(self.data_ingesition.train_data_path),exist_ok=True)

            logging.info("convert to csv file of raw data")

            data.to_csv(self.data_ingesition.raw_data_path,index=False,header=True)

            logging.info("Train test split")
            train_data,test_data=train_test_split(data,test_size=0.2,random_state=42)

            logging.info("save the train data")
            train_data.to_csv(self.data_ingesition.train_data_path)

            logging.info("save the test data")
            test_data.to_csv(self.data_ingesition.test_data_path)

            logging.info("data ingesition complete")

            return (
                self.data_ingesition.train_data_path,
                self.data_ingesition.test_data_path
            )
        except Exception as e:
            raise Coustom_exception(e,sys)

if __name__=="__main__":
    obj=DataIngesition()
    obj.Inilize_Data()