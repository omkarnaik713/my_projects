# -*- coding: utf-8 -*-
"""Space Titanic

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lpvA8HAFIelWEXgMpVNwwGOI8u-jis-B
"""

import pandas as pd
dataset = pd.read_csv('Train.csv')

print(dataset.shape)

dataset.isnull().sum()

dataset.dropna(inplace=True)
dataset['Transported'].value_counts()

"""It is a balanced dataset."""

dataset.shape

dataset.head()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
label = le.fit_transform(dataset['Transported'])
label

dataset.drop('Transported', axis = 1, inplace = True)
dataset['transported'] = label
dataset.head()

dataset.shape

target = dataset['transported']
dataset.drop('transported',axis = 1, inplace = True)

dataset.drop(['PassengerId','Name','Cabin'], axis = 1, inplace = True)
dataset.head()

label_planet = le.fit_transform(dataset['HomePlanet'])
label_sleep = le.fit_transform(dataset['CryoSleep'])
label_destination = le.fit_transform(dataset['Destination'])
label_vip = le.fit_transform(dataset['VIP'])

dataset['homeplanet'] = label_planet
dataset['cryosleep'] = label_sleep
dataset['destination'] = label_destination
dataset['vip'] = label_vip

dataset.head()

dataset.drop(['HomePlanet','CryoSleep','Destination','VIP'],axis = 1 , inplace = True)
dataset.head()

dataset.shape

target.shape
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(dataset,target,test_size = 0.2)

from sklearn.linear_model import Perceptron
model = Perceptron()
model.fit(x_train,y_train)

y_predict = model.predict(x_test)

y_predict.reshape(-1,1)

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_predict)

from sklearn.linear_model import LogisticRegression
model_log = LogisticRegression()
model_log.fit(x_train,y_train)
y_pred_log = model_log.predict(x_test)
accuracy_score(y_test,y_pred_log)

from sklearn.svm import SVC
model_svc = SVC()
model_svc.fit(x_train,y_train)
y_pred_svc = model_svc.predict(x_test)
accuracy_score(y_test,y_pred_svc)

from sklearn.tree import DecisionTreeClassifier
model_tree = DecisionTreeClassifier()
model_tree.fit(x_train,y_train)
y_pred_tree = model_tree.predict(x_test)
accuracy_score(y_test, y_pred_tree)

from sklearn.neural_network import MLPClassifier
model_nn = MLPClassifier()
model_nn.fit(x_train,y_train)
y_pred_nn = model_nn.predict(x_test)
accuracy_score(y_test,y_pred_nn)

"""Next step is to increase the accuracy by finding the best hyperparameters for these models

"""
