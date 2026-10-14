"""Entrada do protótipo MGPEB. Execute: python3 main.py."""

from mgpeb.entrada import cadastrar_modulos, ler_texto, ler_horario, ler_opcao
from mgpeb.exibicao import exibir_lista
from mgpeb.buscas import (
    buscar_menor_combustivel, buscar_maior_prioridade, buscar_por_tipo,
    buscar_por_criticidade, busca_binaria_por_chegada,
)
from mgpeb.ordenacao import (
    bubble_sort_por_chegada, selection_sort_por_combustivel,
    insertion_sort_fila_pouso,
)
from mgpeb.simulacao import simular_pousos, desempilhar_historico


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
    print("O pouso exige combustível de pelo menos 30%, sensores funcionando,")
    print("vento de até 60 km/h sem tempestade e área livre.")
    print("Falha no módulo (combustível abaixo de 30% ou sensores com defeito) gera alerta.")
    print("Se o ambiente não permitir, o módulo fica em espera, perde 5% de combustível e volta ao fim da fila.")
    pousados, em_espera, em_alerta, historico = simular_pousos(fila_pouso)

    # Resultado final
    print("\nResultado final")
    exibir_lista("Pousados", pousados)
    exibir_lista("Em espera", em_espera)
    exibir_lista("Em alerta", em_alerta)
    desempilhar_historico(historico, 3)


if __name__ == "__main__":
    main()
