__author__ = 'lucas'
from multiprocesso_classe import thread_processador
class atribuindo_nomes(thread_processador):
    def funcao(self, inicio, fim):#teste
        import re
        self.contador=0
        self.array_temporario = []
        self.arquivo_para_cruzar = open('final_TSS-Cufflinks-0.9.3-GENCODE-v3c-K562-rep1.gtf', 'r').read()
        #print 'esse metodo deve ser sobrescrito com os parametros presentes nesse arquivo dentro da classe'
        for array_linha in self.arquivo_array[int(inicio):int(fim)]:
            try:
                ensb_query= array_linha.split('\t')[15]
                for linha in self.arquivo_para_cruzar.split('\n'):
                    if len(linha)>0:
                        gene_id = linha.split('transcript_id')[1].split(';')[0]
                        if re.search(ensb_query,gene_id):
                            #print ensb_query,gene_id
                           # print re.sub('\"|\;','',linha.split('\t')[8].split('FPKM')[1])
                            self.array_temporario.append(array_linha+'\t'+re.sub('\"|\;','',linha.split('\t')[8].split('FPKM')[1]))
                            #print array_linha+'\t'+re.sub('\"|\;','',linha.split('\t')[8].split('FPKM')[1])
                           #print len(self.array_temporario)
                            self.contador+=1
                            break
            except:
               # print array_linha
                pass
        print self.contador
        #print self.array_temporario
        self.set_saida(self.array_temporario)
        #for escrever in self.array_temporario: #isso deve ser executado apenas no final da funcao
        #    self.saida_unica.append(escrever + '\n')
atribuindo_nomes('saida_ensembl.txt',4,'saida_fpkm_ensembl.txt')

