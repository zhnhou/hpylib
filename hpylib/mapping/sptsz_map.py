import pyfits as pf
import numpy as np

def read_sptsz_fits(fits_file):
    hdulist = pf.open(fits_file)
    data_map = hdulist[3].data['MAP'][0]
    jack_map = hdulist[4].data['MAP'][0]
    weight_map = hdulist[5].data['MAP'][0]

    ra0  = hdulist[2].data['RA0'][0]
    dec0 = hdulist[2].data['DEC0'][0]

    nsidex = hdulist[2].data['NSIDEX'][0]
    nsidey = hdulist[2].data['NSIDEY'][0]

    reso_arcmin = hdulist[2].data['RESO_ARCMIN'][0]

    d = {'ra0':ra0, 'dec0':dec0, 'nsidex':nsidex, 'nsidey':nsidey, 
         'map_data':data_map, 'map_jack':jack_map, 'map_weight':weight_map}

    return d
