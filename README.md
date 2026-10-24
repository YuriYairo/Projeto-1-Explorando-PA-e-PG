# PA & PG LAB

Gerador de **Progressões Aritméticas (PA)** e **Progressões Geométricas (PG)** em Python, com interface moderna em [customTkinter](https://github.com/TomSchimansky/CustomTkinter) e modo **"Alcançar meta"**.

Projeto da disciplina de Matemática Discreta (*Projeto 1 – Explorando PA e PG*), que relaciona conceitos matemáticos com Pensamento Computacional, transformando padrões matemáticos em algoritmos.

## Autores

- Matheus Yuri
- Lucas Henrique
- Vinicius Fernandes

## Funcionalidades

- Escolha entre PA e PG.
- Geração da sequência **termo a termo**, com laço de repetição (sem usar apenas as fórmulas prontas).
- Soma calculada por **acumulador** dentro do laço.
- Verificação automática do resultado com as fórmulas de Sₙ (✔ confere / ✘ diverge).
- **Alcançar meta:** descobre quantos termos são necessários para a soma ultrapassar um valor definido.
- Validação das entradas e proteção contra metas inalcançáveis.
- Aceita vírgula decimal (ex.: `0,5`).

## Como executar

**Requisitos:** Python 3.9 ou superior.

1. Clone o repositório:

   ```bash
   git clone https://github.com/YuriYairo/Projeto-1-Explorando-PA-e-PG.git
   cd Projeto-1-Explorando-PA-e-PG
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

Entrada: primeiro termo `5`, razão `3`, quantidade `6`.

```
PA gerada:
5, 8, 11, 14, 17, 20

Último termo: 20
Soma dos termos: 75
```

### Gerar sequência: PG

Entrada: primeiro termo `2`, razão `3`, quantidade `5`.

```
PG gerada:
2, 6, 18, 54, 162

Último termo: 162
Soma dos termos: 242
```

### Alcançar meta: PG

Entrada: primeiro termo `2`, razão `2`, meta `1000`.

```
São necessários 9 termos.
Soma obtida: 1022
```

## Explicação do código, passo a passo

O arquivo `codigo_pa_pg.py` é dividido em três partes: **lógica** (os cálculos), **formatação** (leitura e exibição de números) e **interface** (a janela). A lógica não depende da interface, então pode ser testada sozinha.

### Passo 1: importação e configurações iniciais

```python
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

LIMITE_TERMOS = 500
LIMITE_META = 100_000
```

- Importa o `customtkinter` com o apelido `ctk`.
- Define o tema escuro e a cor azul para os botões.
- `LIMITE_TERMOS` limita a quantidade de termos no modo *Gerar sequência*, para a janela não travar.
- `LIMITE_META` é a proteção do modo *Alcançar meta*: se após 100.000 termos a soma não ultrapassar a meta, o programa avisa que ela é inalcançável (evita um laço infinito).

### Passo 2: calcular o próximo termo

```python
def proximo_termo(tipo, termo, razao):
    if tipo == "PA":
        return termo + razao
    return termo * razao
```

Aqui está a **única diferença** entre PA e PG no algoritmo:

| Tipo | Regra | Exemplo (a₁ = 2, razão = 3) |
|---|---|---|
| PA | soma a razão | 2 → 5 → 8 → 11 |
| PG | multiplica pela razão | 2 → 6 → 18 → 54 |

### Passo 3: gerar a sequência termo a termo

```python
def gerar_sequencia(tipo, a1, razao, n):
    termo = a1
    soma = 0
    sequencia = []
    for _ in range(n):
        sequencia.append(termo)
        soma = soma + termo
        termo = proximo_termo(tipo, termo, razao)
    return sequencia, soma
```

Como funciona:

1. `termo` começa com o primeiro termo (`a1`).
2. `soma` começa em `0` (é o **acumulador**).
3. `sequencia` começa como uma lista vazia.
4. O laço `for` repete `n` vezes. Em cada volta:
   - guarda o termo atual na lista;
   - soma o termo ao acumulador;
   - calcula o próximo termo.
5. Ao final, devolve a lista e a soma.

**Teste de mesa** (PA com a₁ = 5, r = 3, n = 6):

| Volta | Termo adicionado | Soma | Próximo termo |
|---|---|---|---|
| 1 | 5 | 5 | 8 |
| 2 | 8 | 13 | 11 |
| 3 | 11 | 24 | 14 |
| 4 | 14 | 38 | 17 |
| 5 | 17 | 55 | 20 |
| 6 | 20 | 75 | 23 (descartado) |

### Passo 4: descobrir quantos termos são necessários (Etapa 6)

```python
def termos_ate_meta(tipo, a1, razao, meta):
    termo = a1
    soma = 0
    quantidade = 0
    while True:
        soma = soma + termo
        quantidade = quantidade + 1
        if soma > meta:
            return quantidade, soma, termo
        if quantidade >= LIMITE_META:
            return None
        termo = proximo_termo(tipo, termo, razao)
```

Aqui o número de termos **não é informado**, então usamos `while` em vez de `for`. A cada volta:

1. soma o termo atual e conta mais um termo;
2. se a soma **ultrapassou** a meta (`soma > meta`), para e devolve a quantidade, a soma e o último termo;
3. se chegou ao limite de segurança, devolve `None` (meta inalcançável);
4. senão, calcula o próximo termo e repete.

Exemplo do enunciado (PG, a₁ = 2, q = 2, meta = 1000): as somas são 2, 6, 14, 30, 62, 126, 254, 510 e **1022**. Na 9ª volta passa de 1000, então o resultado é 9 termos.

### Passo 5: verificar com as fórmulas prontas

```python
def soma_formula(tipo, a1, razao, n, ultimo):
    if tipo == "PA":
        return n * (a1 + ultimo) / 2
    if razao == 1:
        return a1 * n
    return a1 * (razao ** n - 1) / (razao - 1)
```

As fórmulas **não** produzem os resultados. Elas só conferem o que o laço calculou:

- **PA:** Sₙ = n · (a₁ + aₙ) / 2
- **PG:** Sₙ = a₁ · (qⁿ − 1) / (q − 1), para q ≠ 1
- Caso especial: se q = 1, todos os termos são iguais, então Sₙ = a₁ · n.

### Passo 6: ler e formatar números

```python
def ler_numero(texto):
    texto = texto.strip().replace(",", ".")
    ...
```

- Remove espaços e troca vírgula por ponto (assim `0,5` funciona).
- Se o campo estiver vazio ou o texto não for número, gera um erro (`ValueError`) que a interface trata.
- Devolve número inteiro quando possível (`5`) e decimal quando necessário (`0.5`).

```python
def formatar(valor):
    ...
```

- Mostra `20` em vez de `20.0` e usa vírgula nos decimais (`0,5`).

### Passo 7: construir a janela (classe `App`)

A classe `App` herda de `ctk.CTk` (a janela principal). No `__init__`, ela monta, de cima para baixo:

1. o título **PA & PG LAB** e o subtítulo;
2. um cartão (`CTkFrame`) com cantos arredondados contendo:
   - o botão segmentado de **modo** (*Gerar sequência* / *Alcançar meta*);
   - o botão segmentado de **tipo** (PA / PG);
   - os três campos de entrada: primeiro termo, razão e quantidade (ou meta);
   - o botão principal;
3. um aviso em vermelho para mensagens de erro;
4. uma caixa de texto (`CTkTextbox`) para mostrar o resultado.

Métodos auxiliares:

| Método | O que faz |
|---|---|
| `criar_campo` | Cria um rótulo + campo de entrada, para não repetir código três vezes. |
| `atualizar_rotulos` | Troca os textos conforme a escolha: razão **r** (PA) ou **q** (PG); "Quantidade de termos" ou "Meta". |
| `mostrar` | Escreve o resultado na caixa de texto. |
| `erro` | Limpa o resultado e mostra a mensagem de erro em vermelho. |

### Passo 8: o que acontece ao clicar no botão

O método `calcular` é chamado e segue este caminho:

1. limpa o aviso de erro;
2. descobre se o tipo escolhido é PA ou PG;
3. lê os três campos com `ler_numero` (se algum for inválido, mostra o erro e para);
4. chama `modo_gerar` ou `modo_meta`, conforme o modo escolhido.

**`modo_gerar`**

1. confere se a quantidade é inteira, maior que zero e no máximo 500;
2. chama `gerar_sequencia`;
3. compara a soma do laço com `soma_formula` e escolhe a mensagem ✔ ou ✘;
4. mostra a sequência, o último termo, a soma e a verificação.

**`modo_meta`**

1. chama `termos_ate_meta`;
2. se devolver `None`, mostra "Meta inalcançável";
3. senão, mostra a quantidade de termos, a soma obtida, o último termo e a meta.

### Passo 9: iniciar o programa

```python
if __name__ == "__main__":
    App().mainloop()
```

Cria a janela e a mantém aberta, esperando as ações do usuário. A condição `__name__ == "__main__"` garante que a janela só abre quando o arquivo é executado diretamente.

## Testes realizados

| Teste | Valores | Sequência | Soma (programa) | Soma (fórmula) |
|---|---|---|---|---|
| PA crescente | a₁ = 5, r = 3, n = 6 | 5, 8, 11, 14, 17, 20 | 75 | 75 |
| PA decrescente | a₁ = 20, r = −4, n = 6 | 20, 16, 12, 8, 4, 0 | 60 | 60 |
| PG crescente | a₁ = 2, q = 3, n = 5 | 2, 6, 18, 54, 162 | 242 | 242 |
| PG decrescente | a₁ = 64, q = 0,5, n = 6 | 64, 32, 16, 8, 4, 2 | 126 | 126 |
| Meta (PG) | a₁ = 2, q = 2, meta = 1000 | n = 9 termos | 1022 | — |

## Tecnologias

- Python
- customTkinter

---

Desenvolvido por **Matheus Yuri**, **Lucas Henrique** e **Vinicius Fernandes** (2026).
