import numpy as np
import os

def gc_googlescholar_citation_pdf(prefix, path='/Users/zhenhou/GoogleDrive/Family/greencard/documents/citations_google_scholar'):
    file_path = path+'/'+prefix+'/'
    if (os.path.isdir(file_path)):
        os.chdir(file_path)
    else:
        print prefix+' is not a directory. skip'
        return -1

    if (not os.path.isfile(prefix+'.pdf')):
        print prefix+' no head pdf file. skip'
        return -2

    i = 1
    command = 'pdfunite '+prefix+'.pdf'
    while (os.path.isfile('c'+str(i)+'.pdf')):
        command += ' c'+str(i)+'.pdf'
        i += 1

    command += ' '+prefix+'_merged.pdf'
    os.system(command)

    return 0

def gc_googlescholar_merge_citation(path='/Users/zhenhou/GoogleDrive/Family/greencard/documents/citations_google_scholar'):
    command = 'pdfunite '

    for prefix in os.listdir(path):
        if (gc_googlescholar_citation_pdf(prefix) == 0):
            if prefix != 'Planck_2013_XVI':
                command += ' '+prefix+'/'+prefix+'_merged.pdf'

    command += ' citation_merged.pdf'

    os.chdir(path)
    os.system(command)
