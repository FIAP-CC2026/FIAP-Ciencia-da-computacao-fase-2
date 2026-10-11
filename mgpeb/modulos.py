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
