
# cont1 = list(filter(filtra_intervalo_1, lista))

# contadores = [0, 0 , 0 , 0]

# while True:
#     num = int(input("Digite um numero positivo (ou negativo para sair): "))
#     if num < 0:
#         break
#     if 0 <= num <= 25:
#         contadores[0] += 1
#     elif 26 <= num <= 50:
#         contadores[1] += 1
#     elif 51 <= num <= 75:
#         contadores[2] += 1
#     elif 76 <= num <= 100:
#         contadores[3] += 1
    
# print(f"Números no intervalo [0-25]: {contadores[0]}")
# print(f"Números no intervalo [26-50]: {contadores[1]}")
# print(f"Números no intervalo [51-75]: {contadores[2]}")
# print(f"Números no intervalo [76-100]: {contadores[3]}")

# lista_votos = []
# while True:
#     voto = int(input("Vote no melhor sistema operacional para servidores (1-6) ou 0 para parar: "))
#     if voto == 0:
#         break
#     if 1 <= voto <= 6:
#         lista_votos.append(voto)
#     else:
#         print("Voto invalido. Tente Novamente")

# print(lista_votos)
# contadores = [0, 0, 0, 0, 0, 0]
# for voto in lista_votos:
#     contadores[voto]-1 += 1
#     if voto == 1:
#         contadores[0] += 1
#     elif voto == 2:
#         contadores[1] += 1
#     elif voto == 3:
#         contadores[2] += 1
#     elif voto == 4:
#         contadores[3] += 1
#     elif voto == 5:
#         contadores[4] += 1
#     elif voto == 6:
#         contadores[5] += 1

# print(contadores)
# print(f"Windows Server: {contadores[0]} | {contadores[0]}")
# print(f"Unix: {contadores[1]}")
# print(f"Linux: {contadores[2]}")
# print(f"Netware: {contadores[3]}")
# print(f"Mac OS: {contadores[4]}")
# print(f"Outro: {contadores[5]}")

# maior = max(contadores)
# indice_maior = contadores.index(maior)
# sistemas = ["Windows Server" , "Unix" , "Linux" , "Netware" , "Mac OS" , "Outro"]
# print = (f"")

#Ex3
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # c = list(lambda x: x in b, a)
# c= [x for x in a if x in b]
# print(list(set(c)))

#Ex4
# palavra_certa = ['E', 'V', 'A', 'P', 'A', 'R', 'A', 'R']
# chutes= ["_"] * len(palavra_certa)
# print(chutes)
# while chutes != palavra_certa:
#     letra = input("Digite uma letra: ").upper()
#     if letra in chutes:
#         print("Voce ja chutou essa letra, tente outra: ")
#         continue
#     for indice, elemento in enumerate(palavra_certa):
#         if elemento == letra:
#             chutes[indice] = letra
#         print(chutes)