class thread_processador:
    from itertools import count
    '''A funcao principal devera sobrescrita utilizando o seu codigo desejado com ao menos 2 metodos de entrada um para o fim outro para o inicio da tabela'''
    def __init__(self,file,n_process,saida_nome):
        __author__ = 'lucas'
        '''script generico para fazer uma tread em um arquivo com varias entradas'''
        import thread
        self.numero_threads= n_process
        self.arquivo_escolhido= file
        self.saida_nome=saida_nome

        #abrindo o arquivo desejado
        arquivo = open(self.arquivo_escolhido,'r').read() #sempre mude para seu arquivo
        #salvando o arquivo desejado
        saida = open(self.saida_nome,'w') #sempre mude para seu arquivo de saida
        #guardando o arquivo em um array para que seja feita a divisao
        arquivo_array=[]
        for arquivo_linha in arquivo.split('\n'):
            if len(arquivo_linha)>0:
                arquivo_array.append(arquivo_linha)
        tamanho_threads= len(arquivo_array)
        print tamanho_threads
        range_threads= len(arquivo_array)/self.numero_threads
        #
        for thread_numero in range (0,self.numero_threads):
            print thread_numero*range_threads,thread_numero*range_threads+range_threads-1 #estou perdendo o ultimo valor da tabela
            inicio=thread_numero*range_threads
            fim=thread_numero*range_threads+range_threads-1
            try:
                thread.start_new_thread(funcao_principal, (inicio,fim) )
                print "Thread "+ thread_numero +" SUCCESSFULLY CREATED"
            except:
                print "Error: unable to start thread"
    def funcao(inicio,fim):

        pass:





        #def funcao(a,b):
        #    for teste in range(1,10000000):
        #        print str(teste)+a


        # Create two threads as follows
        #try:
        #    thread.start_new_thread( funcao, ('um', 'parametro_b' ) )
        #    thread.start_new_thread( funcao, ('dois', 'parametro_b') )
        #except:
        #   print "Error: unable to start thread"

        #while 1:
        #   pass
