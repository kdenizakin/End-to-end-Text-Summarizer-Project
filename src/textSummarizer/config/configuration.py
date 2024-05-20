#Şimdi "README.md" dosyasında yer alan 4. adım olan "4. Update the configuration manager in src config" adımda sıra. 
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataReceiverConfig


class ConfigurationManager: 
    def __init__( self, config_filepath = FILE_PATH_CONFIG, params_filepath = FILE_PATH_PARAMS):
        
        #common.py dosyasındaki read_yaml() fonksiyonu ile yaml dosyasını okuyoruz.
        self.config = read_yaml(config_filepath) #Aslında Path("config/config.yaml")
        self.params = read_yaml(params_filepath) #Aslında Path("params.yaml")

        create_directories([self.config.artifacts_root]) #artifacts_root: artifacts. Bu method ile "artifacts" isimli folder otomatik olarak oluşturulur.
        #"." kullanarak çağırmayı "ConfigBox"a borçluyuz.

    def get_config(self):
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