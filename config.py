import os


PATH = os.path.dirname(os.path.realpath(__file__))

DATA_PATH = "C:/Users/samra/OneDrive/Documents/Datasets/"

EPSILON = 1e-8

if DATA_PATH is None:
    raise Exception('Configure your data folder location in config.py before continuing!')
