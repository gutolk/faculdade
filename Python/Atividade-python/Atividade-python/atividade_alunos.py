import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("Dados_alunos.xlsx")

print("INFORMACOES DO DATAFRAME")
print(df.info())

print("\nPRIMEIRAS LINHAS")
print(df.head())

df["trabalha?"] = df["trabalha?"].replace("Infelizmente", "sim")
df["trabalha?"] = df["trabalha?"].replace("Pra caramba", "sim")
df["esporte preferido"] = df["esporte preferido"].replace("Futebol", "futebol")
df["estilo musical"] = df["estilo musical"].replace("Pagode", "pagode")
df["estilo musical"] = df["estilo musical"].replace("Sertanejo", "sertanejo")
df["estilo musical"] = df["estilo musical"].replace("sertanejo ", "sertanejo")
df["Jogos digitais?"] = df["Jogos digitais?"].replace("Sim", "sim")
df["Gosta filme?"] = df["Gosta filme?"].replace("Sim", "sim")
df["Gosta série?"] = df["Gosta série?"].replace("Sim", "sim")

map_genero = {"Masculino": 1, "Feminino": 2}
map_linguagem = {"Python": 1, "Java": 2, "C++": 3, "C#": 4, "SQL": 5}
map_esporte = {
    "nenhum": 1,
    "jogo da velha": 2,
    "volei": 3,
    "futebol": 4,
    "Musculação": 5,
    "Jiujitsu": 6,
}
map_trabalha = {"não": 0, "sim": 1}
map_filme = {"não": 0, "um pouco": 1, "sim": 2}
map_serie = {"não": 0, "não muito": 1, "sim": 2}
map_musica = {
    "rock": 1,
    "pagode": 2,
    "geek": 3,
    "heavy metal": 4,
    "Hip hop": 5,
    "sertanejo": 6,
    "Rap": 7,
    "Louvor": 8,
    "Synthwave": 9,
    "Black Metal": 10,
}
map_jogos = {"não": 0, "sim": 1}

df["genero_num"] = df["genero"].map(map_genero)
df["linguagem_num"] = df["linguagem de programação preferida"].map(map_linguagem)
df["esporte_num"] = df["esporte preferido"].map(map_esporte)
df["trabalha_num"] = df["trabalha?"].map(map_trabalha)
df["filme_num"] = df["Gosta filme?"].map(map_filme)
df["serie_num"] = df["Gosta série?"].map(map_serie)
df["musica_num"] = df["estilo musical"].map(map_musica)
df["jogos_num"] = df["Jogos digitais?"].map(map_jogos)

df["horas de sono"] = pd.to_numeric(df["horas de sono"], errors="coerce")


print("\nMEDIA")
print(df[["idade", "horas de sono", "horas de estudo", "horas uso celular"]].mean())

print("\nMEDIANA")
print(df[["idade", "horas de sono", "horas de estudo", "horas uso celular"]].median())

print("\nMODA")
print(df[["idade", "horas de sono", "horas de estudo", "horas uso celular"]].mode())

print("\nDESVIO PADRAO")
print(df[["idade", "horas de sono", "horas de estudo", "horas uso celular"]].std())

print("\nAMPLITUDE")
print(df[["idade", "horas de sono", "horas de estudo", "horas uso celular"]].max() - df[["idade", "horas de sono", "horas de estudo", "horas uso celular"]].min())


print("\nCORRELACAO")
print(
    df[
        [
            "idade",
            "horas de sono",
            "horas de estudo",
            "horas uso celular",
            "genero_num",
            "linguagem_num",
            "esporte_num",
            "trabalha_num",
            "filme_num",
            "serie_num",
            "musica_num",
            "jogos_num",
        ]
    ].corr()
)


plt.hist(df["idade"].dropna(), bins=5)
plt.title("Histograma de idade")
plt.xlabel("Idade")
plt.ylabel("Frequencia")
plt.show()

plt.hist(df["horas de sono"].dropna(), bins=5)
plt.title("Histograma de horas de sono")
plt.xlabel("Horas de sono")
plt.ylabel("Frequencia")
plt.show()

plt.hist(df["horas de estudo"].dropna(), bins=5)
plt.title("Histograma de horas de estudo")
plt.xlabel("Horas de estudo")
plt.ylabel("Frequencia")
plt.show()

plt.hist(df["horas uso celular"].dropna(), bins=5)
plt.title("Histograma de horas uso celular")
plt.xlabel("Horas uso celular")
plt.ylabel("Frequencia")
plt.show()


# PERGUNTAS DA ATIVIDADE
# 1. Voce faz parte da media de cada um dos atributos analisados?
# Resposta: SIM, estou na media de idade, horas de sono e horas de estudo, celular uso um pouco mais.
#
# 2. Voce e a media ou um ponto fora da curva?
# Resposta: Sou a media em idade, horas de sono e horas de estudo, mas sou um pouco fora da curva em horas de uso do celular, pois uso um pouco mais do que a media.
#
# 3. Observando cada uma das variaveis, o que voce infere sobre seus colegas?
# Resposta: A maioria dos meus colegas tem 20 anos, dormem em media 6 horas por noite, estudam em media 3 horas por dia e usam o celular em media 4 horas por dia.
#
# 4. O que a turma gosta e o que desgosta?
# Resposta: futebol, gostam de filmes, series, musica, jogos e a maioria gosta de java.
#
# 5. Todo mundo tem os mesmos gostos, ou existem grupos com preferencias diferentes?
# Resposta: Existem grupos com preferencias diferentes, como os que gostam de rock e os que preferem sertanejo.
#
# 6. Qual o perfil geral dos alunos?
# Resposta o perfil geral dos alunos é de jovens de 20 anos, que dormem em media 6 horas por noite, estudam em media 3 horas por dia e usam o celular em media 4 horas por dia. Eles gostam de futebol, filmes, series, musica e jogos, com uma preferencia maior por java como linguagem de programação.
#
# 7. A turma estuda muito ou pouco?
# Resposta: em média 3 horas, moderado.
#
# 8. A turma dorme bem?
# Resposta: A maioria dos alunos dorme bem, com uma media de 6 horas por noite.
#
# 9. Quem estuda muito dorme bem?
# Resposta: Não necessariamente, pois a correlação entre horas de estudo e horas de sono é baixa, indicando que não há uma relação forte entre esses dois atributos.
#
# 10. Existe correlacao entre atributos?
# Resposta: Sim. 
