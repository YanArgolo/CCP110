from random import randint
def gerar_numeros():
    with open("numeros.txt" , "w") as numeros:
        for _ in range(100):
            numeros.write(f"randint(1,100)\n")

def ler_numeros():
    with open("numeros.txt" , "r") as numeros:
        conteudo = numeros.readlines()

    num= []
    for linha in conteudo:
        num.append(int(linha.strip()))
    return num

def remover_repetidos(lista):
    return list(set(lista))


def salvar_numeros_unicos(numeros_unicos):
    with open("numeros_unicos.txt", "w") as arquivo:
        for numero in numeros_unicos:
            arquivo.write(f"{numero}\n")


gerar_numeros()
numeros_lidos = ler_numeros()
print(f"Numeros lidos do arquivo: {numeros_lidos}")
numeros_unicos = remover_repetidos(numeros_lidos)
print(f"numeros_unicos")

