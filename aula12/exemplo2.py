with open ("pares.txt", "r") as pares, open ("multiplos.txt", "w") as multiplos:
    for linha in pares.readlines():
        print(linha.strip())
        valor = int(linha.strip())
        if valor % 4 ==0:
            multiplos.write(linha)