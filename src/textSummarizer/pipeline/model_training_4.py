from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.ModelTrainer import ModelTrainer
from textSummarizer.utils.common import get_size
from textSummarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_config_model_trainer()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e