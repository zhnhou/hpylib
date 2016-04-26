import numpy as np
import camb
from camb import model, initialpower
import cPickle as pickle

def get_params(path, prefix):
    param_file = path + '/' + prefix + '.txt'
    pname_file = path + '/' + prefix + '.paramnames'

    n = np.genfromtxt(pname_file, dtype='str', usecols=0)
    p = np.loadtxt(param_file, dtype=np.float64)

    num_sample = p.shape[0]
    d = {'num_sample':num_sample}

    ct = 0
    for key in n:
        if key[-1] == '*':
            pnlen = len(key)
            pname = key[0:pnlen-1]
        else:
            pname = key

        d[pname] = p[:,ct+2]
        ct += 1

    return d

def calc_pspec(param, lmax=None, output_root=None, TCMB=2.725):

    num_sample = param['num_sample']

    if lmax is None:
        lmax = 5000

    dl_lensed = np.zeros((lmax+1,4,num_sample))

    clkk_all = np.zeros((lmax+1,num_sample))
    kh_all = np.zeros((400,num_sample))
    pk_all = np.zeros((400,num_sample))

    for i in np.arange(num_sample):
        pars = camb.CAMBparams()
        pars.set_cosmology(H0=param['H0'][i], ombh2=param['omegabh2'][i], omch2=param['omegach2'][i], 
        mnu=param['omeganuh2'][i]*94.30, nnu=param['nnu'][i], YHe=param['yheused'][i],
        tau=param['tau'][i])

        pars.InitPower.set_params(ns=param['ns'][i], As=param['A'][i]*1e-9)
        pars.set_matter_power(redshifts=[0.0], kmax=2.0)
        pars.NonLinear = model.NonLinear_none

        pars.set_for_lmax(lmax, lens_potential_accuracy=1)

        results = camb.get_results(pars)
        powers = results.get_cmb_power_spectra(pars)
        clkk_all[:,i] = results.get_lens_potential_cls(lmax=lmax)[:,0]

        kh, z, pk = results.get_matter_power_spectrum(minkh=1e-6, maxkh=2, npoints=400)

        kh_all[:,i] = kh
        pk_all[:,i] = pk
        dl_lensed[:,:,i] = powers['total'] * TCMB**2

        print i, '/', num_sample

    dl_sample = {'num_sample':num_sample, 'lmax':lmax, 'dl_lensed':dl_lensed, 'cl_lenspoten':clkk_all, 'kh':kh_all, 'pk':pk_all}

    if not (output_root is None):
        pickle.dump(dl_sample, open(output_root+".pkl", "wb"))

    return dl_sample
