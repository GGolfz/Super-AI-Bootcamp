from sklearn.datasets import load_iris
from sklearn.linear_modal import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import numpy as np
import pandas as pd

iris = load_iris()
X,y = iris['data'],iris['target']
dataset = np.hstack((X,y.reshape(-1,1)))
np.random.shuffle(dataset)
X_train,X_test,y_train,y_test = train_test_split(dataset[:,:4],dataset[:,4],test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy_score(y_test,y_pred)
joblib.dump(model,'iris.model')