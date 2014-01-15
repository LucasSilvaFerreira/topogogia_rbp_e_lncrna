__author__ = 'lucas'
arquivo=open('refseq.txt','r').read()
for linha in arquivo.split('\n'):
    print linha