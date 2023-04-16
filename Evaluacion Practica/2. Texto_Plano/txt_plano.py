
filename = 'texto.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:

    msg = "El archivo" + filename + "no existe"
    print(msg)

else:
    palabra = contents.split()
    num_palabras = len(palabra)
    
    n = 0
    for i in contents:
        if i =="\n":
            n += 1
            
    caracter = 0
    for c in contents:
        if c == c.isdigit() or c.isalpha():
            caracter += 1

    archivo = open('Resultado.txt','w')
    
    archivo.write("1. El archivo contiene un total de: " + str (n) + " saltos de linea."+"\n")
    archivo.write("2. El archivo contiene un total de: " + str (num_palabras) + " palabras, sin contar los espacios."+"\n")
    archivo.write("3. El archivo contiene un total de: " + str (caracter) + " caracteres."+"\n")
    archivo.write("4. En el archivo La palabra (Python) se encuenta: " + str( palabra.count('Python')) + " veces.")
    archivo.close()