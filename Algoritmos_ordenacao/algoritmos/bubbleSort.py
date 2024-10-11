# algoritmo de ordenação por flutuação - comparar elementos que estão em posições consecutivas
def bubble_sort(lista):
    n = len(lista)

    for i in range(n - 1): # andar até o penultimo item da lista, pq o ultimo não ngm para comparar (o python não vai incluir o -1, o ultimo item)
        if lista[i] > lista[i+1]:
            