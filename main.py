import os
import pandas as pd

# Lista dos arquivos
arquivos = [arq for arq in os.listdir('./Dados') if arq.lower().endswith(".csv")]

# comb = pd.DataFrame({'Regiao - Sigla':[],'Estado - Sigla':[],'Municipio':[],'Revenda':[],'CNPJ da Revenda':[],'Nome da Rua':[],'Numero Rua':[],'Complemento':[],'Bairro':[],'Cep':[],'Produto':[],'Data da Coleta':[],'Valor de Venda':[],'Valor de Compra':[],'Unidade de Medida':[],'Bandeira':[]})

chunks = []
for arq in arquivos:
    df = pd.read_csv('.\Dados\\' + arq, sep=';', encoding='ISO-8859-1', chunksize=10000)
    for chunk in df:
        chunks.append(chunk)
comb = pd.concat(chunks)

comb.to_csv("combinado.csv", index=False, encoding='utf-8-sig')