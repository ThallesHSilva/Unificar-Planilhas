import pandas as pd
import os

# Coloque caimnho da pasta aonde estão os arquivos
dir_path = "Caminho da pasta"

dfs = []

# Caso esteja em csv, você precisará trocar o .xlsx por .csv
for planilha in os.listdir(dir_path):
    if planilha.endswith('.xlsx') or planilha.endswith('.xls'):
        df = pd.read_excel(os.path.join(dir_path, planilha))
        dfs.append(df)

df_concat = pd.concat(dfs, ignore_index=True)

# renomeie o nome do arquivo que irá retornar
df_concat.to_excel('PlanilhaUnificada.xlsx', index=False)
