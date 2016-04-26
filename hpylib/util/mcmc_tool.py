import numpy as np

def read_cosmoslik_chain_txt(chain_file):
    with open(chain_file, 'r') as f:
        line = f.readline()

    param = line.split()
    txt = np.loadtxt(chain_file, skiprows=1)

    pname_chain = ['weight','lnl','cosmo.ombh2','cosmo.omch2','cosmo.theta','cosmo.ns','cosmo.logA','cosmo.H0','cosmo.Yp','cosmo.tau']
    pname_output = ['weight','loglike','omegabh2','omegach2','theta','ns','logA','H0','Yp','tau']

    num_sample = txt.shape[0]
    num_param = np.shape(pname_chain)[0]

    tmp = np.zeros((num_param, num_sample), dtype=np.float64)

    i = 0
    for pname in pname_chain:
        ip = param.index(pname)
        tmp[i,:] = txt[:,ip]
        i += 1

    d = {'paramname':pname_output, 'chain':tmp, 'num_sample':num_sample, 'num_parameter':num_param}

    return d

def write_cosmoslik_chain_txt(slik_chain, output_prefix):

    num_sample = slik_chain['num_sample']
    num_parameter = slik_chain['num_parameter']
    pname = slik_chain['paramname']

    with open(output_prefix+'.paramnames', 'w') as f:
        for p in pname:
            f.write("%-10s%-10s\n"% (p,p))

    with open(output_prefix+'.txt','w') as f:
        for i in np.arange(0,num_sample):
            for j in np.arange(0,num_parameter):
                f.write("%18.9E"% slik_chain['chain'][j,i])
            f.write("\n")
