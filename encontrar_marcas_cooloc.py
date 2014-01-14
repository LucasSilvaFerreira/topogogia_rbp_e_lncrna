__author__ = 'lucas'
''' Encontra marcas de RBP em sequencias que se co-localizam com lncrnas'''
arquivo_coolocalizados=open('saida_procurar_colocalizacao_lncrna.txt','r').read()
for linha in arquivo_coolocalizados.split('\n'):
    if len(linha)>0:
        print linha