# # Exercicio 2
# from math import inf
# T = []
# menor = inf
# for elemento in T:
#     if elemento < menor:
#         menor = elemento
# print(menor)

#   Exercicio 3
# lista = []
# for c in range(10):
#     n = int(input("Digite um numero: "))
#     lista.append(n)
# print(lista)
# maior= lista[0]
# indice_maior= 0
# for indice in range(len(lista)):
#     if lista[indice]>maior:
#         maior = lista[indice]
#         indice_maior = indice
# print(f"O maior valor é {maior} no indice {indice_maior}")

#   Exercicio 4
# lista = []
# for c in range(10):
#     n = int(input("Digite um numero: "))
#     lista.append(n)
# print(lista)

# soma_pares = 0
# for i in range(len(lista)):
#     if lista[i] %2 == 0:
#         soma_pares += lista[i]
# print(f'A soma dos elementos pares eh: {soma_pares}')

# soma_indice = 0
# for i in range(len(lista)):
#     if i %2 ==0:
#         soma_indice += lista[i]
# print(f"A soma dos indices pares eh: {soma_indice}")


#   Exercicio 5
# lista = []
# for i in range(5):
#     n = int(input("Digite um numero: "))
#     lista.append(n)
# print(lista)
# lista_reversa = lista[::-1] #:: serve para omitir o início e fim da lista
# print(lista_reversa)