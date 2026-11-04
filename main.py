# =====================================================================
# MAIN PROGRAM
# Your code starts here. This is the file that will be run.
# =====================================================================

import src.functions as sf  # This allows you to access functions from functions.py using sf.function_name()
from src.classes import Batch  # This allows you to import individual Classes from classes.py
from src.constants import *  # This imports all constants from constants.py

# 1. load the data and hold out a test set
df = sf.load_data()
x_train, x_test, y_train, y_test = sf.split_data(df)

