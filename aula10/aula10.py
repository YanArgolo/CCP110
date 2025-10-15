# from random import randint, random
# # inteiros = []
# # for i in range(10):
# #     inteiros.append(randint(1, 100))
# # print(inteiros)
# inteiros = [randint(1, 100) for i in range(10)]
# print(inteiros)

# reais = [random () * 100 for i in range(5)]
# print(reais)

# strings = ["maçã", "banana", "uva", "pera", "kiwi", "laranja", "melão"]
# print(strings)

# completa = [inteiros, reais, strings]
# print(completa)

# del inteiros
# del reais
# del strings
# print(completa)
# # reais = []
# # strings = ["maçã", "banana", "uva", "pera", "kiwi", "laranja", "melão"]
# # completa = [inteiros, reais, strings]

n = []

for num_linha in range(10):
    linha = []
    for num_coluna in range(15):
        linha.append(num_linha + num_coluna)
        n.append(linha)
        