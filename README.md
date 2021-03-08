# Mushrooms
 Identifying a mushroom as edible or poisonous

 The dataset is from UCI Machine Learning Repository
 https://archive.ics.uci.edu/ml/datasets/Mushroom

## Data Set Information:

This data set includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family (pp. 500-525). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like ``leaflets three, let it be'' for Poisonous Oak and Ivy.

## Files containing the data:

1.data/agaricus-lepiota.data  - dataset
2.data/agaricus-lepiota.names - field description and other information on the data

## Files in this directory
1. Mushroom Classification.ipynb - Main Jupyter Notebook
2. app.py - streamlit script file
3. requirements.txt - dependencies for hosting on Heroku
4. setup.sh - Heroku required file
5. mushroon_model.h5 - tensorflow model
6. mushroom_model_LR.pkl - Liner Regression model with scikit-learn , used on Heroku

You can see the app running here:
https://mushroom-identification.herokuapp.com/

### Running the app on desktop

1. Clone the repository
2. Install streamlit library as "pip install streamlit"
3. streamlit run app.py
