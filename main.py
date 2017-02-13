import numpy as np
import parse
import pickle

def calc_path():
    data = parse_data();
    path_size = 0
    label = data[0,0]
    time_stamp = data[0,1]
    result = np.empty([3,2])*0
    paths_size_1 = []
    paths_size_2 = []
    paths_size_3 = []
    for index in range(len(data)):
        if np.abs(data[index,1]-time_stamp)<60000*0.5:
            path_size += 1
        else:
            result[label,0] += path_size
            result[label, 1] += 1
            if label == 0:
                paths_size_1.append(path_size)
            if label == 1:
                paths_size_2.append(path_size)
            if label == 2:
                paths_size_3.append(path_size)
            path_size=0
            label = data[index,0]
            time_stamp = data[index, 1]
    print result
    median_1 = np.median(paths_size_1)
    median_2 = np.median(paths_size_2)
    median_3 = np.median(paths_size_3)

    cov_1 = np.cov(paths_size_1)
    cov_2 = np.cov(paths_size_2)
    cov_3 = np.cov(paths_size_3)
    print median_1 , median_2 ,median_3 , cov_1 , cov_2 , cov_3

    with open('C:\data\data.pickle', 'w') as f:
        pickle.dump([median_1, median_2, median_3,cov_1,cov_2,cov_3,result,paths_size_1,paths_size_2,paths_size_3], f)

def parse_data():
    data = parse.parse_data(r'C:\data\train.csv')
    new_data = np.empty_like(data)
    indexNew = 0
    index = data[0,2]
    new_data[indexNew] = data[0]
    for indexRow in range(len(data)):
        if data[indexRow, 2] != index:
            indexNew+=1
            new_data[indexNew] = data[indexRow]
            index = data[indexRow, 2]

    # indexNew+=1
    new_data = np.delete(new_data, np.s_[indexNew::], 0)
    return new_data


new_data = calc_path()