# Anexo — Estruturas de dados do MGPEB

## Modelo e listas

Cada módulo é um dicionário com identificação, tipo de carga, prioridade (1 a 5, sendo 5 a maior), combustível (%), massa (kg), criticidade, horário estimado de chegada à órbita, integridade dos sensores e contador de tentativas. Os horários representam um mesmo dia simulado.

`carregar_modulos_cadastrados`, em `mgpeb/modulos.py`, fornece seis exemplos: habitação, energia, laboratório, logística, suporte médico e comunicações. O cadastro interativo permite acrescentar os módulos definidos pela equipe em uma nova lista.

As listas `pousados`, `em_espera` e `em_alerta`, em `mgpeb/simulacao.py`, registram os destinos de cada módulo. Um módulo adiado entra em `em_espera`; quando volta a ser atendido, sai dessa lista antes de receber a nova decisão. Ao término da simulação, a fila foi consumida e não há módulos em espera.

## Fila de pouso

A fila é representada por uma lista. `pop(0)` retira o primeiro módulo e `append(modulo)` coloca um módulo adiado no final. Assim, após a ordenação inicial, o atendimento segue FIFO: primeiro a entrar, primeiro a sair. Uma espera consome cinco pontos percentuais de combustível.

Por exemplo, com `[HAB-01, ENE-01, LAB-01]`, o próximo módulo atendido é `HAB-01`. Se ele for adiado, a fila passa a `[ENE-01, LAB-01, HAB-01]`.

Antes da simulação, a equipe pode organizar a fila por chegada (bubble sort), combustível crescente (selection sort) ou prioridade decrescente (insertion sort). Na prioridade, os desempates consideram menor combustível e depois chegada mais cedo.

A retirada do início de uma lista exige deslocar os demais elementos, com custo O(n). Essa implementação privilegia os recursos básicos estudados e uma quantidade pequena de módulos.

## Pilha de decisões

`historico` armazena tuplas `(ciclo, identificacao, decisao)`. Cada decisão é empilhada com `append`. `desempilhar_historico` usa `pop()` para apresentar primeiro a decisão mais recente: comportamento LIFO, último a entrar, primeiro a sair.

Por exemplo, após empilhar `(1, "HAB-01", "AUTORIZADO")` e `(2, "ENE-01", "ADIADO")`, o primeiro evento retirado será o de `ENE-01`. A exibição final retira até três registros, consumindo essas entradas da pilha.

## Busca e ordenação

As buscas por menor combustível, maior prioridade, tipo e criticidade percorrem a lista linearmente, com custo O(n). A busca binária por chegada usa uma lista previamente ordenada e custo O(log n) para localizar um horário; se houver horários iguais, retorna um dos módulos correspondentes.

Bubble sort, selection sort e insertion sort têm custo O(n²) no pior caso e trabalham sobre cópias das listas. As cópias compartilham os dicionários dos módulos: durante a simulação, combustível e tentativas são atualizados no próprio módulo.

## Relação com o relatório

Este anexo pode ser incorporado ao PDF final. As regras do circuito e da simulação ainda precisam ser unificadas pela equipe, conforme descrito no README, para que os exemplos do relatório reflitam a decisão definitiva.
