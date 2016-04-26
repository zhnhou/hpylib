import numpy as np
import os

def gc_googlescholar_citation_pdf(prefix, path='/Users/zhenhou/GoogleDrive/Family/greencard/documents/citations_google_scholar'):
    file_path = path+'/'+prefix+'/'

    os.chdir(file_path)
    i = 1
    command = 'pdfunite '+prefix+'.pdf'
    while (os.isfile('c'+str(i)+'.pdf')):
        command += ' c'+str(i)+'.pdf'
        i += 1

    command += ' all.pdf'
