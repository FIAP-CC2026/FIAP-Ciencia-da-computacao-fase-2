# Criação dos módulos e conversão de horários
def criar_modulo(id_modulo, tipo, prioridade, combustivel, massa,
                 criticidade, chegada, sensores_ok=True):
    return {
        "id": id_modulo,
        "tipo": tipo,
        "prioridade": prioridade,
        "combustivel": combustivel,
        "massa": massa,
        "criticidade": criticidade,
        "chegada": chegada,
        "sensores_ok": sensores_ok,
        "tentativas": 0,
    }


def horario_em_minutos(horario):
    horas, minutos = horario.split(":")
    return int(horas) * 60 + int(minutos)


# Cadastro dos módulos
def carregar_modulos_cadastrados():
    return [
        criar_modulo("HAB-01", "Habitação",       5, 62, 18000, "Alta",  "08:10"),
        criar_modulo("ENE-01", "Energia",         5, 28, 12500, "Alta",  "08:25"),
        criar_modulo("LAB-01", "Laboratório",     3, 75,  9800, "Média", "08:40"),
        criar_modulo("LOG-01", "Logística",       2, 55, 21000, "Baixa", "08:05"),
        criar_modulo("MED-01", "Suporte Médico",  4, 12,  7600, "Alta",  "08:30"),
        criar_modulo("COM-01", "Comunicações",    3, 48,  5400, "Média", "08:50",
                     sensores_ok=False),
    ]


# Entrada de dados
def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Preencha este campo.")


def ler_inteiro(mensagem, minimo, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo and (maximo is None or valor <= maximo):
                return valor
        except ValueError:
            pass
        if maximo is None:
            print(f"Digite um número inteiro a partir de {minimo}.")
        else:
            print(f"Digite um número inteiro entre {minimo} e {maximo}.")


def ler_opcao(mensagem, opcoes):
    while True:
        opcao = input(mensagem).strip().lower()
        if opcao in opcoes:
            return opcao
        print("Opção inválida. Tente novamente.")


def ler_horario(mensagem):
    while True:
        horario = input(mensagem).strip()
        partes = horario.split(":")
        if len(partes) == 2:
            horas, minutos = partes
            if horas.isdigit() and minutos.isdigit():
                horas = int(horas)
                minutos = int(minutos)
                if 0 <= horas <= 23 and 0 <= minutos <= 59:
                    return f"{horas:02d}:{minutos:02d}"
        print("Digite um horário válido, como 08:30.")


# Cadastro pelo terminal
def cadastrar_modulos():
    print("\n1 - Cadastrar novos módulos")
    print("2 - Usar os módulos já cadastrados")
    escolha = ler_opcao("Escolha uma opção: ", ("1", "2"))
    if escolha == "2":
        return carregar_modulos_cadastrados()

    modulos = []
    identificacoes = []
    quantidade = ler_inteiro("Quantos módulos deseja cadastrar? ", 1)
    for numero in range(quantidade):
        print(f"\nMódulo {numero + 1}")
        while True:
            id_modulo = ler_texto("Identificação: ").upper()
            if id_modulo not in identificacoes:
                break
            print("Esta identificação já foi cadastrada.")
        tipo = ler_texto("Tipo de carga: ")
        prioridade = ler_inteiro("Prioridade (1 a 5, sendo 5 a maior): ", 1, 5)
        combustivel = ler_inteiro("Combustível (%): ", 0, 100)
        massa = ler_inteiro("Massa (kg): ", 1)
        criticidade = ler_opcao("Criticidade (alta, média ou baixa): ",
                               ("alta", "média", "media", "baixa"))
        if criticidade == "media":
            criticidade = "média"
        chegada = ler_horario("Horário de chegada (HH:MM): ")
        resposta = ler_opcao("Sensores funcionando? (s/n): ", ("s", "n"))
        sensores_ok = resposta == "s"
        modulo = criar_modulo(id_modulo, tipo, prioridade, combustivel, massa,
                              criticidade.capitalize(), chegada, sensores_ok)
        modulos.append(modulo)
        identificacoes.append(id_modulo)
        print("Módulo cadastrado.")
    return modulos


# Exibição dos módulos
def exibir_modulo(modulo):
    sensores = "ok" if modulo["sensores_ok"] else "com falha"
    print(f"{modulo['id']} - {modulo['tipo']} | prioridade {modulo['prioridade']} | "
          f"combustível {modulo['combustivel']}% | massa {modulo['massa']} kg | "
          f"criticidade {modulo['criticidade']} | chegada {modulo['chegada']} | "
          f"sensores {sensores}")


def exibir_lista(titulo, lista):
    print(f"\n{titulo}:")
    if not lista:
        print("Nenhum módulo.")
        return
    for modulo in lista:
        exibir_modulo(modulo)


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


# Regras lógicas de autorização de pouso

LIMITE_EMERGENCIA = 15
CONSUMO_POR_ESPERA = 5
MAX_TENTATIVAS = 3


def avaliar_pouso(modulo, atmosfera_ok, area_livre):
    emergencia = modulo["combustivel"] < LIMITE_EMERGENCIA

    if not modulo["sensores_ok"]:
        return "ALERTA"
    elif area_livre and atmosfera_ok:
        return "AUTORIZADO"
    elif area_livre and emergencia:
        return "EMERGENCIAL"
    elif modulo["tentativas"] >= MAX_TENTATIVAS:
        return "ALERTA"
    else:
        return "ADIADO"


# Simulação dos ciclos de pouso
CONDICOES_POR_CICLO = [
    (True,  True),
    (False, True),
    (False, True),
    (True,  False),
    (True,  True),
]


def simular_pousos(fila_pouso):
    pousados = []
    em_espera = []
    em_alerta = []
    historico = []
    ciclo = 0

    while fila_pouso:
        if ciclo < len(CONDICOES_POR_CICLO):
            atmosfera_ok, area_livre = CONDICOES_POR_CICLO[ciclo]
        else:
            atmosfera_ok, area_livre = True, True
        ciclo += 1

        modulo = fila_pouso.pop(0)
        decisao = avaliar_pouso(modulo, atmosfera_ok, area_livre)

        clima = "favorável" if atmosfera_ok else "desfavorável"
        area = "livre" if area_livre else "ocupada"
        print(f"\nCiclo {ciclo}: {modulo['id']} ({modulo['tipo']}) | "
              f"combustível {modulo['combustivel']}% | clima {clima} | área {area}")

        if modulo in em_espera:
            em_espera.remove(modulo)

        if decisao in ("AUTORIZADO", "EMERGENCIAL"):
            pousados.append(modulo)
            print(f"Pouso {decisao.lower()}.")
        elif decisao == "ALERTA":
            em_alerta.append(modulo)
            print("Módulo encaminhado para inspeção.")
        else:
            modulo["tentativas"] += 1
            modulo["combustivel"] = max(0, modulo["combustivel"] - CONSUMO_POR_ESPERA)
            em_espera.append(modulo)
            fila_pouso.append(modulo)
            print(f"Pouso adiado (tentativa {modulo['tentativas']}), "
                  f"combustível agora {modulo['combustivel']}%")

        historico.append((ciclo, modulo["id"], decisao))

    return pousados, em_espera, em_alerta, historico


def desempilhar_historico(historico, quantidade):
    print(f"\nÚltimas {quantidade} decisões:")
    for _ in range(quantidade):
        if not historico:
            break
        ciclo, id_modulo, decisao = historico.pop()
        print(f"  ciclo {ciclo}: {id_modulo} -> {decisao}")


# Programa principal
def main():
    print("Missão Aurora Siger - Controle de pousos")

    # Cadastro
    fila_pouso = cadastrar_modulos()
    exibir_lista("Fila inicial", fila_pouso)

    # Buscas
    print("\nBusca de módulos")
    print("Vamos consultar o combustível, a prioridade, o tipo de carga e a chegada.")
    modulo = buscar_menor_combustivel(fila_pouso)
    print(f"Menor combustível: {modulo['id']} ({modulo['combustivel']}%)")
    modulo = buscar_maior_prioridade(fila_pouso)
    print(f"Maior prioridade: {modulo['id']} (prioridade {modulo['prioridade']})")
    tipo = ler_texto("Digite o tipo de carga que deseja localizar (ex.: Energia): ")
    resultado = buscar_por_tipo(fila_pouso, tipo)
    exibir_lista(f"Módulos do tipo {tipo}", resultado)
    resultado = buscar_por_criticidade(fila_pouso, "Alta")
    exibir_lista("Módulos com criticidade alta", resultado)

    por_chegada = bubble_sort_por_chegada(fila_pouso)
    horario = ler_horario("Digite o horário de chegada que deseja localizar (ex.: 08:30): ")
    modulo = busca_binaria_por_chegada(por_chegada, horario)
    if modulo:
        print(f"Módulo com chegada às {horario}: {modulo['id']}")
    else:
        print("Nenhum módulo encontrado nesse horário.")

    # Ordenações
    print("\nSelecione o critério para organizar a fila de pouso:")
    print("1 - Horário de chegada: quem chegou mais cedo pousa primeiro.")
    print("2 - Combustível: quem tem menos combustível pousa primeiro.")
    print("3 - Prioridade: quem tem maior prioridade pousa primeiro.")
    print("    Em caso de empate, vale o menor combustível e depois a chegada mais cedo.")
    criterio = ler_opcao("Digite o número do critério (1, 2 ou 3): ", ("1", "2", "3"))

    if criterio == "1":
        fila_pouso = bubble_sort_por_chegada(fila_pouso)
        criterio_escolhido = "horário de chegada"
    elif criterio == "2":
        fila_pouso = selection_sort_por_combustivel(fila_pouso)
        criterio_escolhido = "menor combustível"
    else:
        fila_pouso = insertion_sort_fila_pouso(fila_pouso)
        criterio_escolhido = "maior prioridade, menor combustível e horário de chegada"

    print(f"\nCritério escolhido: {criterio_escolhido}.")
    exibir_lista("Fila que será usada na simulação", fila_pouso)

    # Simulação
    print("\nSimulação dos pousos")
    print("Os módulos serão atendidos na ordem da fila acima.")
    print("Sensores funcionando e área livre são obrigatórios para pousar.")
    print("Com clima desfavorável, o pouso só ocorre com combustível abaixo de 15%.")
    print("Quem tiver o pouso adiado perde 5% de combustível e volta ao fim da fila.")
    pousados, em_espera, em_alerta, historico = simular_pousos(fila_pouso)

    # Resultado final
    print("\nResultado final")
    exibir_lista("Pousados", pousados)
    exibir_lista("Em espera", em_espera)
    exibir_lista("Em alerta", em_alerta)
    desempilhar_historico(historico, 3)


if __name__ == "__main__":
    main()
