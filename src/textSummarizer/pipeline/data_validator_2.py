
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger
from textSummarizer.components.DataValidator import DataValidation

"""README > 6. Update pipeline"""
class DataValidationPipeline: 
    
    def __init__(self):
        pass
    def main(self):
        try:
            config_manager_obj = ConfigurationManager()
            data_validation_config =  config_manager_obj.get_config_data_validation() 
            data_validation_instance = DataValidation(data_validation_config=data_validation_config)
            validation_status= data_validation_instance.validate_data() 
            logger.info(f"Data Validation has been performed and resulted with status: {validation_status}")
        except Exception as e:
            raise e
