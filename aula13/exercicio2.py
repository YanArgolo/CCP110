string = input("Digite um texto: ")

print(string)

string_nova= ""
for char in string:
    if char ==" ":
        continue
    string_nova += char

string_nova = string_nova.lower()
print(string_nova.lower())

if string_nova == string_nova[::-1]:
    print("É palindromo")
else:
    print("Não é palindromo") 