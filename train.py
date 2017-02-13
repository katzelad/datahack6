import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse
import xgboost as xg
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.cluster import DBSCAN
from sklearn import metrics
import matplotlib.pyplot as plt


class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))

print "Loading data..."

data = parse.parse_data("data/subtrain.csv")

print "Data loaded!"

def train(data,test_size=0.25,val_size=0.1):
    X = data[:,1:6]
    y = data[:,0]
    target_names = ['class 0', 'class 1', 'class 2']

    seed=42
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)

    model = get_model()
    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    predictions = [round(value) for value in pred]
    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    print(classification_report(y_test, predictions, target_names=target_names))


def get_model():
    #model = xg.XGBClassifier(silent=False,max_depth=6)
    model = SVC(verbose=True,max_iter=500)

    return model



time_data = data[:, 1]
labels=data[:,0]
time_clustering(time_data,labels)
