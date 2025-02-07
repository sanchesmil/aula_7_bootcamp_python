from etl import ler_csv, excluir_produtos_nao_entregues, soma_valores_dos_produtos

# Executanto o ETL 
path_arquivo = 'vendas.csv'
produtos = ler_csv(path_arquivo)
produtos_entregues = excluir_produtos_nao_entregues(produtos)
soma_valores = soma_valores_dos_produtos(produtos_entregues)
print(soma_valores)