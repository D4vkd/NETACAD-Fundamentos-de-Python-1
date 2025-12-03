blocks = int(input("Ingresa el número de bloques: "))
height = 0

while True:
    height = height + 1
    blocks = blocks - height 
    if height >= blocks:
        break 

print("La altura de la pirámide:", height)