#!/usr/bin/env python3

import numpy as np


def make_instance():
    # set the number of random numbers
    num_rands = 200
    # set K
    K = 5
    # set random numbers
    rands = np.random.rand(num_rands)
    # optimal solution
    rands_sort = sorted(rands)
    optimal_obj = sum(rands_sort[0:5])
    print('*****')
    print(optimal_obj)
    print('*****')
    return {'num_rands': num_rands, 'K': K, 'rands': rands, 'optimal_obj': optimal_obj}
