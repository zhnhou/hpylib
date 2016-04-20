import numpy as np

def read_dl_simulation(path, prefix, nsims, suffix=None, file_ext='txt', has_pol=False):

    if suffix is None:
        suf = ''
    else:
        suf = '_'+suffix

    for i in np.arange(0,nsims):
        filename = path+'/'+prefix+'_sim_'+str(i)+suf+'.'+file_ext
        if has_pol:
            tmp = np.loadtxt(filename, usecols=[1,2,3,4], dtype=np.float64)
        else:
            tmp = np.loadtxt(filename, usecols=[1], dtype=np.float64)

        if i == 0:
            lmax = np.shape(tmp)[0] - 1
            if has_pol:
                dl_all = np.zeros((nsims,lmax+1,4), dtype=np.float64)
            else:
                dl_all = np.zeros((nsims,lmax+1), dtype=np.float64)
                
    if has_pol:
        dl_all[i,:,:] = tmp[:,:]
    else:
        dl_all[i,:] = tmp[:]

    dl_ave = np.mean(dl_all, axis=0)

    return dl_all, dl_ave
