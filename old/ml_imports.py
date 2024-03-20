#######################################
# Comprehensive ML import list
#######################################

import IPython.display
import collections
import copy
import importlib
import itertools
import json
import os
import pathlib
import random
import shutil
import sys
import tarfile
import urllib.request
import zipfile

from datetime import datetime
from os.path import exists
from packaging import version
from pathlib import Path
from urllib.parse import urlparse
from zipfile import ZipFile

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import tensorflow as tf

from keras import Sequential, layers, models, regularizers
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Activation
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import image_dataset_from_directory, img_to_array, load_img, plot_model
from sklearn import set_config
from sklearn.compose import ColumnTransformer, make_column_selector, make_column_transformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler
from tensorflow import keras
from tensorflow.keras.layers import TextVectorization

# tensorflow_hub is not a required package on the Google cert exam interpreter
# it may not be load if strict compliance with minimal exam requirements are used
try:
  import tensorflow_hub as hub
except ModuleNotFoundError:
  print(f"tensorflow_hub package not available")

# global variable to test import success
ml_imports_loaded = True
