from textSummarizer.pipeline.data_receiver_1 import DataReceiverTrainingPipeline
from textSummarizer.pipeline.data_validator_2 import DataValidationPipeline
from textSummarizer.pipeline.data_transformer_3 import DataTransformerPipeline
from textSummarizer.pipeline.model_training_4 import ModelTrainingPipeline
from textSummarizer.pipeline.model_evaluation_5 import ModelEvaluationPipeline


from textSummarizer.logging import logger

try:
    logger.info(f"Data Receiving has been started.")
    data_receiver = DataReceiverTrainingPipeline()
    data_receiver.main() #data_receiver_1'deki main() çağrılıyor.
    logger.info(f"Data Receiving has been completed.\n \n")

except Exception as e:
    logger.error(f"Data Receiving has been failed.\n \n")
    logger.error(f"Error: {e}")
    logger.error(f"Traceback: {e.format_exc()}")
    raise e

try:
    logger.info(f"Data Validation has been started.")
    data_validation_pipeline_instance = DataValidationPipeline()
    data_validation_pipeline_instance.main() #data_receiver_2'deki main() çağrılıyor.
    logger.info(f"Data Validation has been completed.\n \n")

except Exception as e:
    logger.error(f"Data Validation has been failed.\n \n")
    logger.error(f"Error: {e}")
    raise e

try:
    logger.info(f"Data Transformation has been started.")
    data_transformation_pipeline_instance = DataTransformerPipeline()
    data_transformation_pipeline_instance.main()
    logger.info(f"Data transformation has been completed.\n \n")

except Exception as e:
    logger.error(f"Data transformation has been failed.\n \n")
    logger.error(f"Error: {e}")
    raise e

""" try:
    logger.info(f"Model Training has been started.")
    model_training_pipeline_instance = ModelTrainingPipeline()
    model_training_pipeline_instance.main()
    logger.info(f"Model Training has been completed.\n \n")

except Exception as e:
    logger.error(f"Model Training has been failed.\n \n")
    logger.error(f"Error: {e}")
    raise e """



try:
    logger.info(f"Model Evaluation has been started.")
    model_evaluation_pipeline_instance = ModelEvaluationPipeline()
    model_evaluation_pipeline_instance.main()
    logger.info(f"Model Evaluation has been completed.\n \n")

except Exception as e:
    logger.error(f"Model Evaluation has been failed.\n \n")
    logger.error(f"Error: {e}")
    raise e
