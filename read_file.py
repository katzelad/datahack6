import pickle
with open('C:\data\data.pickle') as f:
    median_1, median_2, median_3, cov_1, cov_2, cov_3, result, paths_size_1, paths_size_2, paths_size_3= pickle.load(f)
x=5