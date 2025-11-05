with open("arquivo.txt" , "p" ,encoding="utf=8") as arquivo:
    conteudo = arquivo.read()
    
print(conteudo)
texto_sem_pontuacao = ""
for char in conteudo:
    if char.isalnum() or char.isspace():
        texto_sem_pontuacao += char

print(texto_sem_pontuacao)

lista_palavras = texto_sem_pontuacao.split()
print(lista_palavras)

maiores_palavras = []
maior_tamanho = 0
for palavra in lista_palavras:
    if len(palavra) > maior_tamanho:
        maior_tamanho = len(palavra)
        maiores_palavras = [palavra]
    elif len(palavra) == maior_tamanho:
        maiores_palavras.append(palavra)
