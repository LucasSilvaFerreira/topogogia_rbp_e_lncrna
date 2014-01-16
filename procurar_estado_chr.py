__author__ = 'lucas'
'''procura marcas de cromatina'''
from multiprocesso_classe import  thread_processador
class Procurar_cromatina(thread_processador):
    def funcao(self, inicio, fim):#teste
        self.array_temporario = []

        #print 'esse metodo deve ser sobrescrito com os parametros presentes nesse arquivo dentro da classe'
        for array_linha in self.arquivo_array[int(inicio):int(fim)]:
            self.arquivo_para_cruzar = open('wgEncodeBroadHmmK562HMM.bed', 'r')
            chr_int=array_linha.split('\t')[9]
            start_int=array_linha.split('\t')[10]
            stop_int=array_linha.split('\t')[11]
            print chr_int+':'+start_int+'-'+stop_int
            for estado_procurar in self.arquivo_para_cruzar:
                if len(estado_procurar)>0:
                    #print estado_procurar
                    chr_hmm=estado_procurar.split('\t')[0]
                    if chr_int == chr_hmm:
                        if int(start_int) >= int(estado_procurar.split('\t')[1]) and int(start_int) <= int(estado_procurar.split('\t')[2]):
                            estados_saida=estado_procurar.split('\t')[3]


                            proximo = self.arquivo_para_cruzar.next().split('\t')

                            while int(proximo[1]) <= int(stop_int): #inicio do proximo
                                #print proximo
                                estados_saida= estados_saida+ '|'+ proximo[3]
                                proximo = self.arquivo_para_cruzar.next().split('\t')
                            print estados_saida
                            print array_linha+'\t'+estados_saida
                            self.array_temporario.append(array_linha+'\t'+estados_saida)
                            break
            self.arquivo_para_cruzar.close()

        for escrever in self.array_temporario: #isso deve ser executado apenas no final da funcao
            print escrever
            self.saida.write(escrever + '\n')
        print 'concluded'



Procurar_cromatina('saida_procurar_colocalizacao_lncrna.txt',1,'saida_cromatina_hmm_estados.txt')

