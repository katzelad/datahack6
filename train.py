import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse, extract
# import xgboost as xg

from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier


class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))

    
data = parse.parse_data("data/train.csv")


def train(data):
    seed = 7
    test_size = 0.2
    
    trajs = {}
    for sample in data:
        if sample[C.TRAJ] not in trajs:
            trajs[sample[C.TRAJ]] = (sample[C.LABEL], [])
        trajs[sample[C.TRAJ]][1].append(sample)
    x, y = [], []
    for traj in trajs.itervalues():
        x.append(extract.traj2features(traj[1]))
        y.append(traj[0])
    
#     X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    x_train, x_test = x[:int(len(x) * test_size)], x[int(len(x) * test_size):]
    y_train, y_test = y[:int(len(x) * test_size)], y[int(len(x) * test_size):]

#     model = xg.XGBClassifier()
#     model = svm.SVC(kernel='rbf', max_iter=1000)
    model = RandomForestClassifier(n_estimators=200, max_depth=12)
    model.fit(x_train, y_train)

    pred = model.predict(x_test)

    predictions = map(round, pred)
    
    correct_preds = list(np.array(filter(lambda (p, r): p == r, zip(predictions, y_test)))[:, 0])
    correct_labels = list(y_test)
    accuracy = map(lambda i: float(correct_preds.count(i)) / correct_labels.count(i), range(0, 3))
    for i, acc_val in enumerate(accuracy):
        print i, ': ', acc_val
    print 'score:', min(accuracy)


train(data)
