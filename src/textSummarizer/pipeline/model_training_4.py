from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.ModelTrainer import ModelTrainer
from textSummarizer.utils.common import get_size
from textSummarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.model_trainer_config = self.config.get_config_model_trainer()


    def main(self):
        try:
            model_trainer_config = ModelTrainer(config=self.model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e