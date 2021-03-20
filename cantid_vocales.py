from io import open
archivo_texto=open("Vocales2.txt" , "a")

texto = input("Ingrese una palabra: ")
texto = texto.lower()
vocales = ["a", "e", "i", "o", "u"]
total=0

for x in vocales:
    for y in texto :
        if x==y:
            total +=1
print("La palabra", texto, "tiene", total, "vocales")
archivo_texto.write("La palabra " + texto + " tiene " + str(total) + " vocales")
archivo_texto.write("\n")
archivo_texto.close()
