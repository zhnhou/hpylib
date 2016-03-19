import numpy as np

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
    
    user, url = info_host(hostname)
    filename
