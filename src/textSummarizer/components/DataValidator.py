"""README > 5. Update components """

import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationEntity


class DataValidation:
    def __init__(self, data_validation_config: DataValidationEntity):
        self.configs = data_validation_config

    #Şimdi aşağıdaki method "artifacts\data_receiver\samsum_dataset" dosyası altında test, train ve validation diye 3 tane folder var mı kontrol edecek.
    def validate_data(self):
        counter = 0

        print(self.configs.root_directory)
        list_of_required_files = self.configs.required_files_list
        list_of_current_folders = os.listdir("artifacts\data_receiver\samsum_dataset")

        for i in range(len(list_of_required_files)):
            for j in range(len(list_of_current_folders)):
                if list_of_required_files[i] == list_of_current_folders[j]:
                    counter += 1

        status_file_path = self.configs.status_file
        if(counter == 3):
            with open(status_file_path, "w") as f:
                f.write(f"Validation is satisfied! {True}")
            return True
        else:
            with open(status_file_path, "w") as f:
                f.write(f"Validation is NOT satisfied! {False}")
            return False


""" config_manager_obj = ConfigManagerValidation()

data_validation_config =  config_manager_obj.get_config_data_validation() 
data_validation_instance = DataValidation(data_validation_config=data_validation_config)
data_validation_instance.validate_data() """