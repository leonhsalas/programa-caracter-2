caracter = input("Cual es el caracter ")

if caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
    print("Vocal Mayuscula")
elif caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
    print("vocal minuscula")
elif "a" <= caracter <= "z":
    print("consonante minuscula")
elif "A" <= caracter <= "Z":
    print("Consonante Mayuscula")
elif caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9":
    print("Numero")
else:
    print("Caracter")
