# Bibliotecas
import pandas as pd 
from datetime import datetime, timedelta
import sys
import os
# Adiciona ao sys.path o diretório acima de `src`
sys.path.append(r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\06.ChequeEspecial\classes")
from query_executor import QueryExecutor



# Exemplo de uso
database = "inteligencia_credito_dados"
query_executor = QueryExecutor(database)

# # Executar e salvar as consultas
# query_executor.execute_query_to_parquet(
#     r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\06.ChequeEspecial\Data\sql\conta_corrente.sql",
#     r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\06.ChequeEspecial\Data\data_parquet\conta_corrente")

# Executar e salvar as consultas de dados do PA 
query_executor.execute_query_to_parquet(
    r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\06.ChequeEspecial\Data\sql\dados_pa.sql",
    r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\06.ChequeEspecial\Data\data_parquet\dados_pa.parquet")