import numpy as np


def compute_vec_2norm(vec):
    return np.sqrt((vec ** 2).sum(axis=1))


def compute_error(p1, p2):
    return compute_vec_2norm(p1-p2).mean()
