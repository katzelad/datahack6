import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse
import xgboost as xg

from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))

data = parse.parse_data("data/train.csv")


def train(data):
    x = data[:,1:5]
    y= data[:,0]
    seed = 7
    test_size = 0.2
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=seed)

    model = xg.XGBClassifier()
    model.fit(X_train, y_train,verbose=1)

    pred = model.predict(X_test)

    predictions = [round(value) for value in pred]
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))



train(data)
