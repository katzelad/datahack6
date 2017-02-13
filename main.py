from numpy import genfromtxt
import numpy as np
my_data = genfromtxt(r'C:\data\train.csv', delimiter=',')
index = my_data[0][3]
for row in my_data:
    if row[3] == index:
        np.delete(my_data,row)
    else: index = row[3]