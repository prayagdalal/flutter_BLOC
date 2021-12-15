# -*- coding: utf-8 -*-
"""Copy of KNN_demo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XJ_-gg0FeiXHRXA56iQQHWvW_NT2-dxe
"""

import numpy as np
import pandas as pd

df=pd.read_csv("Iris.csv")
df.head()

X=df[["SepalLengthCm", "SepalWidthCm",	"PetalLengthCm", "PetalWidthCm"]].values
Y=df["Species"].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X,Y, test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
model.fit(X_train, Y_train)

Y_pred=model.predict(X_test)
Y_pred

from sklearn.metrics import  confusion_matrix
cm=confusion_matrix(Y_pred, Y_test)
cm

for i in range(30):
  print(Y_pred[i],"  ",Y_test[i])