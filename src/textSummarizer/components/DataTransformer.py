"""README > 5. Update components """
import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationEntity


class DataTransformer:
    def __init__(self, config: DataTransformationEntity):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer)
    
    def convert_examples_to_features(self, example_batch):

        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
        """ 
        Tokenizer, metinleri modelin anlayabileceği tokenlere dönüştüren bir objecttir. Mesela cümledeki her bir harf bir token yapılabilir. 
        Benzer şekilde cümledeki her bir kelime de token yapılabilir.
        Yani tokenizerlar ile metin daha küçük paraçalara ayrılır.
        max_length = 1024 demek, tokenlere ayrılacak olan metnin maximum uzunluğunu göstermektedir. 
        "truncation = True" parametresi ise eğer metin 1024 karakterden daha uzun ise kesileceği anlamına gelir. 
        """

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        return { #Burada ise datanın featurelarına "input_ids, attention_mask, labels" columnlarını eklemekteyiz.
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
    }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        saving_dir = os.path.join(self.config.root_dir, "samsum_dataset")
        dataset_samsum_pt.save_to_disk(saving_dir)