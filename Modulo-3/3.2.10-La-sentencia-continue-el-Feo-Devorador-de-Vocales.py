user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU": 
        continue 
    else:
        print(letter) 