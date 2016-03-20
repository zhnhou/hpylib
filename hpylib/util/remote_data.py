import numpy as np
import os
from sys import exit

def info_host(hostname):
    if (str.upper(hostname) == 'MIDWAY'):
        user = 'zhenhou'
        url  = 'midway.rcc.uchicago.edu'
    elif (str.upper(hostname) == 'CORI'):
        user = 'hou'
        url  = 'cori.nersc.gov'
    elif (str.upper(hostname) == 'EDISON'):
        user = 'hou'
        url  = 'edison.nersc.gov'
    elif (str.upper(hostname) == 'SPT'):
        user = 'hou'
        url  = 'spt.uchicago.edu'
    elif (str.upper(hostname) == 'CLOUD'):
        user = 'hou'
        url  = 'sptcloud.uchicago.edu'
    else:
        print "hmm, maybe I am thinking of AWS?"
        exit()

    return [user, url]


def sync_from_remote(hostname, filename):

    # filename is the file name including the absolute path on remote machine

    home_path = os.getenv('HOME')+'/'
    user, url = info_host(hostname)
    dat_pastr = '/data_'+str.lower(hostname)+'/'
    sub_index = filename.find(dat_pastr)

    filename_local = home_path+'data_local/'+filename[sub_index+len(dat_pastr):]

    if os.path.isfile(filename_local):
        return filename_local

    path_index = filename_local.rfind('/')
    path_local = filename_local[0:path_index]

    if not os.path.exists(path_local):
        os.makedirs(path_local)

    os.system("scp "+user+"@"+url+":"+filename+" "+filename_local)
    return filename_local
