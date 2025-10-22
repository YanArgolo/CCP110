from random import randint

def lancarDados():
    return randint(1,6) + randint(1,6)

lista = []

for _ in range(1000):
    lista.append(lancarDados())

dicionario = {}
print(lista)

for numero in lista:
    if numero in dicionario:
        dicionario[numero] = dicionario[numero] + 1
    else:
        dicionario[numero] = 1

dicionario = dict(sorted(dicionario.items()))
print()
print(dicionario)

print()
for chave, valor in dicionario.items():
    print(f"{chave} : {valor /1000:.2%}")