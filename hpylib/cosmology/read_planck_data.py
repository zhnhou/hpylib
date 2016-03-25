import pyfits as pf
import numpy as np

import camb
from camb import model, initialpower

def set_planck_cambparams(base=True, lmax=5000):
    pars = camb.CAMBparams()

    omegabh2 = 0.02226e0
    omegach2 = 0.1186e0
    H0 = 67.81
    mnu = 0.06
    tau = 0.0660e0
    ns = 0.9677
    logA = 3.0620e0

    omegak = 0.00
    neff   = 3.046
    nrun   = 0.00
    r      = 0.00
    w      = -1.00e0

    pars.set_cosmology(ombh2=omegabh2, omch2=omegach2, H0=H0, mnu=mnu, nnu=neff, tau=tau)
    pars.InitPower.set_params(ns=ns, As=np.exp(logA)*1e-10)
    pars.set_for_lmax(lmax, lens_potential_accuracy=1, max_eta_k=4*lmax)

    return pars

"""
This function will read the public Planck power spectrum
in the officially released fits file 'COM_PowerSpect_CMB_R2.02.fits'
Header index, data type
 1, low-ell  CMB TT (unbinned)
 2, low-ell  CMB TE (unbinned)
 3, low-ell  CMB EE (unbinned)
 4, low-ell  CMB TB (unbinned)
 5, low-ell  CMB EB (unbinned)
 6, low-ell  CMB BB (unbinned)
 7, high-ell CMB TT (binned)
 8, high-ell CMB TT (unbinned)
 9, high-ell CMB TE (binned)
10, high-ell CMB TE (unbinned)
11, high-ell CMB EE (binned)
12, high-ell CMB EE (unbinned)
"""

def read_planck_pspec_fits(fitsfile):
    hdulist = pf.open(fitsfile)
    lowl_TT_bands = hdulist[1].data['ell']
    lowl_TT_dbs   = hdulist[1].data['d_ell']
    lowl_TT_errup = hdulist[1].data['errup']
    lowl_TT_errdown = hdulist[1].data['errdown']

    highl_TT_bands = hdulist[7].data['ell']
    highl_TT_dbs   = hdulist[7].data['d_ell']
    highl_TT_err   = hdulist[7].data['err']

    d = {'lowl_TT_bands':lowl_TT_bands, 'lowl_TT_dbs':lowl_TT_dbs, 
         'lowl_TT_errup':lowl_TT_errup, 'lowl_TT_errdown':lowl_TT_errdown,
         'highl_TT_bands':highl_TT_bands, 'highl_TT_dbs':highl_TT_dbs, 'highl_TT_err':highl_TT_err}

    return d


