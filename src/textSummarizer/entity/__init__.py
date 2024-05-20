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