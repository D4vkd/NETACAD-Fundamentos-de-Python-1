def liters_100km_to_miles_gallon(liters):
    km_l = 100/liters
    millas_l = km_l / 1.609344 #en km
    return millas_l * 3.785411784 

def miles_gallon_to_liters_100km(miles):
    km_gal = miles * 1.609344
    km_l = km_gal / 3.785411784
    return 100 / km_l 

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))