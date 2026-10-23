# PA & PG LAB

Gerador de **Progressões Aritméticas (PA)** e **Progressões Geométricas (PG)** em Python, com interface moderna em [customTkinter](https://github.com/TomSchimansky/CustomTkinter) e modo **"Alcançar meta"**.

Projeto da disciplina de Matemática Discreta (*Projeto 1 – Explorando PA e PG*), que relaciona conceitos matemáticos com Pensamento Computacional, transformando padrões em algoritmos.

## Funcionalidades

- Escolha entre PA e PG.
- Geração da sequência **termo a termo**, com laço de repetição (sem usar apenas as fórmulas prontas).
- Soma calculada por **acumulador** dentro do laço.
- Verificação automática do resultado com as fórmulas de Sₙ (✔ confere / ✘ diverge).
- **Alcançar meta:** descobre quantos termos são necessários para a soma ultrapassar um valor definido.
- Validação de entradas (campos vazios, quantidade ≤ 0, valores inválidos) e proteção contra metas inalcançáveis.
- Aceita vírgula decimal (ex.: `0,5`).

## Como executar

**Requisitos:** Python 3.9 ou superior.

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU-USUARIO/pa-pg-lab.git
   cd pa-pg-lab
   ```

2. Instale a dependência:

   ```bash
   python -m pip install customtkinter
   ```

3. Execute o programa:

   ```bash
   python codigo_pa_pg.py
   ```

## Como usar

1. Escolha o modo: **Gerar sequência** ou **Alcançar meta**.
2. Escolha o tipo: **Progressão Aritmética** ou **Progressão Geométrica**.
3. Informe o primeiro termo e a razão.
4. Informe a quantidade de termos (modo *Gerar sequência*) ou a meta (modo *Alcançar meta*).
5. Clique no botão e veja o resultado.

## Exemplos

### Gerar sequência: PA

| Entrada | Valor |
|---|---|
| Primeiro termo | 5 |
| Razão | 3 |
| Quantidade | 6 |

```
PA gerada:
5, 8, 11, 14, 17, 20

Último termo: 20
Soma dos termos: 75
```

### Gerar sequência: PG

| Entrada | Valor |
|---|---|
| Primeiro termo | 2 |
| Razão | 3 |
| Quantidade | 5 |

```
PG gerada:
2, 6, 18, 54, 162

Último termo: 162
Soma dos termos: 242
```

### Alcançar meta: PG

| Entrada | Valor |
|---|---|
| Primeiro termo | 2 |
| Razão | 2 |
| Meta | 1000 |

```
São necessários 9 termos.
Soma obtida: 1022
```

## Como funciona

O mesmo laço serve para os dois tipos de progressão. Só muda a forma de obter o próximo termo:

| Tipo | Próximo termo |
|---|---|
| PA | `termo = termo + razao` |
| PG | `termo = termo * razao` |

A soma é acumulada a cada volta do laço (`soma = soma + termo`). As fórmulas prontas são usadas apenas para conferir o resultado:

- **PA:** Sₙ = n · (a₁ + aₙ) / 2
- **PG:** Sₙ = a₁ · (qⁿ − 1) / (q − 1), para q ≠ 1

## Testes realizados

| Teste | Valores | Sequência | Soma | Fórmula |
|---|---|---|---|---|
| PA crescente | a₁ = 5, r = 3, n = 6 | 5, 8, 11, 14, 17, 20 | 75 | 75 |
| PA decrescente | a₁ = 20, r = −4, n = 6 | 20, 16, 12, 8, 4, 0 | 60 | 60 |
| PG crescente | a₁ = 2, q = 3, n = 5 | 2, 6, 18, 54, 162 | 242 | 242 |
| PG decrescente | a₁ = 64, q = 0,5, n = 6 | 64, 32, 16, 8, 4, 2 | 126 | 126 |

## Tecnologias

- Python
- customTkinter

## Autor

Desenvolvido por **SEU NOME** (2026).
