# Regras de decisão e portas lógicas

Circuito feito no CircuitVerse (arquivo painel_pouso.cv, abrir em Project > Import Project).

## Entradas

- C = combustível (1 se tiver 30% ou mais)
- S = sensores (1 se estiverem funcionando)
- A = atmosfera (1 se o vento estiver até 60 km/h e não tiver tempestade)
- L = área de pouso livre (1 se estiver livre)

## Regras

Primeiro juntamos as entradas em dois grupos:

- modulo ok = C AND S
- ambiente ok = A AND L

Depois as saídas:

- AUTORIZADO = modulo ok AND ambiente ok
- ALERTA = NOT modulo ok (problema no próprio módulo)
- ESPERA = modulo ok AND NOT ambiente ok (módulo bem, mas não dá pra pousar agora)

Se o módulo tem problema, ele vai direto pra ALERTA, mesmo que o tempo esteja ruim, porque com pouco combustível ele não pode ficar esperando.

Também colocamos uma porta NOT em cada entrada ligada a um LED vermelho, pra mostrar qual condição falhou.

## Tabela verdade

| C | S | A | L | AUTORIZADO | ALERTA | ESPERA |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| C ou S = 0 | | qualquer | qualquer | 0 | 1 | 0 |

(as 12 combinações em que C ou S é 0 dão ALERTA)

## Prints

- circuito_autorizado.png: tudo ligado, pouso autorizado
- circuito_alerta.png: sensor desligado, vai pra alerta
- circuito_espera.png: atmosfera ruim, fica em espera
