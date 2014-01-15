class thread_processador:
    from itertools import count

    '''A funcao principal devera sobrescrita utilizando o seu codigo desejado com ao menos 2 metodos de entrada um para o fim outro para o inicio da tabela'''
    def __init__(self,file,n_process,saida_nome):
        __author__ = 'lucas'
        import thread,time

        '''script generico para fazer uma tread em um arquivo com varias entradas'''

        self.numero_threads= n_process
        self.arquivo_escolhido= file
        self.saida_nome=saida_nome

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
        print tamanho_threads
        range_threads= len(self.arquivo_array)/self.numero_threads
        #
        for thread_numero in range (0,self.numero_threads):
            print thread_numero*range_threads,thread_numero*range_threads+range_threads-1 #estou perdendo o ultimo valor da tabela
            inicio_valor=thread_numero*range_threads
            fim_valor=thread_numero*range_threads+range_threads-1
            print inicio_valor,fim_valor
            try:
                thread.start_new_thread(self.funcao,(inicio_valor,fim_valor))
                print "Thread "+ thread_numero +"SUCCESSFULLY CREATED"
            except:
                print "Error: unable to start thread"
            time.sleep(0.01)
    def funcao(self,inicio,fim):#teste
        '''sobrescreva esse metodos'''
        print 'esse metodo deve ser sobrescrito com os parametros presentes nesse arquivo dentro da classe'
        for array_linha in self.arquivo_array[int(inicio):int(fim)]:
            print array_linha


class teste(thread_processador):
    print 'start'
    chia_pet_file=open('hela_s3_chia_pet_pol2.bed','r').read()
    #arquivo= open('linc_enseml.txt','r')
    def funcao(self,inicio,fim):
        for linha in self.arquivo_array[int(inicio):int(fim)]:
            if re.search('chr(\d+|.)\t',linha):
                cromossomo= linha.split()[2]
                start=linha.split()[4]
                end=linha.split()[5]
                name=linha.split()[1]
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
                                    self.saida.write (saida_join+'\n')
                                    #print cromossomo,start,end,name,'---->',interaction_b,'<---->',interaction_a print saida_join
                                    print saida_join
                                    break

                        #print interaction_a







teste('refseq.txt',40,'refseq_saida_apagar.txt')


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
