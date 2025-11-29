year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
    if year % 4 != 0:
        print("El año ingresado es comun")
    elif year % 100 != 0:
        print("El año ingresado es bisiesto")
    elif year % 400 != 0:
        print("El año ingresado es comun")
    else:
        print("El año ingresado es bisiesto") 