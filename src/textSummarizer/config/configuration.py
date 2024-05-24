#Şimdi "README.md" dosyasında yer alan 4. adım olan "4. Update the configuration manager in src config" adımda sıra. 
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataReceiverConfig
from textSummarizer.entity import DataValidationEntity
from textSummarizer.entity import DataTransformationEntity
from textSummarizer.entity import ModelTrainingEntity
from textSummarizer.entity import ModelEvaluationEntity


class ConfigurationManager: 
    def __init__( self, config_filepath = FILE_PATH_CONFIG, params_filepath = FILE_PATH_PARAMS):
        
        #common.py dosyasındaki read_yaml() fonksiyonu ile yaml dosyasını okuyoruz.
        self.config = read_yaml(config_filepath) #Aslında Path("config/config.yaml")
        self.params = read_yaml(params_filepath) #Aslında Path("params.yaml")

        create_directories([self.config.artifacts_root]) #artifacts_root: artifacts. Bu method ile "artifacts" isimli folder otomatik olarak oluşturulur.
        #"." kullanarak çağırmayı "ConfigBox"a borçluyuz.

    def get_config_data_receiver(self):
        config = self.config.data_receiver #Alttakine erişiyoruz. read_yaml(config_filepath) ile bu config.yaml dosyasını okuduk.
        #data_data_receiver:
            #root_dir: artifacts/data_receiver
            #source_URL: https://github.com/kdenizakin/End-to-end-Text-Summarizer-Project/raw/main/text_summarizer_dataset.zip #bu URL'den datayı indirecek.
            #local_data_file: artifacts/data_receiver/data.zip #datayı bu foldera ve "data.zip" ismiyle indirecek.
            #unzip_dir: artifacts/data_receiver #datanın unzip edilmiş hali buraya download edilecek.

        create_directories([config.root_dir])

        data_receiver_config = DataReceiverConfig(
            root_dir = config.root_dir, # config.root_dir = "artifacts/data_receiver". Yani artifacts/data_receiver isimli bir dosya oluşturulacak.
            source_URL = config.source_URL,
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )

        return data_receiver_config
    
    def get_config_data_validation(self)-> DataValidationEntity: 
       
        create_directories([self.config.data_validation.root_dir]) #root_dir: artifacts/data_validation.

        print(f"{self.config.data_validation}")
        """ve alttakine erişiyoruz:
         data_validation:
            root_dir: artifacts/data_validation
            status_file: artifacts/data_validation/status.txt
            required_files: ["train","test","validation"] """

        data_validation_config_obj = DataValidationEntity(
            root_directory = self.config.data_validation.root_dir, 
            status_file = self.config.data_validation.status_file,
            required_files_list = self.config.data_validation.required_files,
        ) 

        return data_validation_config_obj
    
    def get_config_data_transformation(self) -> DataTransformationEntity:
        
        create_directories([self.config.data_transformation.root_dir])

        """ConfigBox kullanmadan böyle de attributelar çağrılabilir."""
        return DataTransformationEntity(
            root_dir = self.config.data_transformation.root_dir,
            data_path = self.config.data_transformation.data_path,
            tokenizer = self.config.data_transformation.tokenizer
        )
    

    def get_config_model_trainer(self) -> ModelTrainingEntity:
        
        parameters_of_the_model = self.params.TrainingParameters

        create_directories([self.config.model_training.root_dir])

        """ConfigBox kullanmadan böyle de attributelar çağrılabilir."""
        return ModelTrainingEntity(
            root_dir= self.config.model_training.root_dir, 
            data_path=self.config.model_training.data_path,
            checkpoints=self.config.model_training.model_checkpoints,
            num_train_epochs= parameters_of_the_model.num_train_epochs,
            warmup_steps=parameters_of_the_model.warmup_steps,
            per_device_train_batch_size= parameters_of_the_model.per_device_train_batch_size,
            weight_decay = parameters_of_the_model.weight_decay,
            logging_steps = parameters_of_the_model.logging_steps,
            evaluation_strategy = parameters_of_the_model.evaluation_strategy,
            eval_steps = parameters_of_the_model.eval_steps,
            save_steps = parameters_of_the_model.save_steps,
            gradient_accumulation_steps = parameters_of_the_model.gradient_accumulation_steps
        )
    
    def get_config_model_evaluation(self) -> ModelEvaluationEntity:

        config_model_evaluation = self.config.model_evaluation
        create_directories([config_model_evaluation.root_dir])
        return ModelEvaluationEntity(
            root_dir = config_model_evaluation.root_dir,
            data_path = config_model_evaluation.data_path,
            model_path = config_model_evaluation.model_path,
            tokenizer_path = config_model_evaluation.tokenizer_path,
            metric_file_name = config_model_evaluation.metric_file_name
        )