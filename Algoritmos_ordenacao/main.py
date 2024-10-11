from algoritmos.selectionSort import selection_sort
from algoritmos.bubbleSort import bubble_sort

if __name__ == '__main__':

    # Definindo a lista
    listaSelection = [7, 5, 1, 8, 3]

    # Chamando a função importada para encontrar o menor valor
    lista_selection = selection_sort(listaSelection)

    # Imprimindo o menor valor da lista
    print(f'lista ordenada com selection sort: {lista_selection}')

    # BUBBLE SORT

    listaBubble = []

    lista_bubble = bubble_sort(listaBubble)

    print(f'lista com bubble sort: {lista_bubble}')
