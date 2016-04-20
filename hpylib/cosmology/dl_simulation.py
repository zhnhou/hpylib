import numpy as np

def read_dl_simulation(path, prefix, nsims, suffix=None, file_ext='txt'):

    if suffix is None:
        suf = ''
    else
        suf = '_'+suffix

    for i in np.arange(0,nsims):
        filename = path+'/'+prefix+'_sim_'+str(i)+suf+'.'+file_ext
        tmp = np.loadtxt(filename, usecols=[1])

        if i == 0:
            lmax = np.shape(tmp)[0] - 1
            dl_all = np.zeros(lmax+1,nsims)

        dl_all[:,i] = tmp[:]

    dl_ave = np.mean(dl_all, axis=1)

    return dl_all, dl_ave
