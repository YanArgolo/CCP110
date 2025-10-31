#           CRUD
MENU = {
    '1': 'Adicionar novo contato',
    '2': 'Buscar contato',
    '3': 'Atualizar contato',
    '4': 'Remover contato',
    '5': 'Sair',
}

def exibir_menu():
    for chave,valor in MENU.items():
        print(f"{chave} - {valor}")
    print()

exibir_menu()

def novo_contato():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    telefone= input("Digite seu telefone: ")
    email = input("Digite seu email: ")
    with open('contato.txt' , 'a' )as arquivo:
        arquivo.write(f"{nome}, {sobrenome},{telefone},{email}\n")
        print("Contato adicionado com sucesso")

def buscar_contato():
    nome_busca= input("Digite o nome do contato que deseja buscar: ")
    encontrado = False
    with open('contatos.txt', 'r') as arquivo:
        for linha in arquivo:
            nome, sobrenome,telefone,email = linha.strip().split(',')
            if nome.lower()== nome_busca.lower():
                print(f"Encontrado: {nome} {sobrenome} {telefone} {email}" )
                encontrado = True
                break
            if not encontrado:
                print("Contato não encontrado")
            print()

def atualizar_contato():
    nome_busca = input("Digite o nome do contato que deseja atualizar: ")
    linhas = []
    atualizado = False
    with open('contatos.txt','r') as arquivo:
        linhas = arquivo.readlines()

        with open('contatos.txt','w') as arquivo:
            for linha in linhas:
                nome, sobrenome, telefone, email = linha.strip().split(',')
                if nome.lower() == nome_busca.lower():
                    print("Contato encontrado, insira os novos dados")
                    novo_nome= input("Novo nome: ")
                    novo_sobrenome = input("Novo sobrenome: ")
                    novo_telefone = input("Novo telefone: ")
                    novo_email = input("Novo email: ")
                    arquivo.write(f"{novo_nome},{novo_sobrenome}, {novo_telefone}, {novo_email}")
                    atualizado = True
                else:
                    arquivo.write()
                if atualizado:
                    print("Contato atualizado com sucesso!")
                else:
                    print("Erro ao atualizar o contato!")



while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")


    if opcao == '0':
        print('Saindo do programa...')
        break
    if opcao == '1':
        print()
        novo_contato()
    elif opcao == '2':
        buscar_contato()
    elif opcao == '3':
        pass
    elif opcao == '4':
        pass
    elif opcao == '5':
        pass