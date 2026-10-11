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
