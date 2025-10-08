            #Exercicio 1 e 2
# x = float(input("Digite um número: "))
# y = float(input("Digite outro número: "))
""" 
    Calcula a média entre dois numeros
    Args 
    x(float): o primeiro numero
    y(float): o segundo numero
"""
# def media (x, y):
#         res = (x+y) / 2
#         return res
# print(f"A média é: {media(x, y): .2f}")

            #Exercicio 3
# x = float(input("Digite um número: "))
# y = float(input("Digite outro número: "))
# def maximo(x, y):
#         if x> y:
#             return x
#         else:
#             return y
# maior = maximo(x, y)
# print(f"O maior número é {maximo(x, y)}")

            #Exercicio 4
# x = float(input("Digite um número: "))
# y = float(input("Digite outro número: "))
# def multiplo(x, y):
#     if x % y==0 :
#         return True
#     else:
#         return False
# print(multiplo(x, y))

            #Exercicio 5
# b = float(input("Digite a base do triangulo: "))
# h = float(input("Digite a altura do triangulo: "))
# def area(b, h):
#     res= (b*h) / 2
#     return res
# print(area(b, h))

            #Exercicio 6 
# from math import sqrt
# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))
# n3 = int(input("Digite um número: "))
# def calculo(n1, n2, n3):
#     res= sqrt(n1) + sqrt(n2) + sqrt(n3) + ((n1+n2)/2) + ((n2+n3)/2) + ((n1+n3)/2)
#     return res
# print(calculo(n1, n2, n3))

            #Exercicio 7
sexo= (input("Digite seu sexo: "))
peso= float(input("Digite seu peso: "))
def apta(sexo, peso):
    if sexo== 'feminino' and peso>= 50:
        print("Voce está apta a doar sangue")
    elif sexo== 'masculino' and peso>= 60:
        print("Voce está apto a doar sangue")
    else: 
        print("Coloque dados válidos")
