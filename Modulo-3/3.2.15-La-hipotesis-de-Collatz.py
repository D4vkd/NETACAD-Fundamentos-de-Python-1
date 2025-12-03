c0 = int(input("Ingrese un numero: "))
centinela = 0 
contador = 0

while centinela != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1
    centinela = c0 
    print(c0) 
    contador += 1

print("Numero de pasos: ", contador) 