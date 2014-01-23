__author__ = 'lucas'
import multiprocessing
from multiprocessing import Manager
class thread_processador:
    from itertools import count

    '''A funcao principal devera sobrescrita utilizando o seu codigo desejado com ao menos 2 metodos de entrada um para o fim outro para o inicio da tabela'''
    def __init__(self,file,n_process,saida_nome):
        __author__ = 'lucas'
        import thread,time

        '''script generico para fazer uma tread em um arquivo com varias entradas'''
        self.jobs=[]
        self.numero_threads= n_process
        self.arquivo_escolhido= file
        self.saida_nome=saida_nome
        self.manager= Manager()
        self.saida_unica=self.manager.list()
        
        #abrindo o arquivo desejado
        arquivo = open(self.arquivo_escolhido,'r').read() #sempre mude para seu arquivo
        #salvando o arquivo desejado
        self.saida = open(self.saida_nome,'w') #sempre mude para seu arquivo de saida
        #guardando o arquivo em um array para que seja feita a divisao
        self.arquivo_array=[]


        for arquivo_linha in arquivo.split('\n'):
            if len(arquivo_linha)>0:
                self.arquivo_array.append(arquivo_linha)
        tamanho_threads= len(self.arquivo_array)
       # print tamanho_threads
        range_threads= len(self.arquivo_array)/self.numero_threads
        #
        for thread_numero in range (0,self.numero_threads):
           # print thread_numero*range_threads,thread_numero*range_threads+range_threads-1 #estou perdendo o ultimo valor da tabela
            inicio_valor=thread_numero*range_threads
            fim_valor=thread_numero*range_threads+range_threads-1
           # print inicio_valor,fim_valor
            print "Thread "+ str(thread_numero) + "SUCCESSFULLY CREATED"
            p = multiprocessing.Process(target=self.funcao, args=(inicio_valor,fim_valor))
            #p.start()
            #p.join()
            
            self.jobs.append(p)
            p.start()
        for processos in self.jobs:
            processos.join()
        print 'final',len(self.saida_unica)
        for i in range(len(self.saida_unica)):
            for linha_i in self.saida_unica[i]:
                self.saida.write(linha_i+'\n')
        #for salvando in self.saida_unica:
        #    self.saida.write(salvando+'\n')
        #while True:
        #    for
        #    print len(self.jobs)
    def set_saida(self,array_para_entrar):
        #print 'setando'
        self.saida_unica.append(array_para_entrar)
        #print 'teste',len(self.saida_unica)
    def funcao(self,inicio,fim):#teste
        self.array_temporario=[]
        '''sobrescreva esse metodos'''
        self.arquivo_para_cruzar=open('arquivo_para_abrir','r').read()
        print 'esse metodo deve ser sobrescrito com os parametros presentes nesse arquivo dentro da classe'
        for array_linha in self.arquivo_array[int(inicio):int(fim)]:
            print array_linha
        for escrever in self.array_temporario: #isso deve ser executado apenas no final da funcao
            self.saida.write(escrever+'\n')

    #def salvar(self):
     #   print len(self.saida_unica),'<---saida unica'
