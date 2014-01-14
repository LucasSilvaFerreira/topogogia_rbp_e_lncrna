__author__ = 'lucas'
import re
'''vou iniciar usando so o cromossomo 1 '''
chia_pet_file=open('hela_s3_chia_pet_pol2.bed','r').read()
arquivo= open('lncipedia.bed.txt','r')
saida=open('saida_procurar_colocalizacao_lncrna.txt','w')
for linha in arquivo:
    if re.search('chr(\d+|.)\t',linha):
        cromossomo= linha.split()[0]
        start=linha.split()[1]
        end=linha.split()[2]
        name=linha.split()[3]
        #print '->',name
        #print cromossomo,start,end,name
        for top_coordenada in chia_pet_file.split('\n'):
            if len(top_coordenada)!=0:
                processando_interacores=top_coordenada.split('\t')[3].split(',')[0].split('-')

                interaction_a= re.sub('\.\.|:','\t',processando_interacores[0]).split('\t')
                interaction_b= re.sub('\.\.|:','\t',processando_interacores[1]).split('\t')
                if cromossomo==interaction_a[0] or cromossomo==interaction_a[1]:
                    if cromossomo==interaction_a[0]:
                        if int(start)> int(interaction_a[1])and int(start)< int(interaction_a[2]):
                            saida_join=cromossomo,start,end,name,'---->','  '.join(interaction_a),'<---->','    '.join(interaction_b),'\n'
                            saida_join= ' '.join(saida_join)
                            saida_join=re.sub('\s+','\t',saida_join)
                            saida.write (saida_join+'\n')
                            print saida_join
                            #print (cromossomo,start,end,name,'---->',interaction_a,'<---->',interaction_b)
                    if cromossomo==interaction_b[0]:
                        if int(start)> int(interaction_b[1])and int(start)< int(interaction_b[2]):

                            saida_join=(cromossomo,start,end,name,'---->','  '.join(interaction_b),'<---->','  '.join(interaction_a),'\n')
                            saida_join= ' '.join(saida_join)
                            saida_join=re.sub('\s+','\t',saida_join)
                            saida.write (saida_join+'\n')
                            #print cromossomo,start,end,name,'---->',interaction_b,'<---->',interaction_a print saida_join
                            print saida_join

                #print interaction_a



