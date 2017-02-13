import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse

class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))
    
def append_stats(traj_features, features):
    features.append(np.min(traj_features))
    features.append(np.max(traj_features))
    features.append(np.median(traj_features))
    features.append(np.mean(traj_features))
    features.append(np.std(traj_features))
    features.append(traj_features[len(traj_features)-1]-traj_features[0])

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
    
#     features.append(...)
    return features