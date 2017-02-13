import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse

class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))

count_feature = []
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
    features.append(timestamps[len(timestamps) - 1] - timestamps[0])
    features.append(len(timestamps))
    append_stats(xs, features)
    append_stats(ys, features)
    append_stats(zs, features)

#     features.append(...)
    features.append(count_feature[int(samples[0][C.TRAJ])])
    return features