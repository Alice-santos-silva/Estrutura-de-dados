def selection_sort(lista):
    # Loop externo percorre a lista até o penúltimo elemento
    for j in range(len(lista) - 1):
        min_index = j
        # Loop interno encontra o menor elemento no subarray não ordenado
        for i in range(j + 1, len(lista)):
            if lista[i] < lista[min_index]:
                min_index = i

        # Troca o menor elemento encontrado com o primeiro elemento do subarray
        if min_index != j:
            auxiliar = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = auxiliar

    return lista  # Retorna a lista ordenada
