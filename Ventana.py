import os
import tkinter as tk
from tkinter import Label
import threading

import pygame
from Juego import *

# Detectar si la pregunta se está mostrando
ventana = False
gameOver = False
cont = 0
valP = ""
tesoro = False
instrucciones = False
ventanaInstrucciones = tk.Tk()

def getInstrucciones():
    global instrucciones
    return instrucciones

def setTesoro(value):
    global tesoro
    tesoro = value
    
def getTesoro():
    global tesoro
    return tesoro


def set_valP(value):
    global valP
    valP = value


def get_gameOver():
    global gameOver
    return gameOver


def set_cont(val):
    global cont
    cont = val


def set_gameOver(value):
    global gameOver
    gameOver = value


def get_Ventana():
    global ventana
    return ventana


def run_tkinter(opc, ajolote, finn, mapache):
    global instrucciones
    if opc == 0:  # Instrucciones Personaje
        instrucciones = True
        t = threading.Thread(
            target=mostrarInstruccionesPersonaje, args=(ajolote, finn, mapache)
        )
    if opc == 1:  # Instrucciones del Juego
        instrucciones = True
        t = threading.Thread(target=mostrarInstruccionesJuego)
    if opc == 2:  # Mostrar pregunta
        t = threading.Thread(target=mostrarPregunta, args=(ajolote, finn, mapache))
    if opc == 6:  # Juego Terminado 
        t = threading.Thread(target=ventanaPuntos)
    t.start()


def accionCerrar(root):
    global ventana
    ventana = False
    root.quit()


def accion_aceptar(respuesta_Entry, ventanaP, ajolote, finn, mapache):
    global cont, ventana
    ventana = False
    set_Respuesta(respuesta_Entry.get())
    validarRespuesta(ajolote, finn, mapache)
    if get_error():
        pygame.mixer.Sound(os.path.join("Sounds/Juego", "5.wav")).play()
        if get_Vidas() > 1:
            reducirVidas()
        else:
            set_gameOver(True)
    else:
        pygame.mixer.Sound(os.path.join("Sounds/Juego","6.wav")).play()
        modificarPuntos()
    set_valP(str(get_Puntos()))
    modificarPregunta()
    setTesoro(False)
    cont += 1
    ventanaP.quit() 
    if cont >= 8:
        set_gameOver(True)


def on_cerrar_ventana():
    pass


def seleccionNivel(lvl, root):
    global ventana
    ventana = False
    set_lvl(lvl)
    root.quit()


def centrarVentana(root):
    # Obtener el tamaño de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (screen_width - root.winfo_reqwidth()) / 2
    y = (screen_height - root.winfo_reqheight()) / 2

    # Establecer la posición de la ventana en el centro
    root.geometry("+%d+%d" % (x, y))


def ventanaPuntos():
    global ventana
    ventana = True
    ventanaPun = tk.Tk()
    ventanaPun.title("Game Over")
    ventanaPun.protocol("WM_DELETE_WINDOW", accionCerrar(ventanaPun))
    label = tk.Label(
        ventanaPun,
        text="Fin del juego, obtuviste: " + valP + " puntos",
        font=("Georgia", 8),
        padx=20,
        pady=20,
        justify="center",
    )
    label.pack()
    centrarVentana(ventanaPun)
    ventanaPun.mainloop()


def mostrarPregunta(ajolote, finn, mapache):
    global ventana
    ventana = True
    ventanaP = tk.Tk()
    ventanaP.title("Pregunta")
    ventanaP.protocol("WM_DELETE_WINDOW", on_cerrar_ventana)
    if ajolote:
        label = tk.Label(
            ventanaP,
            text=preguntas_Ajolote[get_numP()],
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="center",
        )
    if finn:
        label = tk.Label(
            ventanaP,
            text=preguntas_Finn[get_numP()],
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="center",
        )
    if mapache:
        label = tk.Label(
            ventanaP,
            text=preguntas_Mapache[get_numP()],
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="center",
        )
    label.pack()

    pregunta_label = tk.Label(ventanaP, text="Escribe tu respuesta:")
    pregunta_label.pack()
    respuesta_Entry = tk.Entry(ventanaP)
    respuesta_Entry.pack()
    centrarVentana(ventanaP)
    aceptar_button = tk.Button(
        ventanaP,
        text="Aceptar",
        command=lambda: accion_aceptar(respuesta_Entry, ventanaP, ajolote, finn, mapache),
    )
    aceptar_button.pack()
    ventanaP.mainloop()


def mostrarInstruccionesJuego():
    ventanaInJ = tk.Tk()
    ventanaInstrucciones = ventanaInJ
    ventanaInJ.title("Instrucciones")
    label = Label(
        ventanaInJ,
        text="Cómo jugar:"
        "\n\nPara abrir una pregunta debes chocaar con las esferas doradas"
        "\n\n1: Mover cámara hacia abajo"
        "\n\n2: Mover cámara hacia arriba"
        "\n\n+: Zomm in"
        "\n\n-: Zoom out"
        "\n\n4:Mover cámara hacia la izquierda"
        "\n\n3: Mover cámara hacia la derecha"
        "\n\nW=Moverse hacia atrás"
        "\n\nA=Moverse hacia la izquierda"
        "\n\nS=Moverse hacia la adelante"
        "\n\nD= Moverse hacia derecha"
        "\n\nE=Regresar al menú"
        "\n\nTAB= Cambia de nivel (Solo si no se ha comenzado el nivel)"
        "\n\nEscribe tu respuesta en el espacio en blanco y da click en Aceptar"
        "\n\nUna vez abierta la pregunta no la podrás cerrar ni interactuar con el personaje!"
        "\n\nEvita las esferas rojas, son Game Over directo (Salen a partir del nivel 2)",
        font=("Georgia", 8),
        padx=20,
        pady=20,
        justify="center",
    )
    label.pack()
    centrarVentana(ventanaInJ)
    ventanaInJ.mainloop()


def mostrarInstruccionesPersonaje(ajolote, finn, mapache):
    global ventanaInstrucciones
    ventanaInP = tk.Tk()
    ventanaInstrucciones = ventanaInP
    ventanaInP.title("Instrucciones")
    if ajolote:
        label = Label(
            ventanaInP,
            text="Posibles movimientos:"
            "\n\n1: Mover cámara hacia abajo"
            "\n\n2: Mover cámara hacia arriba"
            "\n\n+: Zomm in"
            "\n\n-: Zoom out"
            "\n\n4:Mover cámara hacia la izquierda"
            "\n\n3: Mover cámara hacia la derecha"
            "\n\nTambién puedes usar el mouse para mover la cámara dando click y arrastrando"
            "\n\nC: Caminar"
            "\n\nH: Sorpresa"
            "\n\nA: Mover cola a la derecha"
            "\n\nD: Mover cola a la izquierda"
            "\n\nE: Enojado"
            "\n\nT: Triste"
            "\n\nM: Muerto"
            "\n\nI: Ira"
            "\n\nL: Llora"
            "\n\nP: Mover patas delanteras"
            "\n\nO: Mover patas traseras"
            "\n\nV: Sacar lengua"
            "\n\nK: Mareado"
            "\n\nQ: Créditos"
            "\n\nFlecha Izq y Der cambia de fondo"
            "\n\nEnter: Selecciona Personaje"
            "\n\nTAB: Cambia personaje",
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="left",
        )
    elif finn:
        label = Label(
            ventanaInP,
            text="Posibles movimientos:"
            "\n\n1: Mover cámara hacia abajo"
            "\n\n2: Mover cámara hacia arriba"
            "\n\n+: Zomm in"
            "\n\n-: Zoom out"
            "\n\n4:Mover cámara hacia la izquierda"
            "\n\n3: Mover cámara hacia la derecha"
            "\n\nTambién puedes usar el mouse para mover la cámara dando click y arrastrando"
            "\n\nC: Camina "
            "\n\nS: Salta"
            "\n\nG: Gritar"
            "\n\nE: Furia"
            "\n\nP: Golpear"
            "\n\nL: Llorar"
            "\n\nW: Saludar"
            "\n\nF: Mover brazo izquierdo"
            "\n\nB: Mover brazo derecho"
            "\n\nX: Mover pie izquierdo"
            "\n\nY: Mover pie derecho"
            "\n\nQ: Créditos"
            "\n\nEnter: Selecciona Personaje"
            "\n\nTAB: Cambia personaje",
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="left",
        )
    elif mapache:
        label = Label(
            ventanaInP,
            text="Posibles movimientos:"
            "\n\n1: Mover cámara hacia abajo"
            "\n\n2: Mover cámara hacia arriba"
            "\n\n+: Zomm in"
            "\n\n-: Zoom out"
            "\n\n4:Mover cámara hacia la izquierda"
            "\n\n3: Mover cámara hacia la derecha"
            "\n\nTambién puedes usar el mouse para mover la cámara dando click y arrastrando"
            "\n\nO: Original"
            "\n\nC: Chiquito"
            "\n\nR: Levantar Brazo"
            "\n\nL: Levantar Brazos"
            "\n\nA: Enojado"
            "\n\nS: Mueca"
            "\n\nY: Llorar"
            "\n\nN: Emocionado"
            "\n\nU: Confundido"
            "\n\nFlecha Izq y Der cambia de fondo"
            "\n\nQ: Créditos"
            "\n\nEnter: Selecciona Personaje"
            "\n\nTAB: Cambia personaje",
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="left",
        )
    else:
        label = Label(
            ventanaInP,
            text="Seleccionar personaje:"
            "\n\n1: Mover cámara hacia abajo"
            "\n\n2: Mover cámara hacia arriba"
            "\n\n+: Zomm in"
            "\n\n-: Zoom out"
            "\n\n4:Mover cámara hacia la izquierda"
            "\n\n3: Mover cámara hacia la derecha"
            "\n\nTambién puedes usar el mouse para mover la cámara dando click y arrastrando"
            "\n\n5:Finn el humano"
            "\n\n6:Miguel el Ajolote"
            "\n\n7:Juanito el Mapache"
            "\n\nQ: Créditos"
            "\n\nTAB: Cambia personaje",
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="left",
        )
    label.pack()
    centrarVentana(ventanaInP)
    ventanaInP.mainloop()
