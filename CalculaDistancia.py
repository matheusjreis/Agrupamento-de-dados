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


def distMinkowski(x,y,n,r=1):
    k = 0 
    acc = 0
    while k < n:
        acc += (abs(x[k] - y[k]))**r
        k+=1
    dist = acc**(1/r)
    return round(dist,3) 


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
                lst1.append(distMinkowski(lst[i],lst[j],atributos,2))        
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
                lst1.append(distMinkowski(lst[i],lst[j],atributos,1))        
                j+=1       
            lstAux = lst1.copy()
            lst2.append(lstAux)
            lst1.clear() 
            i+=1
        return lst2


def escreve_distancia(arquivo):
    lst = calculoDist(arquivo,op)
    escreve_arquivo(lst)

def main():
    escreve_distancia(arquivo)

main()