import opendatasets as od
import os

def download_kaggle_data():
    """
    Downloads the Parkinson's Disease Progression Prediction dataset from Kaggle and saves it to the local file system.
    This function uses the opendatasets package to download the dataset from Kaggle, renames the downloaded directory to 'raw',
    and saves it to the './data' directory in the local file system. If the './data' directory does not exist, it will be created."""

    if not os.path.exists('./data'):
        os.makedirs('./data')
    od.download(r'https://www.kaggle.com/competitions/amp-parkinsons-disease-progression-prediction',   data_dir='./data/01_raw')
    print("Download complete.")
