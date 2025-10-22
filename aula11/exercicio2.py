from random import randint
lista = []
for i in range(100):
    lista.append(randint(0,20))

# lista = [randint(0, 20) for in range(100)]
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