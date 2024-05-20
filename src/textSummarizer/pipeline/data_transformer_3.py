from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.DataTransformer import DataTransformer
from textSummarizer.utils.common import get_size
from textSummarizer.logging import logger

class DataTransformerPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config_manager_obj = ConfigurationManager()
            data_transformation_config =  config_manager_obj.get_config_data_transformation() 
            data_transformation_instance = DataTransformer(config=data_transformation_config)
            data_transformation_instance.convert()
        except Exception as e:
            raise e