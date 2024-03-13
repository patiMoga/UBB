import time

def sort_alg(lista, comp):
    start_time = time.time()
    n = len(lista)
    for i in range(0, n):
        for j in range(i, n):
            if (lista[j].returnare(comp[0]) < lista[i].returnare(comp[0])) or lista[j].returnare(comp[0]) == lista[i].returnare(comp[0]) and (lista[j].returnare(comp[1]) < lista[i].returnare(comp[1]) or (lista[j].returnare(comp[1]) == lista[i].returnare(comp[1]) and lista[j].returnare(comp[2]) < lista[i].returnare(comp[2]))):
                lista[i], lista[j] = lista[j], lista[i]
    print("the function ends in ", time.time() - start_time, "secs")

def heapify(lista, n, i, comp):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and (lista[i].returnare(comp[0]) < lista[l].returnare(comp[0]) or (lista[i].returnare(comp[0]) == lista[l].returnare(comp[0]) and lista[i].returnare(comp[1]) < lista[l].returnare(comp[1])) or (lista[i].returnare(comp[0]) == lista[l].returnare(comp[0]) and lista[i].returnare(comp[1]) == lista[l].returnare(comp[1]) and lista[i].returnare(comp[2]) < lista[l].returnare(comp[2]))):
        largest = l

    if r < n and (lista[largest].returnare(comp[0]) < lista[r].returnare(comp[0]) or (lista[largest].returnare(comp[0]) == lista[r].returnare(comp[0]) and lista[largest].returnare(comp[1]) < lista[r].returnare(comp[1])) or (lista[largest].returnare(comp[0]) == lista[r].returnare(comp[0]) and lista[largest].returnare(comp[1]) == lista[r].returnare(comp[1]) and lista[largest].returnare(comp[2]) < lista[r].returnare(comp[2]))):
        largest = r

    if largest != i:
        (lista[i], lista[largest]) = (lista[largest], lista[i])  # swap
        heapify(lista, n, largest, comp)

def heapSort(arr, comp):
    start_time = time.time()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, comp)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0, comp)
    print("the function ends in ", time.time() - start_time, "secs")

def search(lista, token):
    for i in lista:
        if i.tokenMasina == token:
            return i