import csv
import math

arquivo = str(input('Digite o nome do arquivo: '))
op = int(input('Digite a medida de distância:\n 1 - Distância Euclidiana\n 2 - Distância Manhattan\n>>> '))

def le_arquivo(arquivo):
    lst = list()
    with open(arquivo,'r') as arq:
        leitor = csv.reader(arq, delimiter = ',')
        for elem in leitor:
            lst.append(elem)
    return lst


def escreve_arquivo(lst):
    with open('saida.csv','w',newline='') as saida:
        escritor = csv.writer(saida)
        for linha in lst:
            escritor.writerow(linha)


def converte_para_float(arquivo):
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


# b)
def distEuclidiana(x,y,n):                              #n = numero de atributos
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


def distManhattan(x,y,n):
    """
    parâmetro 1: lista
    parâmetro 2: lista 
    parâmetro 3: inteiro

    return : float
    """
    k = 0
    dist = 0
    while k < n:
        dist += abs(x[k]-y[k])
        k+=1
    return round(dist,3)


#c)
def calculoDist(arquivo,op = 1):
    lst = converte_para_float(arquivo).copy()
    lst1 = list()
    lst2 = list()

    i = j = 0

    atributos = len(lst[0])
    
    if(op == 1):
        while i < len(lst):     
            j = 0
            while j < len(lst):
                lst1.append(distEuclidiana(lst[i],lst[j],atributos))        
                j+=1                       
            lstAux = lst1.copy()
            lst2.append(lstAux)
            lst1.clear() 
            i+=1
        return lst2
    elif(op == 2):
        while i < len(lst):     
            j = 0
            while j < len(lst):
                lst1.append(distManhattan(lst[i],lst[j],atributos))        
                j+=1       
            lstAux = lst1.copy()
            lst2.append(lstAux)
            lst1.clear() 
            i+=1
        return lst2


#d)
def escreve_distancia(arquivo):
    lst = calculoDist(arquivo,op)
    escreve_arquivo(lst)


escreve_distancia(arquivo)