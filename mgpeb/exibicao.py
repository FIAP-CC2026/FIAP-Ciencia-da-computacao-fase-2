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
