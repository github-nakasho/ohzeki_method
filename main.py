#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

import make_hamiltonian as mh
import make_instance as mi
import solve_problem as sop


if __name__ == '__main__':
    # set instance info.
    print('Make instance data')
    instance_data = mi.make_instance()
    print('Finish making instance data')
    # set costs & constraints
    print('Make hamiltonian & model')
    model = mh.make_hamiltonian(instance_data=instance_data)
    print('Finish making hamiltonian & model')
    # set hyperparameters
    parameters = {'h_1': 0.0}
    eta = 1 / instance_data['num_rands']
    res_list = []
    nu_list = []
    for _ in range(100):
        print('parameters: ', parameters)
        nu_list.append(parameters['h_1'])
        # solve with OpenJij
        solution, energy, broken = sop.solve_problem(model=model, feed_dict=parameters)
        print('broken: ', broken)
        for i in broken.keys():
            parameters[i] -= eta * broken[i][1]
        obj = 0
        for i in range(instance_data['num_rands']):
            obj += instance_data['rands'][i] * solution.array('x', i)
        print(obj)
        res = np.abs(obj-instance_data['optimal_obj'])
        res_list.append(res)
        if obj == instance_data['optimal_obj'] and len(broken) == 0:
            break
    plt.plot(res_list)
    plt.xlabel('Step')
    plt.ylabel('Difference in objective function')
    plt.show()
    plt.plot(nu_list)
    plt.xlabel('Step')
    plt.ylabel('Multiplier')
    plt.show()
    
