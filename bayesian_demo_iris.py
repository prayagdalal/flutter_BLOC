# -*- coding: utf-8 -*-
"""Bayesian_demo_iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1anPU8TrEZBAoztECU7UB0RL1C-JOTkQA
"""

import numpy as np
import pandas as pd

df=pd.read_csv("Iris.csv")
df.head()

df["Species"].value_counts()

X=df[["SepalLengthCm",	"SepalWidthCm",	"PetalLengthCm",	"PetalWidthCm"]].values
Y=df["Species"].values

from sklearn.preprocessing import  LabelEncoder
le=LabelEncoder()
Y=le.fit_transform(Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X,Y, test_size=0.3)

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_train, Y_train)

Y_pred=model.predict(X_test)
Y_pred

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test, Y_pred)
cm

for i in range(30):
  print(i, Y_test[i], Y_pred[i])

from sklearn.metrics import accuracy_score
asc = accuracy_score(Y_test, Y_pred)*100
asc