import pandas as pd
import matplotlib.pyplot as plt

#leitura dos dados tratados

df=pd.read_csv("data/processed/dados_limpos.csv")
print(df.head())

#calculando as frequencias de cada variavel

#faixa_etaria
#absoluta
frequencia_etaria=df["faixa_etaria"].value_counts()
#criando grafico apartir disso
frequencia_etaria.plot(kind="bar")
#plot esta mandando o pandas desenhar um grafico
#kind=var-> define o grafico de barras
#nisso, adicionar o titulo
plt.title("Distribuição da faixa etaria")
#nome do eixo X do grafico
plt.xlabel("Faixa etaria")
#nome do eixo y
plt.ylabel("quantidade de pessoas")
#ajustando a visualizacao
plt.xticks(rotation=0)
#como exibir o grafico

#vai abrir a janela do grafico

#obs: na tabela era preciso ler numeros, no grafico o cerebro percebe de imediato, isso é poder da visualizacao de dados

#em projetos profissionais fazemos graficos para cada variavel
#pq cada variavel ela conta uma parte da historia dos dados


#A DISTRIBUIÇÃO ETARIA DEMONSTROU PREDOMINANCIA DE PARTICIPANTES ENTRE 18-27 ANOS,REPRESENTANDO MAIS DE 70% DA AMOSTRA(e abaixo o grafico)

#o fluxo profissional, é:
#1-calcular frequencia
#2-gerar grafico
#3-personalizar
#4-salvar imagem
#5-exibir
#6-interpretar


#curso
frequencia_curso=df["curso"].value_counts()
plt.figure(figsize=(8,5))
plt.title("Distribuição dos cursos")
plt.xlabel("cursos")
plt.ylabel("quantidade de pessoas")
plt.xticks(rotation=0)
frequencia_curso.plot(kind="bar")
plt.savefig("assets/graphs/grafico_curso.png")

#media_estudos
frequencia_estudos=df["media_estudos"].value_counts()
plt.figure(figsize=(8,5))
frequencia_estudos.plot(kind="bar")
plt.title("Media de estudos por dia")
plt.xlabel("Tempo de estudo")
plt.ylabel("quantidade de pessoas")
plt.xticks(rotation=0)
plt.savefig("assets/graphs/grafico_curso.png")
#faixa_altura
frequencia_altura=df["faixa_altura"].value_counts()
plt.figure(figsize=(8,5))
frequencia_altura.plot(kind="bar")
plt.title("Distribuição da faixa de altura")
plt.xlabel("faixa de altura")
plt.ylabel("quantidade de pessoas")

plt.xticks(rotation=0)
plt.savefig("assets/graphs/grafico_faixa_altura.png")
plt.show()
plt.close()

