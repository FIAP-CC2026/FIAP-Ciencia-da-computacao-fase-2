from .modulos import horario_em_minutos


# Algoritmos de busca
def buscar_menor_combustivel(lista):
    if not lista:
        return None
    menor = lista[0]
    for modulo in lista:
        if modulo["combustivel"] < menor["combustivel"]:
            menor = modulo
    return menor


def buscar_maior_prioridade(lista):
    if not lista:
        return None
    maior = lista[0]
    for modulo in lista:
        if modulo["prioridade"] > maior["prioridade"]:
            maior = modulo
    return maior


def buscar_por_tipo(lista, tipo):
    encontrados = []
    for modulo in lista:
        if modulo["tipo"].lower() == tipo.lower():
            encontrados.append(modulo)
    return encontrados


def buscar_por_criticidade(lista, criticidade):
    encontrados = []
    for modulo in lista:
        if modulo["criticidade"] == criticidade:
            encontrados.append(modulo)
    return encontrados


def busca_binaria_por_chegada(lista_ordenada, horario):
    alvo = horario_em_minutos(horario)
    inicio = 0
    fim = len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor = horario_em_minutos(lista_ordenada[meio]["chegada"])
        if valor == alvo:
            return lista_ordenada[meio]
        elif valor < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None
