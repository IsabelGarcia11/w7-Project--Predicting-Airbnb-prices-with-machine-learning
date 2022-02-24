# w7-Project

# Predicting Airbnb prices with machine learning


<img src="fotos/ams.jpg?raw=true" width="800" height="200" />

**TARGET**

The objective of this project is to predict the prices of different Airbnb accommodation options in the city of Amsterdam through a machine learning model.

For this we use the csv 'train', which collects the different characteristics of those accommodations to later test those price predictions (obtained from the different models used) in the csv 'test'.

It is divided into two Jupyter Notebooks:
* *Train_1*: Has been used to do the first predictions.

* *Train_2*: Used to predict with different models but with a different data treatment, outliers have been removed. 

### Train_1
<img src = "fotos/ml.jpg?raw=true" width="800" height="200">

Firstly, we have downloaded the different datasets from [Kaggle](https://www.kaggle.com/c/airbnb-madrid-ironhack/data), containing training, test and sample data.

We proceeded to do a thorough cleaning of the data, removing any correlation between them, null values, among many other things. 

In this first 'training' we used different models but the one that gives us the best result is the CTR() with an rmse of 85.

<img src = "fotos/py.jpg?raw=true" width="50" height="50">

All the functions used in this process are located in the cleaning4 file inside the src folder.

### Train_2

In this second analysis, we have left characteristics, related to review scores, that we had previously eliminated.  We have also eliminated all data considered outliers, both in price and in the number of reviews for each host. 

Here we have obtained results with lower rmse than in train_1 but with less 'overfitting' between train R² and test R².

**CONCLUSIONS**

<img src = "fotos/res.jpg?raw=true" width="800" height="200">

We can conclude that in train_2, by making the aforementioned modifications to the data, we are closer to reality, they are more generalist models than in train_1 since the difference between the rmse obtained and the real rmse (once the competition is over) is smaller. 

In the results folder, there are all the price predictions obtained in the two train files.

**LINKS & RESOURCES**
* https://www.kaggle.com/c/airbnb-madrid-ironhack/overview
* https://numpy.org/doc/1.18/
* https://pandas.pydata.org/
* https://docs.python.org/3/library/functions.html
* https://docs.python.org/3/library/json.html
* https://python-visualization.github.io/folium/
* https://docs.python.org/3/library/time.html
* https://scikit-learn.org/stable/