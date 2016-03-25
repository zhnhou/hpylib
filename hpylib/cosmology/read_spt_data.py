import numpy as np

def read_spt_bandpower(path):

    bandpower_file = path+'/bandpower.txt'
    tmp = np.loadtxt(bandpower_file, usecols=[1,2,3,4], dtype=np.float64)

    dbs = tmp[:,0]
    err = tmp[:,1]
    band = (tmp[:,2]+tmp[:,3]) * 0.5

    num_band = np.shape(dbs)

    dbs_fgsub = np.zeros(num_band)

    nm_sz = 5.5
    nm_ps = 19.3
    nm_cl = 5.0

    dls_sz = np.loadtxt(path+'/fg/dl_shaw_tsz_s10_153ghz.txt', dtype=np.float64, usecols=1)
    dls_ps = np.loadtxt(path+'/fg/dl_poisson_point_source.txt', dtype=np.float64, usecols=1)
    dls_cl = np.loadtxt(path+'/fg/dl_0p8', dtype=np.float64, usecols=1)
    
    tmp = np.loadtxt(path+'windows/window_1', dtype=np.float64)
    winminell = int(tmp[0,0])
    winmaxell = int(tmp[num_band-1,0])

    dls_fg = dls_sz[winminell:winmaxell]*nm_sz + dls_ps[winminell:winmaxell]*nm_ps + dls_cl[winminell:winmaxell]*nm_cl
    
    winfunc = np.zeros(winmaxell-winminell+1,num_band)
    for i in np.arange(num_band):
        tmp = np.loadtxt(path+'windows/window_'+str(i+1), dtype=np.float64, usecols=1)
        winfunc[:,i] = tmp
        dbs_fgsub[i] = dbs[i] - sum(winfunc[:,i]*dls_fg)


    d = {'num_band':num_band, 'band':band, 'dbs':dbs, 'err':err, 'dbs_fgsub',dbs_fgsub}

    return d
