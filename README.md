# Repo to introduce key ML/AI/TensorFlow concepts to RSDAS.
Created by: Tony Held (tony.held@arb.ca.gov)

## Introduction:
1) Key ML/AI concepts using TensorFlow are introduced in this repo including data pre-processing, 
regression, image processing, time series analysis, and Natural language processing (NLP).
2) Codebase was created as a subset of Tony's Google TensorFlow Certification code and notes  
that has been modified to be useful for satellite and other RSDAS analysis.
3) Repo is initially populated with the following files:
   * tf_util.py:  python utility classes and functions useful for ML/TensorFlow
   * carb_ml_overview_no_output.ipynb: jupyter notebook with code only (no run output)
   * carb_ml_overview_25_epochs_output.ipynb: jupyter notebook with model results of 25 epochs of training
   * mini_conda_02.yml: python conda requirements file containing instructions on how to set up a local ML python interpreter

## Local Machine Usage:
1) Clone this repo to the local directory of your choosing
   * https://github.com/tony-held-carb/ml_rsdas 
2) Inspect the 25_epochs jupyter notebook to get a sense of the project and its output
3) Create a local interpreter following mini_conda_02.yml instructions
4) Save the no_output notebook as a new file
5) Change the number of epochs and run flags at the top of the notebook (if desired)
6) Get coffee and popcorn and settle in for a long training time if you are on a CARB laptop :)

## Running on Colab:
1) open colab in your browser at https://colab.research.google.com/
2) The open-notebook modal form will likely pop up, if not go to File -> Open Notebook
3) Select GitHub and enter tony-held-carb for the user and click the magnifying glass
4) Select the tony-held-carb/ml_rsdas and the main branch
5) You will only be able to open one of the notebooks, you can choose the no_output of 25_epochs_output.  
Although it is a relatively big file (20 megs), you likely want to open the file with output to
be able to see what expected output looks like.
6) You can run the model in Colab by selecting Runtime->Run All
7) Unless you have a GPU enabled in your Colab session, model training may be very slow
8) You must save a copy of the notebook to your local account (you can't directly modify the repo file clone)




