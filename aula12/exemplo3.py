#   Listar produtos
while True:
        nome = input("Digite um nome: ")
        telefone = (input("Digite o telefone: "))
        if nome == "" or telefone == "":
            break
        with open("contatos.txt", "w") as contatos:
            contatos.write(f" {nome} , {telefone}\n")

with open("contatos.txt", "r") as contatos:
     print("-" * 45)
     print(f"|{'nome':>25} | : {'telefone':<15}|")
     print("-" *45)
     for linha in contatos:
          nome,telefone = linha.strip().split(",")
          print(f"|{'nome':>25} |  {'telefone':<15}|")
          print("-" * 45)
