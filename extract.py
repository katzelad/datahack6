import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse

class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))

def traj2features(samples):
    np_samples = np.array(samples)
    features = []
    
    timestamps = np_samples[:, C.TS]
    xs = np_samples[:, C.X]
    ys = np_samples[:, C.Y]
    zs = np_samples[:, C.Z]
    
    features.append(np.min(timestamps))
    features.append(np.max(timestamps))
    features.append(np.median(timestamps))
    features.append(np.mean(timestamps))
    
    features.append(np.min(xs))
    features.append(np.max(xs))
    features.append(np.median(xs))
    features.append(np.mean(xs))
    
    features.append(np.min(ys))
    features.append(np.max(ys))
    features.append(np.median(ys))
    features.append(np.mean(ys))
    
    features.append(np.min(zs))
    features.append(np.max(zs))
    features.append(np.median(zs))
    features.append(np.mean(zs))
    
#     features.append(...)
    return features