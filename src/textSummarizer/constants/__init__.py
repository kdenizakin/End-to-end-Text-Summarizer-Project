#Bu dosyada değişmemesi gereken dosya pathleri gibi constant variablelar tutulacaktır.
#Yani projede bu pathlere her grek olduğunda onları hard kodlamaktansa buradaki variablelardan okunacaklar.

from pathlib import Path

FILE_PATH_CONFIG = Path("config/config.yaml")
FILE_PATH_PARAMS = Path("params.yaml")