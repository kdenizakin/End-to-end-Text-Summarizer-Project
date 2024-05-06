import os
from pathlib import Path
import logging #log the information in runtime.

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    #Next line is important for CI CD deployment.
    ".github/workflows/.gitkeep", #With this line we create a folder in the github repository.
    f"src/{project_name}/__init__.py", #her bir folder için bir "constructor" dosyası olmalı ki import from... şeklinde import edebilelim.
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", #for utility related code. 
    f"src/{project_name}/utils/common.py", #tüm "utility"ler buraya yazılacaktır.
    f"src/{project_name}/logging/__init__.py", 
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py", 
    f"src/{project_name}/entity/__init__.py", 
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml",
    "params.yaml", #we will keep all the model related parameters.
    "app.py",
    "main.py",
    "Dockerfile", #to make the deployments"
    "requirements.txt", #it will contain all the requirements of our project.
    "setup.py", #it will help us to do this local package setup. 
    "research/trails.ipynb", #research will contain all the notebook experiments. trails.ipynb is a notebook.
]

for filepath in list_of_files:
    filepath = Path(filepath) #bu "Path" fonksiyonu işletim sistemine göre otomatik bir biçimde path biçimlendirmesini anlamaktadır.
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #eğer yanlışlıkla "template.py"ı dosyalarda kod varken çalıştırırsak
                                                                            #ve de file boyutunun 0 olup olmadığını kontrol etmez isek tüm dosyalardaki kod
                                                                            #silinir. Mesela bir dosya dolu diğerleri boş ise dolu olan dosya ignore edilecek ve
                                                                            #diğer dosya isimleri için yeni dosya oluşturulacaktır.
        with open(filepath,"w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")

