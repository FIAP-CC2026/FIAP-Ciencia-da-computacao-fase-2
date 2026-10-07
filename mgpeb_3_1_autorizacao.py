# 3.1 - Autorização de pouso (if/elif/else)

# Entradas (valores de exemplo)
combustivel = 85      # nível de combustível (%)
sensores_ok = True    # sensores sem falha
vento = 40            # velocidade do vento (km/h)
tempestade = False    # há tempestade?
area_livre = True     # área de pouso livre

# Sinais do circuito
C = combustivel >= 30               # combustível suficiente
S = sensores_ok                     # sensores ok
A = vento <= 60 and not tempestade  # atmosfera ok
L = area_livre                      # área de pouso livre

modulo_ok = C and S
ambiente_ok = A and L

# Decisão
if modulo_ok and ambiente_ok:
    decisao = "AUTORIZADO"
elif not modulo_ok:
    decisao = "ALERTA"
else:
    decisao = "ESPERA"

print(decisao)
