# # 1
# tamovo = float(input("Digite a medida do ovo: "))
# if tamovo >= 35:
#     print("grande")
# else:
#     print("pequeno")
# # 2
# prod1 = float(input("Digite o valor do primeiro produto: "))
# prod2 = float(input("Digite o valor do segundo produto: "))
# prod3 = float(input("Digite o valor do terceiro produto: "))
# desconto1 = (prod1 + prod2 + prod3) * 20/100
# desconto2 = (prod1 + prod2 + prod3) * 10/100
# if prod1 + prod2 + prod3>=500:
#     print(f"Desconto: {desconto1:.2f}")
    
# else: 
#     print(f"Desconto: {desconto2:.2f}")
# # 3
# import math
# escolha= (input("Você deseja calcular o volume do dodecaedro ou icosaedro:"))
# a= float(input("Digite o valor da aresta a em metros: "))
# if escolha == 'dodecaedro':
#     volume =((15+7* math.sqrt(5)) /4) * (a**3)
#     print(f"O volume de um dodecaedro regular com {a:.2f} de aresta é: {volume:.2f}")
# else:
#     volume= ((5/12 *(3+math.sqrt(5))) * (a**3))
#     print(f"O volume de um icosaedro regular com {a:.2f} de aresta é: {volume:.2f}")

# # 4
# cod= int(input("Digite o código do produto:"))
# quantidade= int(input("Digite a quantidade do produto:"))
# if cod==1:
#     preco1= 6.00
#     precofinal= preco1*quantidade
# elif cod==2:
#     preco1= 6.50
#     precofinal= preco1*quantidade
# elif cod==3:
#     preco1= 5.00
#     precofinal= preco1*quantidade
# elif cod==4:
#     preco1= 3.00
#     precofinal= preco1*quantidade
# elif cod==5:
#     preco1= 2.00
#     precofinal= preco1*quantidade

# print(f"Total: R$ {precofinal:.2f}")

# # 5
# horainicial= int(input("Digite a hora inicial: "))
# mininicial= int(input("Digite o minuto inicial:"))
# horafinal= int(input("Digite a hora final: "))
# minfinal= int(input("Digite o minuto final: "))
# inicio_em_minutos= horainicial*60 + mininicial
# final_em_minutos= horafinal*60 + minfinal
# totalmin= final_em_minutos-inicio_em_minutos
# if totalmin<= 0:
#     totalmin+= 24*60

# duracaohoras= totalmin //60
# duracaofinalmin= totalmin - (duracaohoras * 60)

# print(f"O jogo durou {duracaohoras} hora(s) e {duracaofinalmin:.0f} minutos(s)")

# valor_compra = float(input("Digite o valor total da compra: R$ "))
# numero_parcelas = int(input("Digite o número de parcelas: "))
# percentual_desconto = 0
# if numero_parcelas == 1:
#     percentual_desconto = 10  # 10% para compras à vista
# elif numero_parcelas == 2 or numero_parcelas == 3:
#     percentual_desconto = 5   # 5% para 2 ou 3 parcelas
# # Se for acima de 3 parcelas, o desconto continua 0.
# if valor_compra > 5000.00:
#     percentual_desconto += 5
# valor_desconto = valor_compra * (percentual_desconto / 100)
# valor_final = valor_compra - valor_desconto
# valor_parcela = valor_final / numero_parcelas

# print("\n--- Resumo da Compra ---")
# print(f"Valor do desconto: R$ {valor_desconto:.2f}")
# print(f"Valor final da compra: R$ {valor_final:.2f}")
# print(f"Valor de cada parcela ({numero_parcelas}x): R$ {valor_parcela:.2f}")

mes= (input(""))
if mes in ('janeiro', 'março', 'maio', 'julho', 'agosto', 'outubro', 'dezembro'):
    print(f"{mes} 31 dias")
elif mes in ('abril', 'junho', 'setembro', 'novembro'):
    print(f"{mes} 30 dias")
elif mes in ('fevereiro'):
    print(f"{mes} 28 ou 29 dias")