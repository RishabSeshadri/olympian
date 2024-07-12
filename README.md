# olympian

  For our project, we decided to predict the winning country for each sport for the 2024 Olympics! To define a 'winner',
we said that it would be the country with the most 'points' scored - 3 points are given for golds, 2 for silver, and 1 for bronze. 

  We started the process with some data visualization to try to find correlations between the different types of data we had. We found that
historical winners and the number of medals (as well as type) they placed per sport was relevant when trying to predict future winners. 
We preprocessed our data to include past Olympic medal counts over the last 40 years as features. We picked a Random Forest Regressor 
as our model with hyperparameters n_estimators (max number of trees in the forest) = 100. We then trained our model on 120 years of historical 
Olympic data and predicted for 2024. We took these predictions, merged them into the organized dataframe, and saved the dataframe to a CSV
file. We then took this predictions.csv file and incorporated it to display into our frontend. 

  While our predictions aren't completely accurate, with more time we could see great progress. We have built the infrastructure or "pipeline" 
for this process. Our project is far from finished, but with this pipeline, we can now explore more models, experiment with hyperparameters 
and more features, and work towards better predictions.

## Framework
Python: Kaggle, Pandas, SKLearn, MatPlotLib, ReactPy

-----------------------------------------------

## Execution:

Make sure you have Pip and Python installed. Then, using your pip:
```
pip install reactpy
pip install pandas
```

To run the script itself:
```
python olympics.py
```

Then, visit your [localhost](http://127.0.0.1:8000) to view the webpage.

-----------------------------------------------

## Authors:
Sarayu Ramachandra, Rishab Seshadri


![image](https://github.com/user-attachments/assets/54562a51-cac9-42c0-be79-dbf5ae44019e)
