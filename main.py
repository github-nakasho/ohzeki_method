#!/usr/bin/env python3

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
    eta = 0.001
    for _ in range(100):
        print('parameters: ', parameters)
        # solve with OpenJij
        solution, energy, broken = sop.solve_problem(model=model, feed_dict=parameters)
        print('broken: ', broken)
        for i in broken.keys():
            parameters[i] -= eta * broken[i][1]
        obj = 0
        for i in range(instance_data['num_rands']):
            obj += instance_data['rands'][i] * solution.array('x', i)
        print(obj)
        if obj == instance_data['optimal_obj'] and len(broken) == 0:
            break
        
