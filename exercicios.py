"""Calcular Média de Valores em uma Lista"""

# def media_valores(numeros:list[float])->float:
#     return sum(numeros)/len(numeros)

# lista_numeros = [20.4,10.1,3,99.9,18.5,45.6]
# print(media_valores(lista_numeros))

"""Filtrar Dados Acima de um Limite"""

# def filtrar_acima_de(dados:list[float], limite:float)->list[float]:
#     dados_filtrados = [valor for valor in dados if valor > limite ]
#     return dados_filtrados

# lista_numeros = [20.4,10.1,3,99.9,18.5,45.6]
# limite = 30.5;
# print(filtrar_acima_de(lista_numeros, limite))

"""Contar Valores Únicos em uma Lista"""

# def contar_valores_unicos(valores:list[int])->int:
#     return len(set(valores))

# valores = [2,54,67,12,34,33,2,54,2]
# print(contar_valores_unicos(valores))

"""Converter Celsius para Fahrenheit em uma Lista"""

# def converter_celsius_to_fahreinheit(medicoes:list[float])->list[float]:
#     return [(temp * (9/5) + 32) for temp in medicoes]

# medicoes_celsius = [20.4,10.1,3,99.9,18.5,45.6]
# print(converter_celsius_to_fahreinheit(medicoes_celsius))

"""Calcular Desvio Padrão de uma Lista"""

# def calcular_desvio_padrao(valores:list[float])->float:
#     media = sum(valores)/len(valores)

#     variancia = sum((valor - media) ** 2 for valor in valores) / len(valores)

#     desvio_padrao = variancia ** 0.5 

#     return desvio_padrao

# valores = [2,54,67,12,34,33,2,54,2]
# print(calcular_desvio_padrao(valores))

"""Encontrar Valores Ausentes em uma Sequência"""

def encontrar_valores_ausentes(sequencia:list[int])->list[int]:
    completo = set(range(min(sequencia),max(sequencia)+1))
    return [valor for valor in completo if valor not in sequencia]
    # return list(completo - set(sequencia))

sequencia = [2,5,6,8,12]
print(encontrar_valores_ausentes(sequencia))