import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse

class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))

def traj2features(samples):
    np_samples = np.array(samples)
    features = []
    timestamps = np_samples[:, C.TS]
    features.append(np.min(timestamps))
    features.append(np.max(timestamps))
    features.append(np.median(timestamps))
    features.append(np.mean(timestamps))
#     features.append(...)
    return features