import pandas as pd

#leitura dos dados brutos

df=pd.read_csv("data/raw/respostas.csv")

#visualizar primeiras linhas

print(df.head())

#o python leu o arquivo csv usando algo como pandas.read_csv()
#transformação/limpeza

#pode-se
#remover valores vazios
#corrigir nomes
#converter tipos
#tratar erros

#depois dessa etapa eu ja posso fazer analise
#fazer estatisticas, graficos,insights
#depois disso, eu posso ter uma saida
#mostrar na tela,salvar outro csv, criar dashboard,alimentar banco de dados, etc

#quando fala que se entrou em um pipeline,é que eu comecei  o fluxo de processamento de dados
#o csv virou parte de um  processo de manipulacao de dados

#os pipelines existem, porque empresas precisam de:

#automatizar processos
#evitar trabalho manual
#organizar fluxo de dados
#garantir qualidade dos dados
#gerar analises confiaveis

#ESSA BRANCH A FUNCAO DELA É:

#PREPARAR OS DADOS PARA QUE ELES POSSAM SER ANALISADOS CORRETAMENTE DEPOIS

#PQ ELES BRUTOS OCORRE:

#VEM BAGUNÇADOS
#POSSUEM NOMES RUINS
#POSSUEM INCONSISTENCIAS
#NAO ESTAO PADRONIZADOS

#inspeção dos dados_>exame/auditoria


#ETAPA DE INVESTIGAR OS DADOS ANTES DE LIMPAR

#VER INFORMAÇÕES GERAIS DOS DADOS

print("\nInformações gerais:")
print(df.info())

#O INFO()
#QUANTIDADE DE LINHAS
#QUANTIDADE DE COLUNAS
#TIPOS DE DADOS
#CAMPOS PREENCHIDOS
#CONSUMO DE MEMORIA

#AQUI SO PEGOU UMA PARTE


#AQUI IREMOS COMEÇAR A ENTENDER:
#ESTRUTURA DO DATASET
#NATUREZA DAS VARIAVEIS
#ORGANIZAÇÃO TABULAS


#MOSTRANDO O NOME DAS COLUNAS

print("\nColunas:")
print(df.columns)
#26 ENTRIES-> RESPOSTAS
#AQUI JA SE VER O TAMANHO DA AMOSTRA QUE É 26

#OS NOMES OFICIAIS DAS COLUNAS
#TEMOS A ENCONTRAR NOMES LONGOS E NAO PADRONIZADOS
#É ALGO NEGATIVO, POIS:

#TEM ESPAÇOS
#ACENTOS
#PERGUNTAS COMPLETAS
#É RUIM PARA ANALISE DE DADOS
#NISSO, IREMOS PRECISAR PADRONIZAR AS COLUNAS





#ISSO AQUI É IMPORTANTE PQ O FORMS
#CRIA:
#NOMES LONGOS
#NOMES RUINS
#ESPAÇOS
#ACENTOS
#EM PROJETOS PROFISSIONAIS NOMES DE COLUNAS PRECISAM SER PADRONIZADOS. ENTAO PRECISAMOS SABER COMO ELAS VIERAM

#VENDO SE TEM VALORES NULOS

print("\nValores nulos:")
print(df.isnull().sum())

#campos vazios
#respostas faltantes
#inconsistencias


#para rodar isso é : 
#python src/limpeza_dados.py
#e pqtem que ser assim? tentar entender isso aqui 


#AQUI FOI ENCERRADO A INTEGRIDADE DA AMOSTRA

#FASE NOVA: PADRONIZACAO DOS DADOS
#RENOMEAR COLUNAS
#REMOVER PROBLEMAS ESTRUTURAIS
#ORGANIZAR DATASET
#DADOS ORGANIZADOS VAI FACILITAR ANALISE DESCRITIVA

#ANTES DE ANALISAR DADOS, PRECISAMOS ORGANIZA-LOS CORRETAMENTE

#OBJETIVO DA PADRONIZAÇÃO:
#TRANSFORMAR COLUNAS DIFICEIS EM ALGO PROFISSIONAL
#EM PROJETOS PROFISSIONAIS NORMALMENTE USAMOS:
#MINUSCULAS
#UNDERSCORE_
#SEM ESPAÇO
#SEM ACENTOS
#NOMES CURTOS E CLAROS

#AS COLUNAS QUE TEMOS ATUALMENTE

#CARIMBO DE DATA/HORA
#QUAL A SUA FAIXA DE ETARIA
#QUAL A SUA FAIXA DE ALTURA
#QUAL O SEU CURSO
#QUAL A SUA MEDIA DE ESTUDOS POR DIA
#IREMOS DEIXAR OS NOMES PADRONIZADOS

#timestamp
#faixa_etaria
#faixa_altura
#curso
#media_estudos

#RENOMEANDO AS COLUNAS

df.columns=[
    "timestamp",
    "faixa_etaria",
    "faixa_altura",
    "curso",
    "media_estudos"
]
#pq essa estrutura?
#o q significa o df?
#pq o python src/limpeza_dados.py



#o pandas ta permitindo substituir os nomes das colunas diretamente
#a ordem aqui vai importar

#MOSTRANDO NA TELA AS NOVAS COLUNAS NOMEADAS

print("\nColunas padronizadas:")
print(df.columns)

#TRATAMENTO DO DATASET

#DECIDIR:
#MANTER TIMESTAMP OU REMOVER
#ANALISAR CATEGORIAS
#VERIFICAR CONSISTENCIA
#PREPARAR EXPORTACAO
#NISSO IREMOS TRANSFORMAR DADOS BRUTOS EM TRATADOS

#VAMOS AQUI SE "O DATASET JA ESTA PRONTO PARA ANALISE?"

#VER COLUNAS DESNECESSARIAS
#CONSISTENCIA
#ORGANIZACAO FINAL
#ESTRUTURA IDEAL

#TRATAMENTO ESTRUTURAL,MELHORAR A ESTRUTURA DO DATASET ANTES DA ANALISE. ESTAMOS PREPARANDO O TERRENO PARA A ESTATISTICA

#EM DATASETS DEVEM CONTER APENAS INFORMACOES UTEIS PARA O OBJETIVO ANALITICO, COLUNAS QUE NAO FIZEREM SENTIDO TEM QUE ANULAR

#ISSO AQUI É SELECAO DE VARIAVEIS(ESTATISTICA,CIENCIAS DE DADOS,MACHINE LEARNING)

#REMOVENDO COLUNA TIMESTAMP(desnecessaria)

df=df.drop(columns=["timestamp"])
#o panda pega o dataframe,remove a coluna timestamp,devolve o dataframe atualizado

print("\nDataset após remoção do timestamp:")
print(df.head())
#remocao de varaiveis irrevalantes
#nem toda variavel ccoletada precisa permanecer na analise
#mostrara as primeiras colunas novamente
#agora sem a coluna timestamp

#a gente ta fazendo isso so com as 5 colunas que foram selecionadas la no head,ajeitando isso ai do dataset, mas como a gente so ta ajeitando uma parte, nao estaria errado ta so ajeitando uma parte? ou so ta ajeitando uma parte pequena para a gente entende o basico,e mais pra frente é que vai ter a etapa de realmente resolver tudo? pq se a gente so ta fazendo isso em uma amostra , e as demais colunas que ainda falta?  ou n?e linhas nao vai ver? pq sao 27 linhas e pelo que vi 6 colunas? essa ta sendo a duvida gritante agora

#VERIFICACAO DAS CATEGORIAS(AS RESPOSTAS ESTAO CONSISTENTES?)
#por que em datasets reais podem existir problemas como:
#categorias escritas diferentes
#respostas duplicadas semanticamente 
#inconsistencias
#erros de digitacao

#se a resposta for ads,ADS,analise e desenvolvimento de sistemas. mesmo sendo a mesma resposta o pc interpreta de maneira diferente
#verificar valores unicos
#categorias existentes
#consistencia do dataset

#ANALISE CATEGORICA INICIAL

#INVESTIGANDO CADA VARIAVEL VENDO VALORES UNICOS

print("\n Valores únicos- faixa_etaria:")
print(df["faixa_etaria"].unique())
#.unique() -todos os valores diferentes existentes na coluna. nisso vamos ver consistencia,padronizacao,categorias reais

print("\n Valores unicos - faixa_altura:")
print(df["faixa_altura"].unique())

print("\n Valores unicos - curso:")
print(df["curso"].unique())

print("\n Valores unicos - media_estudos:")
print(df["media_estudos"].unique())


#corrigindo a padronização da categoria

df["curso"]=df["curso"].replace("outro","Outro")

#verificando o resultado

print("\nCursos após padronização:")
print(df["curso"].unique())



#adicionando a exportação dos dados limpos para a pasta processed

#exportando dataset tratado

df.to_csv("data/processed/dados_limpos.csv",index=False)

print("\n Dataset tratado exportado com sucesso!!!")


















