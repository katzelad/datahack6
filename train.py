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
import  parse
import extract
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from math import sqrt,pow

class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))

print "Loading data..."

# data = parse.parse_data("data/subtrain.csv")
data = parse.parse_data("data/train.csv")


print "Data loaded!"


def get_model():
    model = xg.XGBClassifier(silent=False)
    #model = SVC(verbose=True)
    # model = RandomForestClassifier(n_estimators=100, max_depth=10)
    return model



def train(data):
    seed = 42
    test_size = 0.2
    
    trajs = {}
    for sample in data:
        if sample[C.TRAJ] not in trajs:
            trajs[sample[C.TRAJ]] = (sample[C.LABEL], [])
        trajs[sample[C.TRAJ]][1].append(sample)
    x, y = [], []
    for traj in trajs.itervalues():
        if len(traj[1])>1:
            x.append(extract.traj2features(traj[1]))
            y.append(traj[0])

    x=np.array(x)
    y=np.array(y)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=seed)

    model=get_model()
    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    predictions = map(round, pred)
    
    correct_preds = list(np.array(filter(lambda (p, r): p == r, zip(predictions, y_test)))[:, 0])
    correct_labels = list(y_test)
    accuracy = map(lambda i: float(correct_preds.count(i)) / correct_labels.count(i), range(0, 3))
    for i, acc_val in enumerate(accuracy):
        print i, ': ', acc_val
    print 'score:', min(accuracy)

train(data)