__author__ = 'lucas'
import multiprocessing




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
        self.saida_unica=[]

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
            print "Thread "+ str(thread_numero) + "SUCCESSFULLY CREATED"
            p = multiprocessing.Process(target=self.funcao, args=(inicio_valor,fim_valor))
            p.start()
            #p.join()
            #self.jobs.append(p)

        #for salvando in self.saida_unica:
        #    self.saida.write(salvando+'\n')
        #while True:
        #    for
        #    print len(self.jobs)


    def funcao(self,inicio,fim):#teste
        self.array_temporario=[]
        '''sobrescreva esse metodos'''
        self.arquivo_para_cruzar=open('arquivo_para_abrir','r').read()
        print 'esse metodo deve ser sobrescrito com os parametros presentes nesse arquivo dentro da classe'
        for array_linha in self.arquivo_array[int(inicio):int(fim)]:
            print array_linha
        for escrever in self.array_temporario: #isso deve ser executado apenas no final da funcao
            self.saida.write(escrever+'\n')




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
                            if cromossomo==interaction_b[0]:
                                if int(start)> int(interaction_b[1])and int(start)< int(interaction_b[2]):

                                    saida_join=(cromossomo,start,end,name,'---->','  '.join(interaction_b),'<---->','  '.join(interaction_a),'\n')
                                    saida_join= ' '.join(saida_join)
                                    saida_join=re.sub('\s+','\t',saida_join)
                                    #self.saida.write(saida_join+'\n')
                                    self.array_temporario.append(saida_join)
                                    print saida_join
                                    break

                for escrever in self.array_temporario:
                    self.saida.write(escrever+'\n')

                        #print interaction_a







teste('linc_enseml.txt',70,'saida_procurar_colocalizacao_lncrna.txt')
