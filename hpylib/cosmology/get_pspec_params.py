import numpy as np

def get_params(path, prefix):
    param_file = path + '/' + prefix + '.txt'
    pname_file = path + '/' + prefix + '.paramnames'

    n = np.genfromtxt(pname_file, dtype='str', usecols=0)
    p = np.loadtxt(param_file, dtype=np.float64)

    d = {}

    ct = 0
    for key in n:
        d[key] = p[ct+2]
        p += 1

