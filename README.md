# MGPEB — Missão Aurora Siger

Protótipo acadêmico do **Módulo de Gerenciamento de Pouso e Estabilização de Base**, desenvolvido para a Fase 2 de Ciência da Computação da FIAP. Organiza módulos da colônia em Marte, consulta seus atributos, ordena a fila e simula decisões de pouso.

## Execução

Requer Python 3, sem dependências externas. Na raiz do repositório:

```bash
python3 main.py
```

Para experimentar os dados de exemplo, escolha `2`, consulte o tipo `Energia`, informe `08:30` e escolha um dos três critérios de ordenação. Também é possível cadastrar módulos pelo terminal.

## Organização

```text
main.py                         Entrada e fluxo do programa
mgpeb/
    __init__.py                 Identificação do pacote
    modulos.py                  Modelo dos módulos e dados de exemplo
    entrada.py                  Cadastro e validação de entradas
    exibicao.py                 Exibição dos módulos
    buscas.py                   Buscas lineares e busca binária
    ordenacao.py                Bubble, selection e insertion sort
    regras_pouso.py             Funções de decisão de pouso
    simulacao.py                Fila, ciclos e pilha de decisões
docs/
    estruturas_dados.md         Anexo de listas, fila e pilha
    modelagem_matematica_e_contexto_historico.pdf
                                Contribuição das seções 4 e 5 (Gustavo)
    relatorio_tecnico.pdf       Relatório técnico final para entrega
    portas_logicas/
        regras_logicas.md       Expressões booleanas e tabela verdade
        painel_pouso.cv         Projeto para importar no CircuitVerse
        circuito_*.png          Exemplos visuais das saídas
```

Os arquivos e funções usam nomes descritivos em português, sem acentos, em `snake_case`. Os algoritmos clássicos mantêm seus nomes usuais. O programa utiliza apenas recursos básicos do Python e estruturas lineares implementadas com listas.

## Relação com a atividade

| Conteúdo | Material |
| --- | --- |
| Cenário, atributos e cadastro de módulos | `mgpeb/modulos.py` e `mgpeb/entrada.py` |
| Portas lógicas e funções booleanas | [Regras e circuito](docs/portas_logicas/regras_logicas.md) |
| Condicionais, buscas, ordenações e simulação | Pacote `mgpeb/`, executado por `main.py` |
| Listas, fila e pilha | [Anexo de estruturas de dados](docs/estruturas_dados.md) |
| Modelagem matemática e evolução da computação | [Seções 4 e 5 — contribuição do Gustavo](docs/modelagem_matematica_e_contexto_historico.pdf) |
| ESG e governança | Seção 8 do [relatório técnico](docs/relatorio_tecnico.pdf) |
| Relatório técnico de 5 a 10 páginas em PDF | [Relatório técnico final](docs/relatorio_tecnico.pdf) |

## Regras de decisão usadas no relatório

A simulação e o circuito usam a mesma regra, implementada em `autorizar_pouso` (`mgpeb/regras_pouso.py`). Ela recebe `combustivel`, `sensores_ok`, `vento`, `tempestade` e `area_livre` e retorna `AUTORIZADO`, `ALERTA` ou `ESPERA`:

- `C`: combustível de pelo menos 30%.
- `S`: sensores íntegros.
- `A`: vento de até 60 km/h e ausência de tempestade.
- `L`: área de pouso livre.
- `AUTORIZADO`: `(C and S) and (A and L)`.
- `ALERTA`: `not (C and S)`, falha no próprio módulo.
- `ESPERA`: `(C and S) and not (A and L)`, módulo bem, mas o ambiente não permite pousar agora.

Na simulação, cada ciclo define vento, tempestade e área livre (`CONDICOES_POR_CICLO` em `mgpeb/simulacao.py`). Um módulo em `ESPERA` perde 5% de combustível e volta ao fim da fila; ao cair abaixo de 30%, passa a `ALERTA`. Com os módulos de exemplo, aparecem os três resultados: `LAB-01` autorizado, `HAB-01` em espera e `ENE-01` em alerta
