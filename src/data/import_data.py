import zipfile
import os

def import_raw_data():
    
    os.system("kaggle competitions download -c house-prices-advanced-regression-techniques")
    os.system("move house-prices-advanced-regression-techniques.zip ../data/raw")
    with zipfile.ZipFile("../data/raw/house-prices-advanced-regression-techniques.zip","r") as zip_ref:
        zip_ref.extractall("../data/raw")
    os.remove("../data/raw/house-prices-advanced-regression-techniques.zip")
    
    return