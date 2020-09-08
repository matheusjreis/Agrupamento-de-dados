import csv
from statistics import mode


def inverte(lst):                                               # Transforma linha em coluna e vice-versa
    lst1 = list()
    lst2 = list()

    k = i = 0

    while k < len(lst[0]):
        i = 0
        while i < len(lst):
            lst1.append(lst[i][k])
            i+=1
        lstAux = lst1.copy()
        lst2.append(lstAux)
        lst1.clear()
        k+=1
    return lst2


def media(lst):                                                  # Aplica a media nos elementos de uma lista.
    tam = len(lst)
    m = sum(lst)
    return round((m / tam), 1)


def moda_media(lst1):                                            # Escolhe entre a média e a moda e aplica.
    lstAux = lst1.copy()
    lst2 = lst1.copy()

    n = lstAux.count('?')
    for i in range(0, n):
        lstAux.remove('?')

    for j, num in enumerate(lst1):
        try:
            if(num != '?'):
                num = float(num)
                lst1[j] = num
        except ValueError:
                num = str(num)
    for j, num in enumerate(lstAux):                               # Retira as strings da lista.
        try:
            if (num != '?'):
                num = float(num)
                lstAux[j] = num
        except ValueError:
                num = str(num)
                lstAux.remove(num)
    i = 0
    while (i < len(lst1)):
        lst2[i] = lst1[i]
        if (lst2[i] == '?'):
                try:                                                    # Tenta aplicar a moda, caso não seja possível, se aplica 
                    lst2[i] = mode(lstAux)                              # a média.
                except:
                   lst2[i] = media(lstAux)                             
        i += 1                                                          
    return lst2


entrada = str(input('Digite o nome do arquivo: '))

lst1 = list()

with open(entrada,'r') as arq:
    leitor = csv.reader(arq, delimiter = ',')
    for elem in leitor:
        lst1.append(elem)

lst2 = inverte(lst1).copy()

lst3 = list()

for l in lst2:
    lst3.append(moda_media(l))
lst4 = inverte(lst3)

with open('saida.csv','w',newline='') as saida:
    escritor = csv.writer(saida)
    for l in lst4:
        escritor.writerow(l)
