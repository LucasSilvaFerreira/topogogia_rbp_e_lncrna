__author__ = 'lucas'
'''fazer com que ele encontre os exons...por enquanto so encontra o refseq'''
ref_seq_arquivo=open('refseq.txt','r').read()
entrada_marcas_cooloc= open('saida_encontrar_marcas_cooloc.txt','r').read()
saida=open('saida_find_refseq.txt','w')
for entrada in entrada_marcas_cooloc.split('\n'):
    if len(entrada)>0:
        procurar_query=entrada.split('\t')[2]
        #print procurar_query
        chr_query=entrada.split('\t')[1]
        for refs in ref_seq_arquivo.split('\n'):
            if len(refs)>0:
                process_ref=refs.split('\t')
                chr_ref=process_ref[2]
                #print chr_ref
                if chr_query == chr_ref:
                    if int(procurar_query)> int(process_ref[4]) and int(procurar_query)< int(process_ref[5]):
                        #print int(procurar_query),int(process_ref[4]),int(process_ref[5]),process_ref[1],process_ref[3]
                        saida_formatada= '\t'.join(((procurar_query),(process_ref[4]),(process_ref[5]),process_ref[1],process_ref[3]))
                        saida.write(saida_formatada+'\n')
                        print(saida_formatada+'\n')
                        break