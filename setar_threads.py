__author__ = 'lucas'
import threading
class setar_threads:
    def __init__(self,arquivo,numero_threads):
        self.arquivo=arquivo
        self.threads = []
        self.numero_threads=numero_threads
        self.array_saida_linhas=[]
        self.arquivo_ler=open (self.arquivo,'r').read()
        for linha in self.arquivo_ler.split('\n'):
            if len(linha)>0:
                self.array_saida_linhas.append(linha)
        self.quantidade_por_thread=(len(self.array_saida_linhas)/self.numero_threads)
        self.array_separacao=[]
        print self.quantidade_por_thread
        for x_thread in range(0,self.numero_threads):
            print((x_thread*self.quantidade_por_thread,(x_thread*self.quantidade_por_thread)+(self.quantidade_por_thread-1)))
            self.array_separacao.append((x_thread*self.quantidade_por_thread,(x_thread*self.quantidade_por_thread)+(self.quantidade_por_thread-1)))

        #print self.array_separacao
    def retorno(self):
        '''retorno numero de treads e array com positions e array com valores das linhas com dados armazenadas'''
        return self.numero_threads,self.array_separacao,self.array_saida_linhas
    def executar(self):
        for num in range(0, self.numero_threads):
            tabela= (self.retorno()[2][self.retorno()[1][num][0]:self.retorno()[1][num][1]])
            #print (tabela)
            thread = usar_thread(tabela)
            thread.start()
            self.threads.append(thread)

        #for thread in self.threads:
        #    thread.join()

class usar_thread(threading.Thread):

    def __init__ (self,dados_cortados):
        threading.Thread.__init__(self)
        self.arquivo = dados_cortados


    def run(self): # SUBSTITUIR ESSE METODO
                    #crie uma nova saida
        import re
        print 'iniciada'
        #print self.arquivo
        chia_pet_file=open('hela_s3_chia_pet_pol2.bed','r').read()

        for linha in self.arquivo:
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
                                    #saida.write (saida_join+'\n')
                                    print saida_join
                                    break
                                    #print (cromossomo,start,end,name,'---->',interaction_a,'<---->',interaction_b)
                            if cromossomo==interaction_b[0]:
                                if int(start)> int(interaction_b[1])and int(start)< int(interaction_b[2]):

                                    saida_join=(cromossomo,start,end,name,'---->','  '.join(interaction_b),'<---->','  '.join(interaction_a),'\n')
                                    saida_join= ' '.join(saida_join)
                                    saida_join=re.sub('\s+','\t',saida_join)
                                    #saida.write (saida_join+'\n')
                                    #print cromossomo,start,end,name,'---->',interaction_b,'<---->',interaction_a print saida_join
                                    print saida_join
                                    break



## EXECUTAR O PROGRAMA
testando=setar_threads('linc_enseml.txt',3) # numero de processadores
testando.executar()
