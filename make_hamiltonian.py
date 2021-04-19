#!/usr/bin/env python3

from pyqubo import Array, Constraint, Placeholder


def make_hamiltonian(instance_data):
    # set variables
    num_rands = instance_data['num_rands']
    K = instance_data['K']
    rands = instance_data['rands']
    x = Array.create('x', shape=(num_rands), vartype='BINARY')
    # set hyperparameters
    nu_1 = Placeholder('h_1')
    # set K constraint
    h_1 = sum(x) - K
    h_1 = Constraint(h_1, label='h_1')
    # set objective function
    obj = sum([rands[i]*x[i] for i in range(num_rands)])
    # compute total hamiltonian
    hamiltonian = - nu_1 * h_1 + obj
    # compile
    model = hamiltonian.compile()
    return model
