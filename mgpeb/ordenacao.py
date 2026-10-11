from .modulos import horario_em_minutos


# Algoritmos de ordenação
def bubble_sort_por_chegada(lista):
    copia = lista.copy()
    tamanho = len(copia)
    for i in range(tamanho - 1):
        for j in range(tamanho - 1 - i):
            chegada_atual = horario_em_minutos(copia[j]["chegada"])
            proxima_chegada = horario_em_minutos(copia[j + 1]["chegada"])
            if chegada_atual > proxima_chegada:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia


def selection_sort_por_combustivel(lista):
    copia = lista.copy()
    tamanho = len(copia)
    for i in range(tamanho - 1):
        indice_menor = i
        for j in range(i + 1, tamanho):
            if copia[j]["combustivel"] < copia[indice_menor]["combustivel"]:
                indice_menor = j
        copia[i], copia[indice_menor] = copia[indice_menor], copia[i]
    return copia


def vem_antes(modulo, outro):
    if modulo["prioridade"] != outro["prioridade"]:
        return modulo["prioridade"] > outro["prioridade"]
    if modulo["combustivel"] != outro["combustivel"]:
        return modulo["combustivel"] < outro["combustivel"]
    return horario_em_minutos(modulo["chegada"]) < horario_em_minutos(outro["chegada"])


def insertion_sort_fila_pouso(lista):
    copia = lista.copy()
    for i in range(1, len(copia)):
        atual = copia[i]
        j = i - 1
        while j >= 0 and vem_antes(atual, copia[j]):
            copia[j + 1] = copia[j]
            j -= 1
        copia[j + 1] = atual
    return copia
