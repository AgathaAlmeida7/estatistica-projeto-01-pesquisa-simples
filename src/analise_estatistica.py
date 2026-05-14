import pandas as pd

#leitura do dataset tratado

df= pd.read_csv("data/processed/dados_limpos.csv")

#visualizar primeiras linhas

print(df.head())

#fa-> contagem do numero de vezes que um determinado valor aparece em um conj.dados

#frequencia absoluta da faixa etaria

freq_abs= df["faixa_etaria"].value_counts()
print("\n Frequencia absoluta- faixa etaria: ")
print(freq_abs)


#FREQUENCIA RELATIVA DA FAIXA ETARIA

freq_rel= df['faixa_etaria'].value_counts(normalize=True)
#em vez de contar, transformar em prop

print("\n Frequencia relativa - faixa etaria:")
print(freq_rel)

#fr-> varia sempre entre 0 e 1 
#convertendo contagem para distribuicao proporcional

#porcentagem geral 

porcetagem=freq_rel*100
print(porcetagem)

#criação da tabela estatistica

tabela_etaria=pd.DataFrame({
    "Frequencia absoluta":freq_abs,
    "Frequencia Relativa":freq_rel,
    "Porcentagem (%)":porcetagem.round(2)
})

print("\n Tabela estatistica- faixa etaria:")
print(tabela_etaria)


#curso

#fa-curso
freq_abs_curso=df["curso"].value_counts()
#fr-curso
freq_rel_curso=df["curso"].value_counts(normalize=True)
#porcentagem - curso
porcentagem_curso=freq_rel_curso*100

#tabela estatistica de curso
tabela_curso=pd.DataFrame({
    "Frequencia absoluta":freq_abs_curso,
    "Frequencia relativa":freq_rel_curso,
    "Porcetagem (%)":porcentagem_curso.round(2)
}
)
print("\n Tabela estatistica - curso:")
print(tabela_curso)

#frequencia absoluta de media_estudo
freq_abs_media_estudos=df["media_estudos"].value_counts()
#frequencia relativa
freq_rel_media_estudos=df["media_estudos"].value_counts(normalize=True)
#porcetagem-media_estudo
porcentagem_media_estudos=freq_rel_media_estudos*100

#tabela de media de estudos

tabela_media_estudos=pd.DataFrame({
    "Frequencia Absoluta":freq_abs_media_estudos,
    "Frequencia Relativa":freq_rel_media_estudos,
    "Porcentagem (%)":porcentagem_media_estudos.round(2)
})

print("\n Tabela Estatistica - Media_estudos:")
print(tabela_media_estudos)

#faixa altura
#frequencia absoluta
freq_abs_faixa_altura=df["faixa_altura"].value_counts()
#frequencia relativa
freq_rel_faixa_altura=df["faixa_altura"].value_counts(normalize=True)
#porcentagem 
porcentagem_faixa_altura=freq_rel_faixa_altura*100

#tabela da faixa altura

tabela_faixa_altura=pd.DataFrame({
    "Frequencia Absoluta":freq_abs_faixa_altura,
    "Frequencia Relativa": freq_rel_faixa_altura,
    "Porcentagem (%)":porcentagem_faixa_altura.round(2)
})

print("\n Tabela Estatistica -Faixa_altura:")
print(tabela_faixa_altura)











