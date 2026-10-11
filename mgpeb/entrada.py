from .modulos import criar_modulo, carregar_modulos_cadastrados


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
