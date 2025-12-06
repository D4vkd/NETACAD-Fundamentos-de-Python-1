my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

comp = []

for i in my_list:
    if i not in comp:
        comp.append(i) 

my_list = comp[:] 

print("La lista con elementos únicos:")
print(my_list)