from .regras_pouso import autorizar_pouso, CONSUMO_POR_ESPERA


# Simulação dos ciclos de pouso
# Cada ciclo: (vento em km/h, tempestade, área livre)
CONDICOES_POR_CICLO = [
    (40, False, True),
    (80, False, True),
    (40, True,  True),
    (40, False, False),
    (40, False, True),
]


def simular_pousos(fila_pouso):
    pousados = []
    em_espera = []
    em_alerta = []
    historico = []
    ciclo = 0

    while fila_pouso:
        if ciclo < len(CONDICOES_POR_CICLO):
            vento, tempestade, area_livre = CONDICOES_POR_CICLO[ciclo]
        else:
            vento, tempestade, area_livre = 40, False, True
        ciclo += 1

        modulo = fila_pouso.pop(0)
        decisao = autorizar_pouso(modulo["combustivel"], modulo["sensores_ok"],
                                  vento, tempestade, area_livre)

        area = "livre" if area_livre else "ocupada"
        print(f"\nCiclo {ciclo}: {modulo['id']} ({modulo['tipo']}) | "
              f"combustível {modulo['combustivel']}% | vento {vento} km/h | "
              f"tempestade {'sim' if tempestade else 'não'} | área {area}")

        if modulo in em_espera:
            em_espera.remove(modulo)

        if decisao == "AUTORIZADO":
            pousados.append(modulo)
            print("Pouso autorizado.")
        elif decisao == "ALERTA":
            em_alerta.append(modulo)
            print("Módulo encaminhado para inspeção.")
        else:
            modulo["tentativas"] += 1
            modulo["combustivel"] = max(0, modulo["combustivel"] - CONSUMO_POR_ESPERA)
            em_espera.append(modulo)
            fila_pouso.append(modulo)
            print(f"Pouso em espera (tentativa {modulo['tentativas']}), "
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
