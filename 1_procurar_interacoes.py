__author__ = 'lucas'
from multiprocesso_classe import thread_processador

class teste(thread_processador):
    print 'start'
    #arquivo= open('linc_enseml.txt','r')
    def funcao(self,inicio,fim):
        import re
        self.array_temporario=[]
        self.chia_pet_file=open('k562_s3_chia_pet_pol2.bed','r').read()

        for linha in self.arquivo_array[int(inicio):int(fim)]:
            if re.search('chr(\d+|.)\t',linha):
                cromossomo= linha.split()[2]
                start=linha.split()[4]
                end=linha.split()[5]
                name=linha.split()[1]
                #print '->',name
                #print cromossomo,start,end,name
                for top_coordenada in self.chia_pet_file.split('\n'):
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
                                    #self.saida.write(saida_join+'\n')
                                    self.array_temporario.append(saida_join)
                                    print saida_join
                                    break
                            if cromossomo==interaction_b[0]:
                                if int(start)> int(interaction_b[1])and int(start)< int(interaction_b[2]):

                                    saida_join=(cromossomo,start,end,name,'---->','  '.join(interaction_b),'<---->','  '.join(interaction_a),'\n')
                                    saida_join= ' '.join(saida_join)
                                    saida_join=re.sub('\s+','\t',saida_join)
                                    #self.saida.write(saida_join+'\n')
                                    self.array_temporario.append(saida_join)
                                    print saida_join
                                    break
                self.set_saida(self.array_temporario)
                #for escrever in self.array_temporario:
                #    self.saida.write(escrever+'\n')

                        #print interaction_a







teste('linc_enseml.txt',4,'saida_procurar_colocalizacao_lncrna.txt')