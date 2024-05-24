from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger
from textSummarizer.components.ModelEvaluation import ModelEvaluation

"""README > 6. Update pipeline"""
class ModelEvaluationPipeline: 
    
    def __init__(self):
        pass
    def main(self):
        try:
            config_manager_obj = ConfigurationManager()
            model_evaluation_config =  config_manager_obj.get_config_model_evaluation() 
            model_evaluation_instance = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_instance.evaluate_model()
        except Exception as e:
            raise e