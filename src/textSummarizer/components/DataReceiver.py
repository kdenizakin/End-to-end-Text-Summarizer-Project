import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataReceiverConfig

class DataReceiver:
    def __init__(self, data_receiver_config: DataReceiverConfig):
        self.config = data_receiver_config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_URL,self.config.local_data_file) #config.yaml'dan tüm pathleri alıyoruz.
            logger.info(f"Downloaded data from {self.config.source_URL} to {self.config.local_data_file} with information: {headers}")
        else:
            logger.info(f"Data already exists at {self.config.local_data_file}")

    #Datayı download ettikten sonra extract edilmesi de gerekmektedir.
    def extract_data(self):
        folder_path_to_unzip = self.config.unzip_dir
        os.makedirs(folder_path_to_unzip, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(folder_path_to_unzip)

