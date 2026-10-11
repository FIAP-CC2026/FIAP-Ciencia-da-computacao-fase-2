# 3.1 - Autorização de pouso (if/elif/else)

def autorizar_pouso(combustivel, sensores_ok, vento, tempestade, area_livre):
    """Retorna "AUTORIZADO", "ALERTA" ou "ESPERA"."""

    # Sinais do circuito
    C = combustivel >= 30               # combustível suficiente (%)
    S = sensores_ok                     # sensores ok
    A = vento <= 60 and not tempestade  # atmosfera ok (vento em km/h)
    L = area_livre                      # área de pouso livre

    modulo_ok = C and S
    ambiente_ok = A and L

    # Decisão
    if modulo_ok and ambiente_ok:
        return "AUTORIZADO"
    elif not modulo_ok:
        return "ALERTA"
    else:
        return "ESPERA"


if __name__ == "__main__":
    print(autorizar_pouso(85, True, 40, False, True))
