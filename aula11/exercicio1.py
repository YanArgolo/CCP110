# dicionario = {
#     1: "um",
#     2:"dois",
#     3: "tres",
#     4: "quatro",
# }   
# print(list(dicionario.items()))

# for chave, valor in dicionario.items():
#     print(f"chave : {chave}, Valor: {valor}")

dicionario = {
    'alpha' : 1,
    'bravo': 2,
    'charlie': 1,
    'delta': 3,
    'echo': 1,
}
def procuraChave(dicionario, valorProcurado):
    lista= []
    for chave, valor in dicionario.items():
        if valor == valorProcurado:
            lista.append(chave)
    return lista
print (procuraChave(dicionario, 1))
