import itertools
import operator
import sklearn as sk, numpy as np, scipy as sp, dateutil.parser, time, parse
import matplotlib.pyplot as plt
import pykalman as kalm
import cPickle as pc

class C:
    LABEL, TS, TRAJ, X, Y, Z = tuple(range(0, 6))

def calc_start_end(samples):

    print sample

    np_samples = np.array(samples)
    features = []

    timestamps = np_samples[:, C.TS]
    xs = np_samples[:, C.X]
    ys = np_samples[:, C.Y]
    zs = np_samples[:, C.Z]

    print "calc directions"

    xs_directions = [ (1 if xs[j] < xs[j+1] else -1) for j in range(0, len(xs)-2)]
    ys_directions = [ (1 if ys[j] < ys[j+1] else -1) for j in range(0, len(ys)-2)]
    zs_directions = [ (1 if zs[j] < zs[j+1] else -1) for j in range(0, len(zs)-2)]

    def good_indexes(directions, points) :
        fixed_xs = []
        s = sum(directions)
        fixed_xs.append([])
        for j in range(0, len(directions)-2) :
            if (directions[j] == 1 and s > 0 )or (directions[j] == -1 and s < 0):
                rel_ind = j-1 if (j!=0) else j+2
                if np.abs(points[rel_ind] - points[j]) > np.abs(points[rel_ind] - points[j+1]) :
                    fixed_xs.append(j+1)
                else :
                    fixed_xs.append(j)

        return fixed_xs

    #.intersection(good_indexes(zs_directions)[i])
    good_indexes_total = list(set(good_indexes(xs_directions,xs)).intersection(good_indexes(ys_directions,ys)))

    print "filter good indexes"

    filtered_xs = [xs[i] for i in good_indexes_total]
    filtered_ys = [ys[i] for i in good_indexes_total]
    filtered_zs = [zs[i] for i in good_indexes_total]

    print "compute coefs"
    coef_xz = np.polyfit(filtered_xs, filtered_zs, 2)
    coef_yz = np.polyfit(filtered_ys, filtered_zs, 2)


    def parabola_zeros(coef) :
        a, b, c = coef[0], coef[1], coef[2]
        delta = b**2 - 4*a*c
        return (-b + np.sqrt(delta)) / (2 * a), (-b - np.sqrt(delta)) / (2 * a)

    print "compute parabola"
    (x1,x2) = parabola_zeros(coef_xz)
    (y1,y2) = parabola_zeros(coef_yz)

    #print [sum(ds) for ds in xs_directions]
    #print zip(starting_x, [sum(ds) for ds in xs_directions])

    print "sorting"

    dx = sum(xs_directions)
    dy = sum(ys_directions)
    start_x,end_x = (x1,x2) if dx>0 else (x2,x1)
    start_y, end_y = (y1,y2)if dy>0 else (y2,y1)

    print "storing"

    return start_x, start_y, end_x, end_y


splited = [list(group) for key,group in itertools.groupby(data,operator.itemgetter(C.TRAJ))]
res = [calc_start_end(sample) for sample in splited]

with open('data.pkl', 'wb') as f:
    pc.dump(res,f)
