# Bubble sort
def sort(lista):
    for cicli in range(len(lista)-1, 0, -1):
        for riga in range(cicli):
            if lista[riga] > lista[riga + 1]:
                lista[riga], lista[riga + 1] = lista[riga + 1], lista[riga]

miaLista=[23, 5, 78, 1211, 3, 56, 78, 12, 4, 51, 4096, 255]
sort(miaLista)
print(miaLista)
