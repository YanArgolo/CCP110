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

def gerar_matriz(n_linhas, n_colunas):
m= []

for num_linha in range(10):
    linha = []
    for num_coluna in range(15):
        linha.append(num_linha + num_coluna)
        m.append(linha)

print(m)
print(len(m[0]))

for linha in range(len(m)):
    for coluna in range (len(m[linha])):
        print(f"{m[linha][coluna]: 4}", end="")
    print()

print("--------------")
for linha in range(len(m)):
    print(m[linha[0]])

for linha in m:
    print(linha[0])a