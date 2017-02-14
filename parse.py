import sklearn as sk, numpy as np
import datetime

def str2ts(str):
    try:
        dt = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S.%f')
    except:
        dt=datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds()


def parse_row(row):
    row[1] = str2ts(row[1])
    return tuple(map(float, row))

def parse_test_row(row):
    row[0] = str2ts(row[0])
    return tuple(map(float, row))

def parse_data(file_name):
    raw_data = np.loadtxt(file_name, dtype='str', delimiter=',', skiprows=1)
    return np.array(map(parse_row, raw_data))

def parse_test(file_name):
    raw_data = np.loadtxt(file_name, dtype='str', delimiter=',', skiprows=1)
    return np.array(map(parse_test_row, raw_data))