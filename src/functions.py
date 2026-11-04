# =======================================================================
# FUNCTIONS
# Define reusable helper functions in this file.
# =======================================================================
import numpy as np
import pandas as pd
from constants import *
from sklearn import train_test_split

# load the csv into a pandas df
def load_data():
    df = pd.read_csv(DATASET)
    return df


# hold out a test set that is only touched once, at the very end
def split_data(df):
    x = df[FEATURES]
    y = df[TARGET]
    return train_test_split(x, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

