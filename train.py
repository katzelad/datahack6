import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.cluster import DBSCAN
from sklearn import metrics
import matplotlib.pyplot as plt
import parse
import extract
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier


class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))


print "Loading data..."

# data = parse.parse_data("data/subtrain.csv")
data = parse.parse_data(r"C:\Users\Nofar\Desktop\hack\train.csv")

print "Data loaded!"


def get_model():
    # model = xg.XGBClassifier(silent=False,max_depth=6)
    # model = SVC(verbose=True)
    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    return model

def calc_path():
    data_calc = parse_data()
    path_size = 1
    time_stamp = data_calc[0,1]
    result = []
    print len(data_calc)
    for index in range(len(data_calc)):
        if np.abs(data_calc[index,1] - time_stamp) < 60000*0.5:
            path_size += 1
        else:
            for i in range(path_size) :
                result.append(path_size)
            if path_size == 0:
                result.append(0)
            path_size=1
            time_stamp = data_calc[index, 1]
    result.append(path_size)

    print len(result)
    return result

def parse_data():
    new_data = np.empty_like(data)
    indexNew = 0
    index = data[0,2]
    new_data[indexNew] = data[0]
    for indexRow in range(len(data)):
        if data[indexRow, 2] != index:
            indexNew+=1
            new_data[indexNew] = data[indexRow]
            index = data[indexRow, 2]

    indexNew+=1
    new_data = np.delete(new_data, np.s_[indexNew::], 0)
    print len(new_data)
    return new_data


def train(data):
    seed = 42
    test_size = 0.2

    trajs = {}
    for sample in data:
        if sample[C.TRAJ] not in trajs:
            trajs[sample[C.TRAJ]] = (sample[C.LABEL], [])
        trajs[sample[C.TRAJ]][1].append(sample)
    x, y = [], []
    extract.count_feature = calc_path()
    print len(trajs)
    print len(extract.count_feature)
    for traj in trajs.itervalues():
        x.append(extract.traj2features(traj[1]))
        y.append(traj[0])

    x = np.array(x)
    y = np.array(y)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=seed)

    model = get_model()
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