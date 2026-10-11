from .regras_pouso import avaliar_pouso, CONSUMO_POR_ESPERA


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
