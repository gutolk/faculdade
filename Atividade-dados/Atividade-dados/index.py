import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# ETAPA 1 - Seleção dos Dados
# ============================================================

df = pd.read_csv("dataset_atividade_kdd.csv")

df = df[["id", "idade", "salario", "sexo", "renda_extra",
         "tempo_emprego", "setor", "nacionalidade", "status_emprego"]]

print("=== ETAPA 1 - Seleção dos Dados ===")
print(df.head())

# ============================================================
# ETAPA 2 - Pré-processamento e Limpeza
# ============================================================

print("\n=== ETAPA 2 - Pré-processamento e Limpeza ===")
print("Valores nulos antes da limpeza:")
print(df.isnull().sum())

df["idade"] = pd.to_numeric(df["idade"], errors="coerce")
df["salario"] = pd.to_numeric(df["salario"], errors="coerce")
df["tempo_emprego"] = pd.to_numeric(df["tempo_emprego"], errors="coerce")

df = df.dropna(subset=["idade", "salario", "tempo_emprego", "setor"])

df["renda_extra"] = df["renda_extra"].fillna(df["renda_extra"].median())

df = df.drop_duplicates()

df = df[df["status_emprego"].isin(["Empregado", "Desempregado"])]

print("\nValores nulos após limpeza:")
print(df.isnull().sum())
print(df.info())

# ============================================================
# ETAPA 3 - Transformação dos Dados
# ============================================================

print("\n=== ETAPA 3 - Transformação dos Dados ===")

df["renda_total"] = df["salario"] + df["renda_extra"]

print(df[["salario", "renda_extra", "renda_total"]].head())

# ============================================================
# ETAPA 4 - Mineração de Dados
# ============================================================

print("\n=== ETAPA 4 - Mineração de Dados ===")

print("-- Média --")
print(f"Média de idade: {df['idade'].mean():.2f}")
print(f"Média de salário: {df['salario'].mean():.2f}")
print(f"Média de renda total: {df['renda_total'].mean():.2f}")

print("\n-- Mediana --")
print(f"Mediana de idade: {df['idade'].median():.2f}")
print(f"Mediana de salário: {df['salario'].median():.2f}")

print("\n-- Moda --")
print(f"Moda de sexo: {df['sexo'].mode()[0]}")
print(f"Moda de setor: {df['setor'].mode()[0]}")

print("\n-- Desvio Padrão --")
print(f"Desvio padrão do salário: {df['salario'].std():.2f}")
print(f"Desvio padrão da idade: {df['idade'].std():.2f}")

print("\n-- Variância --")
print(f"Variância do salário: {df['salario'].var():.2f}")

print("\n-- Amplitude --")
print(f"Amplitude do salário: {df['salario'].max() - df['salario'].min():.2f}")
print(f"Amplitude da idade: {df['idade'].max() - df['idade'].min():.0f}")

print("\n-- Correlação de Pearson (salário x tempo_emprego) --")
correlacao = df[["salario", "tempo_emprego", "idade", "renda_total"]].corr(method="pearson")
print(correlacao)

print("\n-- Distribuição por Setor --")
print(df["setor"].value_counts())

print("\n-- Distribuição por Status de Emprego --")
print(df["status_emprego"].value_counts())

print("\n-- Salário médio por Setor --")
print(df.groupby("setor")["salario"].mean().sort_values(ascending=False))

print("\n-- Salário médio por Sexo --")
print(df.groupby("sexo")["salario"].mean())

# ============================================================
# ETAPA 5 - Interpretação e Avaliação
# ============================================================

print("\n=== ETAPA 5 - Interpretação e Avaliação ===")

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("KDD - Análise do Dataset de Empregados")

axs[0, 0].scatter(df["tempo_emprego"], df["salario"], alpha=0.4)
axs[0, 0].set_xlabel("Tempo de Emprego (anos)")
axs[0, 0].set_ylabel("Salário")
axs[0, 0].set_title("Salário x Tempo de Emprego")

salario_setor = df.groupby("setor")["salario"].mean().sort_values()
axs[0, 1].barh(salario_setor.index, salario_setor.values)
axs[0, 1].set_xlabel("Salário Médio")
axs[0, 1].set_title("Salário Médio por Setor")

status_counts = df["status_emprego"].value_counts()
axs[1, 0].pie(status_counts, labels=status_counts.index, autopct="%1.1f%%")
axs[1, 0].set_title("Distribuição por Status de Emprego")

axs[1, 1].scatter(df["idade"], df["salario"], alpha=0.4)
axs[1, 1].set_xlabel("Idade")
axs[1, 1].set_ylabel("Salário")
axs[1, 1].set_title("Salário x Idade")

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/kdd_graficos.png")
plt.show()

print("\nGráfico salvo como kdd_graficos.png")

# ============================================================
# RELATÓRIO DE CONCLUSÕES
# ============================================================

print("""
============================================================
RELATÓRIO DE CONCLUSÕES
============================================================

1. SELEÇÃO
   O dataset contém 10 colunas. A coluna 'coluna_irrelevante' foi
   removida por não contribuir com a análise.

2. PRÉ-PROCESSAMENTO
   A coluna 'renda_extra' possuía valores nulos, preenchidos com
   a mediana para não distorcer a distribuição.
   Não foram encontradas linhas duplicadas.

3. TRANSFORMAÇÃO
   Foi criada a variável 'renda_total' (salario + renda_extra)
   para representar a renda anual completa do indivíduo.

4. MINERAÇÃO
   - A correlação de Pearson entre salário e tempo de emprego é
     baixa, indicando que o tempo no emprego não é o principal
     fator para salários mais altos.
   - O setor de Tecnologia apresenta o maior salário médio,
     seguido de Saúde, Educação e Varejo.
   - Não há diferença salarial expressiva entre homens e mulheres
     no dataset.
   - A maioria dos indivíduos está empregada.

5. INTERPRETAÇÃO
   Os dados indicam que o salário está mais relacionado ao setor
   de atuação do que ao tempo de emprego ou à idade. Profissionais
   de Tecnologia tendem a ganhar mais. A renda extra é uma variável
   complementar com distribuição uniforme entre os indivíduos.
============================================================
""")