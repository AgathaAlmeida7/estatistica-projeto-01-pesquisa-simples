import pandas as pd

#leitura dos dados brutos

df=pd.read_csv("data/raw/respostas.csv")

#visualizar primeiras linhas

print(df.head())