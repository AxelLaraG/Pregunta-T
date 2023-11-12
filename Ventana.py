import tkinter as tk
from tkinter import Label
import threading
from Juego import *

# Detectar si la pregunta se está mostrando
ventana = False
gameOver = False
cont = 0
valP = ""

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
    if opc == 0:  # Instrucciones Personaje
        t = threading.Thread(
            target=mostrarInstruccionesPersonaje, args=(ajolote, finn, mapache)
        )
    if opc == 1:  # Instrucciones del Juego
        t = threading.Thread(target=mostrarInstruccionesJuego)
    if opc == 2:  # Mostrar pregunta
        t = threading.Thread(target=mostrarPregunta, args=(ajolote, finn, mapache))
    if opc == 3:  # Respuesta equivocada
        t = threading.Thread(target=respuestaErronea)
    if opc == 5:  # Respuesta correcta
        t = threading.Thread(target=ventanaFelicitacion)
    if opc == 6:  # Juego Terminado con vidas
        t = threading.Thread(target=ventanaPuntos)
    if opc == 7:  # Selección de nivel
        t = threading.Thread(target=ventanaSeleccionNivel)
    t.start()


def accionCerrar(root):
    global ventana
    ventana = False
    root.quit()
    

def accion_aceptar(respuesta_Entry, root, ajolote, finn, mapache):
    global cont
    set_Respuesta(respuesta_Entry.get())
    root.quit()  # Detener el bucle principal de tkinter
    validarRespuesta(ajolote, finn, mapache)
    if get_error():
        if get_Vidas() > 1:
            reducirVidas()
            run_tkinter(3, ajolote, finn, mapache)
        else:
            set_gameOver(True)
    else:
        run_tkinter(5, ajolote, finn, mapache)
    modificarPregunta()
    cont +=1
    if cont >= 8:
        set_gameOver(True)


def on_cerrar_ventana():
    pass

def seleccionNivel(lvl,root):
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
    root = tk.Tk()
    root.title("Game Over")
    root.protocol("WM_DELETE_WINDOW", accionCerrar(root))
    label = tk.Label(
        root,
        text="Fin del juego, obtuviste: " + valP + " puntos",
        font=("Georgia", 8),
        padx=20,
        pady=20,
        justify="center",
    )
    label.pack()
    centrarVentana(root)
    root.mainloop()


def ventanaFelicitacion():
    modificarPuntos()
    set_valP(str(get_Puntos()))
    root = tk.Tk()
    root.title("Felicitación")
    root.protocol("WM_DELETE_WINDOW", accionCerrar(root))
    label = tk.Label(
        root,
        text="Respuesta correcta! +10 puntos",
        font=("Georgia", 8),
        padx=20,
        pady=20,
        justify="center",
    )
    label.pack()

    centrarVentana(root)

    root.mainloop()


def respuestaErronea():
    set_valP(str(get_Puntos()))
    root = tk.Tk()
    root.title("Respuesta equivocada")
    root.protocol("WM_DELETE_WINDOW", accionCerrar(root))
    label = tk.Label(
        root,
        text="Respuesta equivocada te quedan: " + str(get_Vidas()) + " vidas",
        font=("Georgia", 8),
        padx=20,
        pady=20,
        justify="center",
    )
    label.pack()
    centrarVentana(root)
    root.mainloop()


def mostrarPregunta(ajolote, finn, mapache):
    global ventana
    ventana = True
    root = tk.Tk()
    root.title("Pregunta")
    root.protocol("WM_DELETE_WINDOW", on_cerrar_ventana)
    if ajolote:
        label = tk.Label(
            root,
            text=preguntas_Ajolote[get_numP()],
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="center",
        )
    if finn:
        label = tk.Label(
            root,
            text=preguntas_Finn[get_numP()],
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="center",
        )
    if mapache:
        label = tk.Label(
            root,
            text=preguntas_Ajolote[get_numP()],
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="center",
        )
    label.pack()

    pregunta_label = tk.Label(root, text="Escribe tu respuesta:")
    pregunta_label.pack()
    respuesta_Entry = tk.Entry(root)
    respuesta_Entry.pack()
    centrarVentana(root)
    aceptar_button = tk.Button(
        root,
        text="Aceptar",
        command=lambda: accion_aceptar(respuesta_Entry, root, ajolote, finn, mapache),
    )
    aceptar_button.pack()
    root.mainloop()


def mostrarInstruccionesJuego():
    root = tk.Tk()
    root.title("Instrucciones")
    label = Label(
        root,
        text="Cómo jugar:"
        "\n\nW=Moverse hacia atrás"
        "\n\nA=Moverse hacia la izquierda"
        "\n\nS=Moverse hacia la adelante"
        "\n\nD= Moverse hacia derecha"
        "\n\nE=Regresar al menú"
        "\n\nEvita las esferas rojas, son Game Over directo",
        font=("Georgia", 8),
        padx=20,
        pady=20,
        justify="center",
    )
    label.pack()
    centrarVentana(root)
    root.mainloop()


def mostrarInstruccionesPersonaje(ajolote, finn, mapache):
    root = tk.Tk()
    root.title("Instrucciones")
    if ajolote:
        label = Label(
            root,
            text="Posibles movimientos:"
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
            "\n\nFlecha Izq y Der cambia de fondo",
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="left",
        )
    elif finn:
        label = Label(
            root,
            text="Posibles movimientos:"
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
            "\n\nY: Mover pie derecho",
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="left",
        )
    elif mapache:
        label = Label(
            root,
            text="Posibles movimientos:"
            "\n\nO: Original"
            "\n\nC: Chiquito"
            "\n\nR: Levantar Brazo"
            "\n\nL: Levantar Brazos"
            "\n\nA: Enojado"
            "\n\nS: Mueca"
            "\n\nY: Llorar"
            "\n\nN: Emocionado"
            "\n\nU: Confundido"
            "\n\nFlecha Izq y Der cambia de fondo",
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="left",
        )
    else:
        label = Label(
            root,
            text="Seleccionar personaje:"
            "\n\n5:Finn el humano"
            "\n\n6:Miguel el Ajolote"
            "\n\n7:Juanito el Mapache",
            font=("Georgia", 8),
            padx=20,
            pady=20,
            justify="left",
        )
    label.pack()
    root.mainloop()


def ventanaSeleccionNivel():
    global ventana
    ventana = True
    root = tk.Tk()
    root.title("Selección de nivel")
    root.protocol("WM_DELETE_WINDOW", accionCerrar(root))
    label = Label(
        root, text="", font=("Georgia", 8), padx=20, pady=20, justify="center"
    )
    lvl1_button = tk.Button(root, text="Nivel 1", command=lambda: seleccionNivel(1,root))
    lvl2_button = tk.Button(root, text="Nivel 2", command=lambda: seleccionNivel(2,root))
    lvl1_button.pack(pady=10)
    lvl2_button.pack()
    label.pack()
    centrarVentana(root)
    root.mainloop()
