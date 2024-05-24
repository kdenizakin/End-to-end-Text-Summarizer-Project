from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataReceiverConfig: #Bu bir python actual classı değildir bir Data Class'tır.
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#Bu bir fonksiyonun return type'ı gibidir. Mesela bir "DataIngestionConfig" instance oluşturduğumuz zaman bu variableları return edecek. Bu variableları
#gerektiği zamanlarda kullanacağız.
#Mesela "root_dir" çağırırsak "config.yaml" dosyası içerisindeki "artifacts/data_ingestion" pathini return edecek.
#Bu bir ENTİTY'DİR.

"""README > 3. Update entity """

@dataclass(frozen=True)
class DataValidationEntity: #Bu bir python actual classı değildir bir Data Class'tır.
    root_directory: Path
    status_file: str
    required_files_list:list

"""README > 3. Update entity """


@dataclass(frozen=True)
class DataTransformationEntity:
    root_dir: Path #artifacts/data_transformation
    data_path: Path #artifacts/data_receiver/samsum_dataset
    tokenizer: Path #google/pegasus-cnn-dailymail. Automatically download the tokenizer.


@dataclass(frozen=True)
class ModelTrainingEntity:
    root_dir: Path 
    data_path: Path 
    checkpoints: Path 
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int



@dataclass(frozen=True)
class ModelEvaluationEntity:
    root_dir: Path 
    data_path: Path 
    model_path: Path 
    tokenizer_path:Path
    metric_file_name: Path
