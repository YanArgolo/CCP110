# x = 1
# soma = 0
# while x <= 10:
#     n = int(input("Digite um número: "))
#     soma= soma+n
#     x= x+1

# print(f"A soma dos números é {soma}.")

# ultimo= int(input("Digite um número inteiro positivo: "))
# x = 0
# while x <= ultimo:
#     if x % 2 ==0:
#         print(x)
#     x = x+1

# soma= 0

# while True:
#     n= int(input("Digite um número (ou 0 para sair): "))
#     if n==0:
#         break
#     soma= soma+n

# print(f"A soma dos números é {soma}.")

# Exercício 1
# ultimo = int(input("Digite um número inteiro positivo: "))
# x= 0
# while x<=ultimo:
#     if x % 2 ==1: #verifica se é ímpar
#         print(x)
#     x= x+1 

# Exercício 1 for
# n = int(input("Digite um número inteiro positivo: "))
# for x in range(0, n+1):
#     if x % 2 ==1: #verifica se é ímpar
#         print(x)

# Exercício 2
# n=1 
# for x in range(1, 51):
#     print(x)

# for x in range(52, 101, 2):
#     print(x)

# Exercício 3 for
# tabuada= int(input("Digite a tabuada do número que deseja: "))
# for x in range(1, 11):
#     print(f"{tabuada} x {x} = {tabuada * x}")

# Exercício 4
# maior = 0

# for x in range(6):
#     n = int(input("Digite um número: "))
#     if n > maior:
#         maior = n

# print(f"O maior número é {maior}.")

# Exercício 5
# while True:
#     try:
#         n= int(input("Digite um numero de 0 a 10: "))
#         if 0 <= n  <=10:
#             break
#     except ValueError:
#         print("Número inválido, tente novamente.")

#Exercício 6 
while True:
    n= int(input("Digite um número(ou 0 para sair): "))
    if n== 0:
        break
    soma= soma + n
    contador= contador+1
X
print(f"Quantidade de números: {contador}.") 
print(f"soma dos numeros: {soma}.")
if contador> 0:
    print(f"Média dos números: {soma / contador}")

