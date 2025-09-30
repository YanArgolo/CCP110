# Exercicio 1
# x = 5
# def f1():
#     global x
#     x = 4
# def f2(a,b):
#     global x
#     return a+b+x
# f1()
# total = f2(1,2)
# print(total)

# Exercicio 2
# x = 5
# def f1():
#     global x
#     X = 4
# def f2(a,b):
#     X = 3
#     return a+b+x
# f1()
# total = f2(1,2)
# print(total)

# Exercicio 3
# from math import sqrt
# def hip(lado1, lado2):
#     hipotenusa = (lado1**2 + lado2**2)
#     resultado = sqrt(hipotenusa)
#     return resultado
# lado1 = float(input("Digite o primeiro lado do triângulo: "))
# lado2 = float(input("Digite o segundo lado do triângulo: "))
# print(f"Hipotenusa:{hip(lado1,lado2): .2f}")

# Exercicio 4
# def maximo(x, y, imprime=False):
#     if x>y:
#         resultado = x
#     else: 
#         resultado = y
#     if imprime == True:
#         print(f"{resultado}")
#     return resultado
# numero1 = int(input(""))
# numero2 = int(input(""))
# valor_maximo = maximo(numero1, numero2, imprime=True)

# Exercicio 5
# def media(nota1, nota2, nota3, letra):
#     if letra == 'a':
#         resultado= (nota1 + nota2 + nota3) / 3
#     elif letra=='p':
#         resultado= ((nota1*5) + (nota2*3) + (nota3*2)) /10
#     return resultado
# nota1 = float(input("Digite sua primeira nota: "))
# nota2 = float(input("Digite sua segunda nota: "))
# nota3 = float(input("Digite sua terceira nota: "))
# letra=  input("letra: ")
# notafinal= media(nota1, nota2, nota3, letra)
# print(f"a média calculada é: {notafinal: .2f}")

# Exercicio 6 
