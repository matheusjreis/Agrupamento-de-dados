import csv 
import math
import random

arquivo = str(input('Digite o nome do arquivo: '))
k = int(input('Digite o número de grupos: '))

def nomeia_grupo(lst):                                          
    lst2 = list()
    for i,l in enumerate(lst):
        lst2.append([f'Grupo {i+1}']+l)
    return lst2


def le_arquivo(arquivo):                                        # lê o arquivo csv e retorna uma lista de listas de strings
    lst = list()
    with open(arquivo,'r') as arq:
        leitor = csv.reader(arq, delimiter = ',')
        for elem in leitor:
            lst.append(elem)
    return lst


def escreve_arquivo(lst):                                       # lê uma lista de listas e escreve ela no arquivo
    lst2 = nomeia_grupo(lst)
    with open('saida.csv','w',newline='') as saida:
        escritor = csv.writer(saida)
        for linha in lst2:
            escritor.writerow(linha)

 
def converte_para_float(arquivo):                               # converte a listas de listas para float
    lst1 = le_arquivo(arquivo)
    lst3 = list()
    lst4 = list()

    for lst2 in lst1:
        for elem in lst2:
            elem = float(elem)
            lst3.append(elem)
        lstAux = lst3.copy()
        lst4.append(lstAux)
        lst3.clear()
    return lst4


def distEuclidiana(x,y,n):                                      # n = numero de atributos
    """
    parâmetro 1: lista
    parâmetro 2: lista 
    parâmetro 3: inteiro

    return : float
    """
    k = 0 
    acc = 0
    while k < n:
        acc += ((x[k] - y[k])**2)
        k+=1
    dist = math.sqrt(acc)
    return round(dist,3)                                 


def unifica_lista(lst):                                         # Transforma uma lista de listas em uma lista
    lstAux = list()
    for l in lst:
        lstAux +=l
    return lstAux


def centroideInicial(lst,k):                                    # escolhe as centróides aleatóriamente entre os objetos da base de dados
    i = 0   
    centro = list()
    while i < k:
        a = random.randint(0,len(lst)-1)                        # sorteia uma posição
        centro.append(lst[a])
        i+=1
    return centro                                               # retorna uma lista de listas com as centróides


def novoCentroide(lst):                                         # recebe uma lista de listas
    medias = list()
    i = 0
    while i < len(lst):
        try:
            m = sum(lst[i])/len(lst[i])
        except ZeroDivisionError:                               # caso o tamanho da lista seja 0 
            m = sum(lst[i])/1
        medias.append(round(m,3))
        i+=1
    return medias


def PosMaisProxima(elem,lstCentros):                            # recebe um elemento e uma lista de centroídes e verifica qual a centróide
    menor = distEuclidiana([elem],[lstCentros[0]],1)            # mais próxima desse elemento e retorna a posição dessa centróide.
    pos = 0

    i = 0
    while i < len(lstCentros):                            
        if((distEuclidiana([elem],[lstCentros[i]],1))< menor):
            menor = (distEuclidiana([elem],[lstCentros[i]],1))
            pos = i
        i+=1
    return pos                                                  # retorna a posição do centro mais próximo


def K_means(lst, k):
    lst2 = list()                                                
    lstCentroides = list()                                         # armazena todas as listas de centróides em uma lista.                                              

    aux = 0

    i = 0
    while i < k:                                                    # preenche a lista com listas vazias para armazenar os grupos.  
        lst2.append([])
        i+=1
    
    lst1 = centroideInicial(lst,k)

    lstCentroides.append(lst1)
    aux+=1

    for elem in lst:
        lst2[PosMaisProxima(elem,lst1)].append(elem)
    
    j = 0
    while j < 100:
        lst1 = novoCentroide(lst2)
        lstCentroides.append(lst1)
        lst2.clear()
        i = 0

        while i < k:
            lst2.append([])
            i+=1

        for elem in lst:
            lst2[PosMaisProxima(elem,lst1)].append(elem)


        if(lstCentroides[aux] == lstCentroides[aux-1]):                  # Verifica se as centróides se repetem, logo, convergiu.
            break                                                     

        aux+=1
        j+=1
    return lst2


lstAux = converte_para_float(arquivo)

lst = unifica_lista(lstAux)

lst1 = K_means(lst,k)

escreve_arquivo(lst1)