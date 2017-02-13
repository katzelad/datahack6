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
    
    features.append(xs.min(timestamps))
    features.append(xs.max(timestamps))
    features.append(xs.median(timestamps))
    features.append(xs.mean(timestamps))
    
    features.append(ys.min(timestamps))
    features.append(ys.max(timestamps))
    features.append(ys.median(timestamps))
    features.append(ys.mean(timestamps))
    
    features.append(zs.min(timestamps))
    features.append(zs.max(timestamps))
    features.append(zs.median(timestamps))
    features.append(zs.mean(timestamps))
    
#     features.append(...)
    return features