import tkinter
import random
from tkinter.constants import DISABLED 
import time
intentos = 7
palabras = ['hola', 'adios', 'perejil', 'hamaca', 'patata', 'uva', 'salchicha', 'lluvia', 'sillon', 'queso', 'maracas', 'chorizo', 'vestido', 'telefono', 'gorrion', 'estupidez', 'sufrimiento', 'requeson', 'zambomba']
letrasvalidas = ('a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z')
word = palabras[random.randint(0,len(palabras) - 1)]
letrasusadas = []

class aplicacion:

    def __init__(self):
        global intentos
        self.indice = []
        for i in range(len(word)): #creamos una lista con la longitud de la palabra
            self.indice.append('-')

        self.root = tkinter.Tk() 
        self.root.title('Ahorcado')
        self.root.config(bg='black')
        self.root.config(bd=3)
        self.root.geometry('2000x1500')


        self.label = tkinter.Label(self.root, text='Ahorcado') 
        self.label.grid(row=0, column=0)
        self.label.config(fg='lightgreen', bg='black', font=('verdana', 30))

        self.texto = tkinter.StringVar()
        self.texto.set(''.join(self.indice))
        self.adivinado = tkinter.Label(self.root, textvariable=self.texto)
        self.adivinado.grid(row=1,column=0)
        self.adivinado.config(fg='black', font=('verdana', 25))

        self.salida = tkinter.StringVar()
        self.label3 = tkinter.Label(self.root, textvariable=self.salida)
        self.label3.grid(row=2, column=2)
        self.label3.config(fg='lightgreen', bg='black', font=('verdana', 30))
                
        self.imagen7 = tkinter.PhotoImage(file='a7.gif')
        self.imagen6 = tkinter.PhotoImage(file='a6.gif')
        self.imagen5 = tkinter.PhotoImage(file='a5.gif')
        self.imagen4 = tkinter.PhotoImage(file='a4.gif')
        self.imagen3 = tkinter.PhotoImage(file='a3.gif')
        self.imagen2 = tkinter.PhotoImage(file='a2.gif')
        self.imagen1 = tkinter.PhotoImage(file='a1.gif')        
  
        self.foto = tkinter.Label(self.root, image=self.imagen7, bd=10).grid(row=2, column=0, pady=10)

        self.n1 = tkinter.StringVar()
        self.entry = tkinter.Entry(self.root, textvariable=self.n1)
        self.entry.grid(row=2, column=1, padx=5, pady=10)

        self.puntuacion = tkinter.Label(self.root, text = 'Puntuacion:')
        self.puntuacion.grid(row=2, column=3)
        self.puntuacion.config(fg='blue', bg='black', font=('verdana', 18))

        self.puntos = tkinter.StringVar()
        self.puntos.set(0)
        self.visor = tkinter.Label(self.root, textvariable=self.puntos)
        self.visor.grid(row=2, column=4)
        self.visor.config(fg='blue', bg='black', font=('verdana', 18))

        self.letras = tkinter.StringVar()
        self.letras.set(' | '.join(letrasusadas))
        self.letra = tkinter.Label(self.root, textvariable=self.letras)
        self.letra.grid(row=4, column=2)
        self.letra.config(fg='yellow', bg='black', font=('verdana', 14))

        self.comprobarletra = tkinter.Button(self.root, text="Comprobar letra", command = self.comprobadorLetra).grid(row=1, column=1)
        self.comprobarpalabra= tkinter.Button(self.root, text="Comprobar palabra", command = self.comprobadorpalabra).grid(row=1, column=2)
        self.comprobarpalabra= tkinter.Button(self.root, text="Reiniciar", command = self.reiniciar).grid(row=1, column=3)

        self.root.mainloop()  

    def comprobadorLetra(self): #comprueba si la letra esta en la palabra
        global intentos, letrasusadas
        acierto = 0
        self.sumar = True
        self.repetida = False
        if self.n1.get() in letrasvalidas and len(self.n1.get()) == 1 and self.n1.get() not in letrasusadas: #comprueba que no este repetida y que sea valida
            letrasusadas.append(self.n1.get()) #escribe las letras que usan
            self.letras.set(' / '.join(letrasusadas))
            for i in range(0, len(word)):
                if self.n1.get() == word[i]:
                    self.indice[i] = self.n1.get()
                    acierto += 1
        elif self.n1.get() not in letrasvalidas: #si no es valida no suma intentos
            self.salida.set('LETRA NO VALIDA')
            acierto = 1000
            self.n1.set('')
        elif self.n1.get() in letrasusadas: #si es repetida no suma intentos
            self.repetida = True
            self.salida.set('LETRA REPETIDA')
            self.n1.set('')

        if acierto > 0 and acierto != 1000 and acierto != 10000 and self.repetida == False: #comprueba diferentes valores para hacer una accion o otra
            self.n1.set('')
            self.texto.set(''.join(self.indice))
            self.salida.set('')
            self.salida.set('Acierto')
            self.sumar = False
        elif acierto == 1000:
            self.sumar = False
        elif self.repetida == True:
            self.sumar = False
        else:
            self.n1.set('')
            self.salida.set('')
            self.salida.set('Fallo')
                
        if self.sumar == True:
            intentos -= 1

        self.fotochanger()
        self.ganador()
        
        return self.indice, intentos

    def comprobadorpalabra(self): #comprueba la palabra
        global intentos
        if self.n1.get() == word:
            self.n1.set('')
            self.n1.set('HAS GANADO')
            self.puntos.set(100 + intentos * 10) 
            self.reiniciar()
        else:
            self.salida.set('PALABRA FALLADA')
            intentos -= 3
        self.fotochanger()
        self.ganador()
        return intentos
    
    def fotochanger(self): #cambia la foto segun los intentos
        global intentos 
        if intentos == 7:
            self.foto = tkinter.Label(self.root, image=self.imagen7, bd=10).grid(row=2, column=0, pady=10)
        elif intentos == 6:
            self.foto = tkinter.Label(self.root, image=self.imagen6, bd=10).grid(row=2, column=0, pady=10)
        elif intentos == 5:
            self.foto = tkinter.Label(self.root, image=self.imagen5, bd=10).grid(row=2, column=0, pady=10)
        elif intentos == 4:
            self.foto = tkinter.Label(self.root, image=self.imagen4, bd=10).grid(row=2, column=0, pady=10)
        elif intentos == 3:
            self.foto = tkinter.Label(self.root, image=self.imagen3, bd=10).grid(row=2, column=0, pady=10)
        elif intentos == 2:
            self.foto = tkinter.Label(self.root, image=self.imagen2, bd=10).grid(row=2, column=0, pady=10)
        elif intentos == 1:
            self.foto = tkinter.Label(self.root, image=self.imagen1, bd=10).grid(row=2, column=0, pady=10)
        elif intentos == 0:
            self.salida.set('Intentos acabados reiniciando')
            self.puntos.set(0)
            self.n1.set('HAS PERDIDO')
            self.reiniciar()

    def ganador(self): #comprueba si has ganado
        if word == ''.join(self.indice):
            self.n1.set('HAS GANADO') 
            self.puntos.set(100 + intentos * 10) 
            self.reiniciar()
        else:
            pass 

    def reiniciar(self): #reinicia el juego pero no toca la puntuacion
        global intentos, word, letrasusadas
        letrasusadas = []
        self.letras.set('')
        intentos = 7
        self.fotochanger()
        self.salida.set('')
        self.indice = []
        word = palabras[random.randint(0,len(palabras) - 1)]
        for i in range(len(word)): #creamos una lista con la longitud de la palabra
            self.indice.append('-')    
        self.texto.set(''.join(self.indice))
        return self.indice, word, intentos, letrasusadas
        
ahorcado = aplicacion()
