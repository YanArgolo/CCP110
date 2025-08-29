#print(5 >9)

# a = int (input ("Digite um numero: ") )
# b = int (input ("Digite outros numero: ") )

# if a > b:
#     print("Esse numero eh maior! ")
#     print(a)
#     print("Fim do if")

# print("Execute de forma independente da condição")

# salario = float (input ("Digite o valor do salario atual: ") )

# if salario < 1800:
#     novo_salario = salario * 1.1
#     print ("O funcionario tem direito a 10% de aumento")
#     print ("O novo salario ser de R$ %.2f" % novo_salario)
#     print ("Parabens pelo novo sal rio! ! ! ")

#Exercício 1
# a = int(input("Digite um número: "))
# b = int(input("Digite outro número: "))

# if a > b:
#     print(f"Maior: {a} ")

# if b > a:
#     print(f"Maior: {b} ")

#Execício 2
# a = int(input("Digite um número: "))

# if a >= 0:
#     print("Positivo!")
          
# else:
#     print("Negativo!")

#Exercício 3
# dia = int(input("Digite um número: "))

# if dia == 1:
#     print("Domingo")
# if dia == 2:
#     print("Segunda")    
# if dia == 3:
#     print("Terça")   
# if dia == 4:
#     print("Quarta") 
# if dia == 5:
#     print("Quinta")  
# if dia == 6:
#     print("Sexta")  
# if dia == 7:
#     print("Sábado")   

#Exercício 4
# salar = float(input("Digite seu salário: "))
# salariosup = 1250 * 10/100
# salarioinf = 1250 * 15/100

# if salar <= 1250:
#     print(f"Seu novo salário aumentou para: {salar + salarioinf: .2f}")

# else:
#     print(f"Seu novo salário aumentou para: {salar + salariosup: .2f}")

#Exercício 5
# nascimento = int(input("Digite sua data de nascimento: "))
# idade = 2025 - nascimento

# if idade >= 18:
#     print(f"Você tem {idade} anos, já pode tirar a CNH")

#Exercício 6
# anocar = int(input("Digite o ano do seu carro: "))
# if anocar <= 2022:
#     print(f"Seu carro é antigo, pois é do ano de {anocar}")

# else:
#     print(f"Seu carro é novo, pois é do ano de {anocar}")

#Exercício 7 
distancia = int(input("Digite a distancia que deseja percorrer: "))
precovicurta = 0.50 * {distancia}
precovilonga = 0.45 * {distancia}

if distancia >= 200:
    prin