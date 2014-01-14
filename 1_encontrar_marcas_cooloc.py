__author__ = 'lucas'
import re
''' Encontra marcas de RBP em sequencias que se co-localizam com lncrnas'''
arquivo_coolocalizados=open('saida_procurar_colocalizacao_lncrna.txt','r').read()
arquivo_rbp_mark=open('HeLa_Form.CSAR_PPS_FDR05.bed','r').read()
saida= open('saida_encontrar_marcas_cooloc.txt','w')
for linha in arquivo_coolocalizados.split('\n'):
    if len(linha)>0:

        interacao_final=linha.split('<---->\t')[1]
        interacao_final=interacao_final.split('\t')
        #print interacao_final
        for rbp_mark in arquivo_rbp_mark.split('\n'):
            if len(rbp_mark)>0:
                chr_mark=rbp_mark.split('\t')[0]
                if chr_mark==interacao_final[0]:
                    start_mark=rbp_mark.split('\t')[1]
                    end_mark=rbp_mark.split('\t')[2]
                    if int(interacao_final[1])> int(start_mark) and int(interacao_final[1])< int(end_mark):
                       # print linha.split('\t')[3],chr_mark,int(interacao_final[1]),int(start_mark) ,int(end_mark)
                        saida_formatando= linha.split('\t')[3],chr_mark,(interacao_final[1]),(start_mark),(end_mark)
                        saida_formatando= '\t'.join(saida_formatando)
                        saida.write(saida_formatando+'\n')
                        print (saida_formatando+'\n')
