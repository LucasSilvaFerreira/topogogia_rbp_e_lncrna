__author__ = 'lucas'
from multiprocesso_classe import thread_processador
class ensembl_procura(thread_processador):
    #chr21	38580803	38592892	TCONS_00028773	---->	chr21	38580547	38582227	<---->	chr21	38738473	38740592		1_Active_Promoter|6_Weak_Enhancer|1_Active_Promoter

    def funcao(self, inicio, fim):#teste
        self.array_temporario = []
        '''sobrescreva esse metodos'''
        self.arquivo_para_cruzar = open('Ensembl.txt', 'r').read()
        #print 'esse metodo deve ser sobrescrito com os parametros presentes nesse arquivo dentro da classe'
        for array_linha in self.arquivo_array[int(inicio):int(fim)]:
            process_array_linha=array_linha.split('\t')
            #pair_name=gene_chr=process_array_linha[]
            pair_chr=process_array_linha[9]
            pair_start=process_array_linha[10]
            pair_end=gene_chr=process_array_linha[11]
            for ensembl in self.arquivo_para_cruzar.split('\n'):
                if len(ensembl)>0:
                    if pair_chr == ensembl.split('\t')[2]:
                        '''essa parte de bater apenas no start deve ser revista'''
                        if int(pair_start)> int(ensembl.split('\t')[4]) and int(pair_start)< int(ensembl.split('\t')[5]):
                            #print ensembl.split('\t')[1]
                            #self.array_temporario.append(array_linha+'\t'+ensembl.split('\t')[1]+'\t'+ensembl.split('\t')[3])
                            print(array_linha+'\t'+pair_chr+':'+pair_start+'-'+pair_end+'\t'+ensembl.split('\t')[1]+'\t'+ensembl.split('\t')[3])
                            self.array_temporario.append(array_linha+'\t'+pair_chr+':'+pair_start+'-'+pair_end+'\t'+ensembl.split('\t')[1]+'\t'+ensembl.split('\t')[3])

                            break
                        if int(pair_end)> int(ensembl.split('\t')[4]) and int(pair_end)< int(ensembl.split('\t')[5]):
                            print(array_linha+'\t'+pair_chr+':'+pair_start+'-'+pair_end+'\t'+ensembl.split('\t')[1]+'\t'+ensembl.split('\t')[3])
                            self.array_temporario.append(array_linha+'\t'+pair_chr+':'+pair_start+'-'+pair_end+'\t'+ensembl.split('\t')[1]+'\t'+ensembl.split('\t')[3])

                            break
                   # print ensembl
            #print array_linha
        for escrever in self.array_temporario: #isso deve ser executado apenas no final da funcao
            print escrever
            self.saida.write(escrever + '\n')


ensembl_procura('saida_cromatina_hmm_uniq_estados.txt',2,'saida_ensembl.txt')