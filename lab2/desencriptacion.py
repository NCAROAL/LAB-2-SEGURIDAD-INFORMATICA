#Nicolas Caroca
#Edmond Morales
from random import sample
from itertools import product as col

dicc1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
        'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
        'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
        'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
        'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

dicc2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
        6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
        11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O',
        16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T',
        21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y'}


 
def desencriptar(mensaje, rott):
    decifrado = ''
    for letter in mensaje:
        if(letter != ' '):
            num = ( dicc1[letter] - rott + 26) % 26
            decifrado += dicc2[num]
        else:
            decifrado += ' '
 
    return decifrado
	
def vigenere(x,llave):
    lista_final = []
    codigo = list(x)
    j = 0
	
    for i,char in enumerate(codigo):
        if char.isalpha():
            codigo[i] = llave[(i+j)%len(llave)]
            lista_final.append((ord(x[i]) - ord(codigo[i])) % 26)
            
        else:
            lista_final.append(ord(char))
            j -=1

    for i,char in enumerate(codigo):
        if char.isalpha():
            lista_final[i] = chr(lista_final[i] + 65)
        else:
            lista_final[i] = chr(lista_final[i])
			
    return ''.join(lista_final)

archivo = open("mensaje seguro.txt")
leer = archivo.readlines()
archivo.close()
lista2 =[]
for i in leer:
    i = i.replace("\n","")
    lista2.append(i)
mensaje = lista2[1]
print(mensaje)
llave = input('ingrese llave: ').upper()
resultado = (vigenere(mensaje,llave))
print(resultado)
rott = 5
nuevo = desencriptar(resultado.upper(), rott)
print(nuevo)

archivo1 = open("mensajeDeEntrada.txt")
leer1 = archivo1.readlines()
archivo1.close()
print(leer1[0])

if(nuevo == leer1[0].upper()):
    print("El mensaje es integro")
else:
    print("El mensaje fue modificado")
    
