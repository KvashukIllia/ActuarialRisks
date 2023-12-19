import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import zipfile
# Load the dataset
# Make sure to adjust the file path as per your setup in Colab
zip_file_path = 'actuarial-loss-estimation.zip'

# Extracting and loading the train.csv file
with zipfile.ZipFile(zip_file_path, 'r') as z:
    with z.open('train.csv') as f:
        data = pd.read_csv(f)
        