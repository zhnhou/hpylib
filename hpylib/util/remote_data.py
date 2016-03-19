import numpy as np
import os

def info_host(hostname):
    if (str.upper(hostname) is 'MIDWAY'):
        user = 'zhenhou'
        url  = 'midway.rcc.uchicago.edu'
    else if (str.upper(hostname) is 'CORI'):
        user = 'hou'
        url  = 'cori.nersc.gov'
    else if (str.upper(hostname) is 'EDISON'):
        user = 'hou'
        url  = 'edison.nersc.gov'
    else if (str.upper(hostname) is 'SPT'):
        user = 'hou'
        url  = 'spt.uchicago.edu'
    else if (str.upper(hostname) is 'CLOUD'):
        user = 'hou'
        url  = 'sptcloud.uchicago.edu'
    else:
        print "hmm, maybe I am thinking of AWS?"
        exit()

    return user, url


def sync_from_remote(hostname, filename):

    # filename is the file name including the absolute path on remote machine
    
    user, url = info_host(hostname)
    dat_pastr = '/data_'+str.lower(hostname)+'/'
    sub_index = filename.find(dat_pastr)

    filename_local = '~/data_local/'+filename[sub_index+len(dat_pastr):]
    path_index = filename_local.rfind('/')
    path_local = filename_local[0:path_index]

    if not os.path.exists(path_local):
        os.makedirs(path_local)

    os.system("scp "+user+"@"+url+":"+filename+" "+filename_local)
