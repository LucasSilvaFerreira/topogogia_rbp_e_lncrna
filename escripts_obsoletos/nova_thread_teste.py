__author__ = 'lucas'
import threading

class print_out(threading.Thread):

    def __init__ (self, arquivo,numero_threads):
        threading.Thread.__init__(self)
        self.arquivo = arquivo
        self.threads = []
        self.array_dados=[]
        self.numero_threads=numero_threads
        for arquivo_linha in self.arquivo.split('\n'):
            if len(arquivo_linha)>0:
                self.array_dados.append(arquivo_linha)
        tamanho_threads= len(self.array_dados)
        print tamanho_threads
        self.range_threads= len(self.array_dados)/self.numero_threads
        #
        #for thread_numero in range (0,self.numero_threads):
        #    print thread_numero*range_threads,thread_numero*range_threads+range_threads-1 #estou perdendo o ultimo valor da tabela
        #    inicio_valor=thread_numero*range_threads
        #    fim_valor=thread_numero*range_threads+range_threads-1
        #    print inicio_valor,fim_valor


    def run(self):
        print self.m1
        print "\n"


    def iniciando(self,n_treads,inicio,fim):
        for num in range(0, n_treads-1):
            thread = print_out('a', 'b')
            thread.start()
            self.threads.append(thread)

        for thread in self.threads:
            thread.join()