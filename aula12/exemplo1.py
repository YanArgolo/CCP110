pares = open("pares.txt", "w")
impares = open("impares.txt", "w")

for numero in range(1000):
    if numero %2 == 0:
        pares.write(f"{numero}\n")
    else:
        impares.write(f"{numero}\n")
pares.close()
impares.close()