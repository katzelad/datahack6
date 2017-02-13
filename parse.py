import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time

def str2ts(str):
    return time.mktime(dateutil.parser.parse(str).timetuple())

def parse_row(row):
    row[1] = str2ts(row[1])
    return tuple(map(float, row))

def parse_data(file_name):
    raw_data = np.loadtxt(file_name, dtype='str', delimiter=',', skiprows=1)
    return np.array(map(parse_row, raw_data))