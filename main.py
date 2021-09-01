import random 

palabras = ['hola', 'adios', 'perejil', 'hamaca']

word = palabras[random.randint(0,len(palabras) - 1)]
primeravez = True
indice = []
acierto = 0
letrasvalidas = ('a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z')
intentos = 7

class comprobador:
    def creador(self):
        for i in range(len(word)): #creamos una lista con la longitud de la palabra
            indice.append('-')
    def comprobadorLetra(self, a): #comprueba si la letra esta en la palabra
        global acierto
        for i in range(0, len(word)):
            if a == word[i]:
                indice[i] = a 
                acierto += 1 #variamos el valor acierto para que mas tarde se comprueba que la letra ha sido acertada
        return indice, acierto          
   
comprobado = comprobador()
comprobado.creador()

while intentos != 0:
    acierto = 0
    letravalida = False
    opcion = input("[1] Escribir Letra [2] Adivinar palabra ")
    if opcion == '1':
        letra = input('Escribe una letra: ')
        if letra in letrasvalidas:
            comprobado.comprobadorLetra(letra) 
        else:
            print("Caracter no valido")
            break
        if  acierto > 0: #comprobamos si el valor cambia
            print('HAS ACERTADO LA LETRA')
        else:
            print('NO HAS ACERTADO LA LETRA')
            intentos -= 1
    elif opcion == '2':
        palabra = input("Escribe una palabra: ")
        if palabra == word: #comprobar de manera directa la palabra
            print('Genial has acertado!!')
            input()
            break
        else:
            print('Sigue intentandolo')
            intentos -= 3
    else: 
        print("OPCION NO VALIDA")     
        
    print(" ".join(indice),f"  Intentos: [{intentos}]")












