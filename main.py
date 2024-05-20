from textSummarizer.pipeline.data_receiver_1 import DataReceiverTrainingPipeline
from textSummarizer.pipeline.data_validator_2 import DataValidationPipeline

from textSummarizer.logging import logger

try:
    logger.info(f"Data Receiving has been started.")
    data_receiver = DataReceiverTrainingPipeline()
    data_receiver.main() #data_receiver_1'deki main() çağrılıyor.
    logger.info(f"Data Receiving has been completed.")

except Exception as e:
    logger.error(f"Data Receiving has been failed.")
    logger.error(f"Error: {e}")
    logger.error(f"Traceback: {e.format_exc()}")
    raise e

try:
    logger.info(f"Data Validation has been started.")
    data_validation_pipeline_instance = DataValidationPipeline()
    data_validation_pipeline_instance.main() #data_receiver_2'deki main() çağrılıyor.
    logger.info(f"Data Validation has been completed.")

except Exception as e:
    logger.error(f"Data Validation has been failed.")
    logger.error(f"Error: {e}")
    raise e
