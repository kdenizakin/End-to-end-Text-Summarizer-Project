from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.DataReceiver import DataReceiver
from textSummarizer.utils.common import get_size
from textSummarizer.logging import logger

class DataReceiverTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config_manager_obj = ConfigurationManager()
            data_receiver_config =  config_manager_obj.get_config()
            data_receiver = DataReceiver(data_receiver_config=data_receiver_config)
            data_receiver.download_data()
            data_receiver.extract_data()
            logger.info(f"Extracted data from {data_receiver_config.local_data_file} to {data_receiver_config.unzip_dir} with size {get_size(data_receiver_config.unzip_dir)}")
        except Exception as e:
            raise e