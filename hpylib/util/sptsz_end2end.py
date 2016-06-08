import numpy as np
from scipy.io.idl import readsav
from sys import exit

def restore_end_save(savfile, ellmin=None, ellmax=None):

    n = readsav(savfile)
    key = n.keys()
    if (len(key) != 1):
        exit(".sav file is not a combined end2end file")

    bands = n[key[0]]['bands'][0]

    if (not ellmin):
        ellmin = bands[0]

    if (not ellmax):
        ellmax = bands[-1]

    num_bands = int(n[key[0]]['num_bands'][0])
    dbs_data = n[key[0]]['dbs_data_combined'][0]
    dbs_sims = n[key[0]]['dbs_sims_combined'][0] # (nsims, nspecs, nbands)

    winminell = int(n[key[0]]['winminell'][0])
    winmaxell = int(n[key[0]]['winmaxell'][0])

    winfunc_data = n[key[0]]['winfunc_data_combined'][0]
    winfunc_sims = n[key[0]]['winfunc_sims_combined'][0]

    cov_sv    = n[key[0]]['cov_sv_combined'][0]
    cov_noise = n[key[0]]['cov_noise_combined'][0]

    d = {'num_bands':num_bands, 'bands':bands, 
         'dbs_data':dbs_data, 'dbs_sims':dbs_sims,
         'winminell':winminell, 'winmaxell':winmaxell,
         'winfunc_data':winfunc_data, 'winfunc_sims':winfunc_sims,
         'cov_sv':cov_sv, 'cov_noise':cov_noise}

    return d

def dls2dbs(dls_theory, winfunc, winminell=0, winmaxell=None):
    dim = np.shape(dls_theory)
    nspecs = dim[0]
    lmax   = dim[1] - 1

    if winmaxell is None:
        winmaxell = lmax

    dim = np.shape(winfunc)
    if dim[0] != nspecs or dim[2] != winmaxell-winminell+1:
        exit("check the dimention of dls_theory and winfunc")

    num_bands = dim[1]

    dbs_theory = np.zeros((nspecs, num_bands))
    for i in np.arange(nspecs):
        dbs_theory[i,:] = np.dot(winfunc[i,:,:], np.transpose(dls_theory[i,winminell:winmaxell+1]))

    return dbs_theory

    
        
    
