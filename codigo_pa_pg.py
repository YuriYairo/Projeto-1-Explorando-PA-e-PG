"""
PA & PG LAB
Projeto 1 - Explorando PA e PG

Funcionalidades:
  - Gerar uma PA ou PG termo a termo (laço de repetição + acumulador de soma)
  - Alcançar a meta: descobrir quantos termos são necessários para a soma
    ultrapassar um valor definido (Etapa 6)
  - Interface gráfica moderna em customTkinter (Etapa 7)

Instalação:  pip install customtkinter
Execução:    python pa_pg_lab.py
"""

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

LIMITE_TERMOS = 500        # máximo de termos no modo "Gerar sequência"
LIMITE_META = 100_000      # proteção contra metas inalcançáveis


# ======================= LÓGICA (sem interface) =======================

def proximo_termo(tipo, termo, razao):
    """PA: soma a razão. PG: multiplica pela razão."""
    if tipo == "PA":
        return termo + razao
    return termo * razao


def gerar_sequencia(tipo, a1, razao, n):
    """Constrói a sequência termo a termo e acumula a soma (Etapas 3 e 5)."""
    termo = a1
    soma = 0
    sequencia = []
    for _ in range(n):
        sequencia.append(termo)
        soma = soma + termo
        termo = proximo_termo(tipo, termo, razao)
    return sequencia, soma


def termos_ate_meta(tipo, a1, razao, meta):
    """
    Etapa 6: gera termos até a soma ULTRAPASSAR a meta (soma > meta).
    Retorna (quantidade, soma, ultimo_termo) ou None se não for alcançável.
    """
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


def soma_formula(tipo, a1, razao, n, ultimo):
    """Fórmulas prontas, usadas apenas para VERIFICAR o resultado (Etapa 4)."""
    if tipo == "PA":
        return n * (a1 + ultimo) / 2
    if razao == 1:
        return a1 * n
    return a1 * (razao ** n - 1) / (razao - 1)


# ======================= FORMATAÇÃO =======================

def ler_numero(texto):
    """Converte texto em número (aceita vírgula). Retorna int quando possível."""
    texto = texto.strip().replace(",", ".")
    if not texto:
        raise ValueError("campo vazio")
    valor = float(texto)
    if valor != valor or valor in (float("inf"), float("-inf")):
        raise ValueError("valor inválido")
    return int(valor) if valor.is_integer() and "." not in texto else valor


def formatar(valor):
    if isinstance(valor, float):
        if valor.is_integer():
            return str(int(valor))
        return f"{valor:.6g}".replace(".", ",")
    return str(valor)


# ======================= INTERFACE =======================

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PA & PG LAB")
        self.geometry("520x740")
        self.minsize(480, 700)

        ctk.CTkLabel(
            self, text="PA & PG LAB",
            font=ctk.CTkFont(size=30, weight="bold"),
        ).pack(pady=(26, 2))
        ctk.CTkLabel(
            self, text="Explorando Progressões Aritméticas e Geométricas",
            font=ctk.CTkFont(size=13), text_color="gray60",
        ).pack(pady=(0, 16))

        card = ctk.CTkFrame(self, corner_radius=16)
        card.pack(padx=28, fill="x")

        # Modo: gerar sequência ou alcançar meta
        self.modo = ctk.CTkSegmentedButton(
            card, values=["Gerar sequência", "Alcançar meta"],
            command=self.atualizar_rotulos, height=34,
        )
        self.modo.set("Gerar sequência")
        self.modo.pack(padx=20, pady=(20, 8), fill="x")

        # Tipo: PA ou PG
        self.tipo = ctk.CTkSegmentedButton(
            card, values=["Progressão Aritmética", "Progressão Geométrica"],
            command=self.atualizar_rotulos, height=34,
        )
        self.tipo.set("Progressão Aritmética")
        self.tipo.pack(padx=20, pady=(0, 10), fill="x")

        self.rot_a1, self.ent_a1 = self.criar_campo(
            card, "Primeiro termo (a₁)", "Ex.: 5")
        self.rot_razao, self.ent_razao = self.criar_campo(
            card, "Razão (r)", "Ex.: 3")
        self.rot_terceiro, self.ent_terceiro = self.criar_campo(
            card, "Quantidade de termos (n)", "Ex.: 6")

        self.botao = ctk.CTkButton(
            card, text="Gerar sequência", height=42, corner_radius=10,
            font=ctk.CTkFont(size=15, weight="bold"), command=self.calcular,
        )
        self.botao.pack(padx=20, pady=(16, 20), fill="x")

        self.aviso = ctk.CTkLabel(self, text="", text_color="#ff6b6b",
                                  font=ctk.CTkFont(size=13))
        self.aviso.pack(pady=(10, 0))

        self.saida = ctk.CTkTextbox(
            self, height=190, corner_radius=12, wrap="word",
            font=ctk.CTkFont(size=14), state="disabled",
        )
        self.saida.pack(padx=28, pady=(6, 24), fill="both", expand=True)

    def criar_campo(self, pai, titulo, dica):
        rotulo = ctk.CTkLabel(pai, text=titulo, anchor="w",
                              font=ctk.CTkFont(size=13))
        rotulo.pack(padx=22, pady=(6, 0), fill="x")
        entrada = ctk.CTkEntry(pai, placeholder_text=dica, height=36,
                               corner_radius=8)
        entrada.pack(padx=20, pady=(2, 4), fill="x")
        return rotulo, entrada

    def atualizar_rotulos(self, _=None):
        pa = self.tipo.get() == "Progressão Aritmética"
        self.rot_razao.configure(text="Razão (r)" if pa else "Razão (q)")
        if self.modo.get() == "Gerar sequência":
            self.rot_terceiro.configure(text="Quantidade de termos (n)")
            self.ent_terceiro.configure(placeholder_text="Ex.: 6")
            self.botao.configure(text="Gerar sequência")
        else:
            self.rot_terceiro.configure(text="Meta (a soma deve ultrapassá-la)")
            self.ent_terceiro.configure(placeholder_text="Ex.: 1000")
            self.botao.configure(text="Descobrir quantidade de termos")

    def mostrar(self, texto):
        self.saida.configure(state="normal")
        self.saida.delete("1.0", "end")
        self.saida.insert("1.0", texto)
        self.saida.configure(state="disabled")

    def erro(self, mensagem):
        self.mostrar("")
        self.aviso.configure(text=mensagem)

    def calcular(self):
        self.aviso.configure(text="")
        tipo = "PA" if self.tipo.get() == "Progressão Aritmética" else "PG"

        try:
            a1 = ler_numero(self.ent_a1.get())
            razao = ler_numero(self.ent_razao.get())
            terceiro = ler_numero(self.ent_terceiro.get())
        except ValueError:
            self.erro("Preencha todos os campos com números válidos.")
            return

        if self.modo.get() == "Gerar sequência":
            self.modo_gerar(tipo, a1, razao, terceiro)
        else:
            self.modo_meta(tipo, a1, razao, terceiro)

    def modo_gerar(self, tipo, a1, razao, n):
        if n != int(n):
            self.erro("A quantidade de termos deve ser um número inteiro.")
            return
        n = int(n)
        if n <= 0:
            self.erro("A quantidade deve ser maior que zero.")
            return
        if n > LIMITE_TERMOS:
            self.erro(f"Use no máximo {LIMITE_TERMOS} termos.")
            return

        sequencia, soma = gerar_sequencia(tipo, a1, razao, n)
        ultimo = sequencia[-1]

        try:
            esperado = soma_formula(tipo, a1, razao, n, ultimo)
            ok = abs(esperado - soma) <= 1e-9 * max(1, abs(soma))
            verif = "✔ Confere com a fórmula" if ok else "✘ Diverge da fórmula"
        except OverflowError:
            verif = "Número grande demais para verificar"

        nome = "PA gerada" if tipo == "PA" else "PG gerada"
        self.mostrar(
            f"{nome}:\n{', '.join(formatar(t) for t in sequencia)}\n\n"
            f"Último termo: {formatar(ultimo)}\n"
            f"Soma dos termos: {formatar(soma)}\n\n"
            f"{verif}"
        )

    def modo_meta(self, tipo, a1, razao, meta):
        resultado = termos_ate_meta(tipo, a1, razao, meta)
        if resultado is None:
            self.erro("Meta inalcançável: a soma não ultrapassa a meta "
                      "com esses valores.")
            return
        quantidade, soma, ultimo = resultado
        self.mostrar(
            f"São necessários {quantidade} termos.\n"
            f"Soma obtida: {formatar(soma)}\n"
            f"Último termo: {formatar(ultimo)}\n"
            f"Meta: {formatar(meta)}"
        )


if __name__ == "__main__":
    App().mainloop()