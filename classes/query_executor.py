import pandas as pd
import sys
import os

# Adiciona ao sys.path o diretório onde está o database_executor.py
sys.path.append(r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\06.ChequeEspecial\classes")
from database_executor import DatabaseQueryExecutor 
class QueryExecutor:
    def __init__(self, database):
        self.database = database

    def execute_query_to_parquet(self, query_file_path, output_path):
        # Lê o conteúdo do arquivo SQL
        with open(query_file_path, 'r') as file:
            query = file.read()
        # Criação de uma instância da classe DatabaseQueryExecutor com a consulta
        db_executor = DatabaseQueryExecutor(self.database, query)
        # Executa a consulta
        resultado = db_executor.execute_query()
        # Salva o resultado em um arquivo Parquet
        resultado.to_parquet(output_path)