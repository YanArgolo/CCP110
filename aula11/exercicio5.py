def eh_anagrama (palavra1, palavra2):
    dicionario1 = {}
    for letra in palavra1:
        if letra in dicionario1:
            dicionario1[letra] += 1
        else:
            dicionario1[letra] = 1

    dicionario2 = {}
    for letra in palavra2:
        if letra in dicionario2:
            dicionario2[letra] += 1
        else:
            dicionario2[letra] = 1

    return dicionario1 == dicionario2

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

print(eh_anagrama(palavra1, palavra2))