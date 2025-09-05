# a = int(input("Lado a: "))
# b = int(input("Lado b: "))
# c = int(input("Lado c: "))
# if (a < b + c) and (b < a + c) and (c < a + b):
#     if (a == b) and ( b == c):
#         print("Triangulo equilátero")
#     else:
#         if (a == b) or (a == c) or (b == c):
#             print("Triangulo isosceles")
#         else:
#             print("Triangulo escaleno")
# else:
#     print(" Não é Triangulo")

#Exercício 1
# preco = float(input("Digite o preço do produto: "))
# cod = int(input("Digite o código do produto: "))
# if cod == 1:
#     print(f"Procedênia Sul, Preço: {preco:.2f}")
# elif cod== 2:
#     print(f"Procedênia Norte, Preço: {preco:.2f}")
# elif cod== 3:
#     print(f"Procedênia Leste, Preço: {preco:.2f}")
# elif cod== 4:   
#     print(f"Procedênia Oeste, Preço: {preco:.2f}")
# elif cod== 5 or cod== 6:
#     print(f"Procedênia Nordeste, Preço: {preco:.2f}")
# elif cod== 7 or cod== 8 or cod== 9:
#     print(f"Procedênia Sudeste, Preço: {preco:.2f}")
# elif cod>= 10 and cod<= 20:
#     print(f"Procedênia  Centro-Oeste, Preço: {preco:.2f}")
# elif cod>= 25 and cod<=30:
#     print(f"Procedênia  Centro-Oeste, Preço: {preco:.2f}")
# else:
#     print(f"Procedência Importada, Preço: R${preco:.2f}")

#Exercicio 2
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a > b and a > c:
    print(f"O maior valor é A: {a}")
    if b>c:
        print(a,b,c)
    elif c>b:
        print(a,c,b)
elif b> a and b>c:
    print(f"O maior valor é B: {b}")
    if a>c:
        print(b,a,c)
    elif c>a:
        print(b,c,a)
elif c>a and c>b:
    print(f"O maior valor é C: {c}")
    if a>b:
        print(c,a,b)
    elif b>a:
        print(c,b,a)
else: print("Os números são iguais.")




# elif b > a and b > c:
#     #print(f"O maior valor é B: {b}")
    
# elif c > a and c > a:
#     #print(f"O maior valor é C: {c}")    