__author__ = 'lucas'
from multiprocesso_classe import  thread_processador
class Procurar_cromatina(thread_processador):
    def funcao(self, inicio, fim):#teste
        self.array_temporario = []
        '''sobrescreva esse metodos'''
        self.arquivo_para_cruzar = open('k562_s3_chia_pet_pol2.bed', 'r').read()
        print 'esse metodo deve ser sobrescrito com os parametros presentes nesse arquivo dentro da classe'
        for array_linha in self.arquivo_array[int(inicio):int(fim)]:
            print array_linha
        for escrever in self.array_temporario: #isso deve ser executado apenas no final da funcao
            self.saida.write(escrever + '\n')

Procurar_cromatina('saida_procurar_colocalizacao_lncrna.txt',3,'saida_cromatina_hmm_estados.txt')

