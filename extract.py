import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse

from math import sqrt,pow

class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))
    
def append_stats(traj_features, features):
    features.append(np.min(traj_features))
    features.append(np.max(traj_features))
    features.append(np.median(traj_features))
    features.append(np.mean(traj_features))
    features.append(np.std(traj_features))

def traj2features(samples):
    np_samples = np.array(samples)

    features = []
    
    timestamps = np_samples[:, C.TS]
    xs = np_samples[:, C.X]
    ys = np_samples[:, C.Y]
    zs = np_samples[:, C.Z]

    append_stats(timestamps, features)
    append_stats(xs, features)
    append_stats(ys, features)
    append_stats(zs, features)

    features.append(avg_speed(samples))
    #     features.append(...)
    return features

def avg_speed(samples):
    prev = samples[0]
    sum = 0
    curr={}
    for index in range(len(samples)):
        if (index > 0):
                curr = samples[index]
                distant = np.sqrt(
                   np.power((curr[3] - prev[3]), 2) + np.power((curr[4] - prev[4]), 2) + np.power((curr[5] - prev[5]), 2))
                speed = distant / (curr[1] - prev[1])
                sum = sum + speed
                prev=curr
    return (sum / (len(samples) - 1))


