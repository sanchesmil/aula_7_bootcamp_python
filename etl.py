import csv

def ler_csv(nome_do_arquivo:str)->list[dict]:
    """ Função que lê um arquivo csv e retorna uma lista de dicionários."""

    with open(nome_do_arquivo, mode='r', encoding='utf-8') as arquivo:
        reader = csv.DictReader(arquivo)
        
        return list(reader)


def excluir_produtos_nao_entregues(dados:list[dict])->list[dict]:
    """Função que filtra os produtos que não foram entregues."""

    lista_entregues = [dado for dado in dados if dado['entregue'] == 'True']
    return lista_entregues

def soma_valores_dos_produtos(dados:list[dict])->float:
    """ Função que soma os valores dos produtos informados."""
    return sum(float(dado['price']) for dado in dados)
