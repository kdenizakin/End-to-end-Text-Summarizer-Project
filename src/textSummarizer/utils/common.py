#Utils kullanmamızın nedeni mesela sık sık kullandığımız bir python fonksiyonu olsun, utils>common ile bu fonksiyonu sadece bir 
#kez yazarak her seferinde kullanmak için sadece bu common.py dosyasını import etmek yeterlidir. Yani aslında bir module yapıyoruz.

import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger #daha önce oluşturduğumuz custom loggerı import ediyoruz.
from ensure import ensure_annotations 
from box import ConfigBox #YAML dosyalarını "ConfigBox" tipinde okumamızın nedeni bir dictionarydeki kayıtlara ".key" yazarak ulaşabilmek. Başka bir amacı yoktur.
from pathlib import Path
from typing import Any

@ensure_annotations #Bunun nedeni de parametre olarak kullandığımız değişkenlerin tipleri, fonksiyonun çağırırken başka tipteki değişkenler vererek çağırınca değişmesin diye.
#Yani bir nevi dynamic type binding gibi bir çevirme yapılmasın diye kullanılır.
def read_yaml(pathh: Path) -> ConfigBox:
    try:
        with open(pathh) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {pathh} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def get_size(path:Path)->str:
    kbs = round(os.path.getsize(path)/1024)
    return f"~	{kbs} KBs"        