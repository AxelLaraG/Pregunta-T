import pygame
from Personajes import Ajolote as aj
from Personajes import Finn as fn
from Personajes import Mapache as mp
from Ventana import *
from Juego import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import os

# Ddetectar si el personaje se está moviendo
camina = False
creditos = False

# Variable para detectar si se va a jugar
juego = False
nivel_nuevo = True

# Variables para el control del mouse
rotating = False
prev_mouse_x = 0
prev_mouse_y = 0
rotation_speed = 0.5

# Posicion del personaje
p_x, p_y, p_z = 0, 0, 0

# Determinar el personaje seleccionado
ajolote, mapache, finn = False, False, False

# Identificar personaje
personaje = 0

# Bandera para fondos
cont = 0

# Bandera para sonidos
band = 0

# Inicializa Pygame
pygame.init()

# Configuramos la ventana de Pygame
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption(
    "Pregunta T      Presiona Z para ver instrucciones"
)

# Configura la perspectiva OpenGL
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
gluLookAt(0, 0, 4, 0, 0, 0, 0, 1, 0)

# Diccionario de control de cámara
cam = {
    K_1: False,
    K_2: False,
    K_PLUS: False,
    K_MINUS: False,
    K_3: False,
    K_4: False,
}

# Inicializar diccionario de eventos
keys = {}

# Arreglo de sonidos
sound = []


# Arreglo de fondos
fondos = [
    "Backgrounds/Finn/fondo1.png",
    "Backgrounds/Finn/fondo2.png",
    "Backgrounds/Finn/fondo3.png",
    "Backgrounds/Finn/abajo.png",
    "Backgrounds/Finn/top.png",
]

texture_background = pygame.image.load(fondos[0])
texture_left = pygame.image.load(fondos[1])
texture_right = pygame.image.load(fondos[2])
texture_bottom = pygame.image.load(fondos[3])
texture_top = pygame.image.load(fondos[4])


# Llenado de sonidos
def llenadoDeSonidos():
    global ajolote, finn, mapache, sound
    raiz = "Sounds/Finn"
    if ajolote:
        raiz = "Sounds/Ajolote"
    if mapache:
        raiz = "Sounds/Mapache"
    if juego:
        raiz = "Sounds/Juego"
    sound.clear()
    for i in os.listdir(raiz):
        if i.endswith(".wav") or i.endswith(".mp3"):
            sound.append(pygame.mixer.Sound(os.path.join(raiz, i)))


def stopSound():
    global sound
    for i in range(0, len(sound)):
        sound[i].stop()


def reproducirSonido():
    global band, sound
    stopSound()
    if band < len(sound):
        sound[band].play()
        band += 1
    else:
        band = 0
        sound[band].play()


def llenadoDeFondos():
    global ajolote, finn, mapache, texture_background, texture_left, texture_right, texture_bottom, texture_top, fondos, cont

    cont = 0

    fondos = [
        "Backgrounds/Finn/fondo1.png",
        "Backgrounds/Finn/fondo2.png",
        "Backgrounds/Finn/fondo3.png",
        "Backgrounds/Finn/abajo.png",
        "Backgrounds/Finn/top.png",
    ]

    texture_background = pygame.image.load(fondos[0])
    texture_left = pygame.image.load(fondos[1])
    texture_right = pygame.image.load(fondos[2])
    texture_bottom = pygame.image.load(fondos[3])
    texture_top = pygame.image.load(fondos[4])

    if ajolote:
        fondos = [
            "Backgrounds/Ajolote/0.jpg",
            "Backgrounds/Ajolote/1.jpg",
            "Backgrounds/Ajolote/2.jpg",
            "Backgrounds/Ajolote/3.jpg",
            "Backgrounds/Ajolote/4.jpg",
            "Backgrounds/Ajolote/5.jpg",
            "Backgrounds/Ajolote/6.jpg",
            "Backgrounds/Ajolote/7.jpg",
            "Backgrounds/Ajolote/8.jpg",
            "Backgrounds/Ajolote/9.jpg",
            "Backgrounds/Ajolote/10.jpg",
            "Backgrounds/Ajolote/11.jpg",
            "Backgrounds/Ajolote/12.jpg",
            "Backgrounds/Ajolote/13.jpg",
            "Backgrounds/Ajolote/14.jpg",
            "Backgrounds/Ajolote/15.jpg",
            "Backgrounds/Ajolote/16.jpg",
            "Backgrounds/Ajolote/17.jpg",
            "Backgrounds/Ajolote/18.jpg",
            "Backgrounds/Ajolote/19.jpg",
            "Backgrounds/Ajolote/20.jpg",
        ]

        texture_background = pygame.image.load(fondos[2])
        texture_left = pygame.image.load(fondos[0])
        texture_right = pygame.image.load(fondos[0])
        texture_bottom = pygame.image.load(fondos[1])
        texture_top = pygame.image.load(fondos[1])

    if mapache:
        fondos = [
            "Backgrounds/Mapache/1.jpg",
            "Backgrounds/Mapache/2.jpg",
            "Backgrounds/Mapache/3.jpg",
            "Backgrounds/Mapache/4.jpg",
            "Backgrounds/Mapache/5.jpg",
            "Backgrounds/Mapache/6.jpg",
            "Backgrounds/Mapache/7.jpg",
            "Backgrounds/Mapache/8.jpg",
            "Backgrounds/Mapache/9.jpg",
            "Backgrounds/Mapache/10.jpg",
            "Backgrounds/Mapache/11.jpg",
            "Backgrounds/Mapache/12.jpg",
            "Backgrounds/Mapache/13.jpg",
            "Backgrounds/Mapache/14.jpg",
        ]
        texture_background = pygame.image.load(fondos[2])
        texture_left = pygame.image.load(fondos[0])
        texture_right = pygame.image.load(fondos[0])
        texture_bottom = pygame.image.load(fondos[1])
        texture_top = pygame.image.load(fondos[1])


# Función para cargar una textura OpenGL
def load_texture(texture_surface):
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width, height = texture_surface.get_size()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGB,
        width,
        height,
        0,
        GL_RGB,
        GL_UNSIGNED_BYTE,
        texture_data,
    )

    return texture_id


# Función para manejar los eventos del mouse
def handle_mouse_events(event):
    global rotating, prev_mouse_x, prev_mouse_y

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Botón izquierdo del mouse
            rotating = True
            prev_mouse_x, prev_mouse_y = event.pos
    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            rotating = False
    elif event.type == pygame.MOUSEMOTION and rotating:
        delta_x = event.pos[0] - prev_mouse_x
        delta_y = event.pos[1] - prev_mouse_y
        prev_mouse_x, prev_mouse_y = event.pos
        glRotatef(delta_x * rotation_speed, 0, 1, 0)
        glRotatef(delta_y * rotation_speed, 1, 0, 0)


# Dibujar cubo de texturas
def texturas():
    # Establecimiento de texturas en formato OpenGL
    texture_background_id = load_texture(texture_background)
    texture_left_id = load_texture(texture_left)
    texture_right_id = load_texture(texture_right)
    texture_top_id = load_texture(texture_top)
    texture_bottom_id = load_texture(texture_bottom)
    # Dibuja un cubo con texturas
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_background_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 0)
    glVertex3f(20, -20, -20)
    glTexCoord2f(1, 1)
    glVertex3f(20, 20, -20)
    glTexCoord2f(0, 1)
    glVertex3f(-20, 20, -20)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture_left_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 0)
    glVertex3f(-20, -20, 20)
    glTexCoord2f(1, 1)
    glVertex3f(-20, 20, 20)
    glTexCoord2f(0, 1)
    glVertex3f(-20, 20, -20)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture_right_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(20, -20, -20)
    glTexCoord2f(1, 0)
    glVertex3f(20, -20, 10)
    glTexCoord2f(1, 1)
    glVertex3f(10, 10, 10)
    glTexCoord2f(0, 1)
    glVertex3f(20, 20, -20)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture_top_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-20, 20, -20)
    glTexCoord2f(1, 0)
    glVertex3f(20, 20, -20)
    glTexCoord2f(1, 1)
    glVertex3f(20, 20, 20)
    glTexCoord2f(0, 1)
    glVertex3f(-20, 20, 20)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture_bottom_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 0)
    glVertex3f(20, -20, -20)
    glTexCoord2f(1, 1)
    glVertex3f(20, -20, 20)
    glTexCoord2f(0, 1)
    glVertex3f(-20, -20, 20)
    glEnd()

    glDisable(GL_TEXTURE_2D)


def inicializarBrillo():
    light_ambient = [0.9, 0.9, 0.9, 1.0]
    light_diffuse = [0.3, 0.3, 0.3, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]
    light_position = [1.0, 1.5, 1.0, 0.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)


def definirPersonaje():
    global personaje, ajolote, mapache, finn
    ajolote, mapache, finn = False, False, False
    if personaje == 1:
        finn = True
    if personaje == 2:
        ajolote = True
    if personaje == 3:
        mapache = True


def reloadKeys():
    global keys
    for key in keys:
        keys[key] = False


def definirEventos():
    global keys, ajolote, finn, mapache
    if juego:
        keys = {
            "W": False,
            "A": False,
            "S": False,
            "D": False,
        }
    elif ajolote:
        keys = {
            "C": False,  # Mov 1
            "H": False,  # Gesto 1
            "A": False,  # Mov 2
            "D": False,  # Mov 3
            "E": False,  # Gesto 2
            "T": False,  # Gesto 3
            "M": False,  # Gesto 4
            "I": False,  # Gesto 5
            "L": False,  # Gesto 6
            "P": False,  # Mov 4
            "O": False,  # Mov 5
            "V": False,  # Mov 6
            "K": False,  # Gesto 7
        }
    elif finn:
        keys = {
            "C": False,  # Camina
            "S": False,  # Salta
            "G": False,  # Gritar
            "E": False,  # Furia
            "P": False,  # Golpear
            "L": False,  # Llorar
            "W": False,  # Saludar
            "F": False,  # Brazo I
            "B": False,  # Brazo Derecho
            "X": False,  # Pie I
            "Y": False,  # Pie Derecho
        }
    elif mapache:
        keys = {
            "O": False,
            "C": False,
            "R": False,
            "L": False,
            "A": False,
            "S": False,
            "Y": False,
            "N": False,
            "U": False,
        }


def movCam():
    global cam
    if cam[K_1]:
        glRotatef(1, -1, 0, 0)
    if cam[K_2]:
        glRotatef(1, 1, 0, 0)
    if cam[K_PLUS]:
        glTranslatef(0.0, 0.0, 0.1)
    if cam[K_MINUS]:
        glTranslatef(0.0, 0.0, -0.1)
    if cam[K_3]:
        glRotatef(1, 0, -1, 0)
    if cam[K_4]:
        glRotatef(1, 0, 1, 0)


# Cargando las texturas
def inicializarTexturas(fondo_NB, fondo_NL, fondo_NR, fondo_NT, fondo_NBo):
    global texture_left, texture_right, texture_background, texture_top, texture_bottom, fondos
    texture_background = pygame.image.load(fondos[fondo_NB])
    texture_right = pygame.image.load(fondos[fondo_NR])
    texture_left = pygame.image.load(fondos[fondo_NL])
    texture_bottom = pygame.image.load(fondos[fondo_NBo])
    texture_top = pygame.image.load(fondos[fondo_NT])


def movPersonaje():
    global p_x, p_y, p_z
    if keys["W"]:
        p_z -= 0.1
    if keys["A"]:
        p_x -= 0.1
    if keys["S"]:
        p_z += 0.1
    if keys["D"]:
        p_x += 0.1


def definirFondo():
    global cont, ajolote, mapache, finn
    if cont == 0:
        if ajolote:
            inicializarTexturas(2, 0, 0, 1, 1)
        if mapache:
            inicializarTexturas(2, 1, 1, 1, 1)
    elif cont == 1:
        if ajolote or mapache:
            inicializarTexturas(8, 5, 5, 4, 4)
    elif cont == 2:
        if ajolote or mapache:
            inicializarTexturas(3, 7, 7, 9, 9)
    elif cont == 3:
        if ajolote or mapache:
            inicializarTexturas(11, 10, 10, 9, 9)
    elif cont == 4:
        if ajolote:
            inicializarTexturas(12, 14, 14, 8, 8)
        if mapache:
            inicializarTexturas(12, 13, 13, 8, 7)
    elif cont == 5:
        if ajolote:
            inicializarTexturas(15, 16, 16, 9, 7)
    elif cont == 6:
        if ajolote:
            inicializarTexturas(20, 18, 18, 9, 7)


def reiniciarElementos():
    global band
    definirPersonaje()
    definirEventos()
    llenadoDeFondos()
    stopSound()
    llenadoDeSonidos()
    band = 0


def reiniciarJuego():
    global juego, personaje, p_x, p_y, p_z, nivel_nuevo
    pygame.display.set_caption(
        "Pregunta T      Presiona Z para ver instrucciones"
    )
    set_CajaObstaculo(mBall(0.2, 0.2, 0.2, [-20, 0, 0]))
    set_puntos(0)
    set_cont(0)
    set_lvl(1)
    set_x_y2(-3)
    set_vidas(3)
    juego, nivel_nuevo = False, True
    personaje = 0
    p_x, p_y, p_z = 0, 0, 0
    reiniciarElementos()
    clearCaja()


def ejecucionPregunta():
    global visible, ajolote, finn, mapache, cajas, juego, nivel_nuevo
    cajaPersonaje = fn.cajaCabeza
    if mapache:
        cajaPersonaje = mp.cajaCabeza
    if ajolote:
        cajaPersonaje = aj.cajaCabeza
    for i in range(len(cajas)):
        if interseccion(cajaPersonaje, cajas[i]) and visible[i] == 1:
            sound[4].play()
            run_tkinter(2, ajolote, finn, mapache)
            nivel_nuevo = False
            visible[i] = 0
            setTesoro(True)
    if interseccion(cajaPersonaje, get_CajaObstaculo()) or (
        get_lvl() == 3 and (interseccion(cajaPersonaje, getCajaObstaculo2()))
    ):
        pygame.mixer.Sound(os.path.join("Sounds/Juego", "5.wav")).play()
        set_valP(str(get_Puntos()))
        set_gameOver(True)


# Función para renderizar texto en OpenGL
def render_text(text, x, y):
    font = pygame.font.Font(None, 36)  # Tamaño de la fuente
    text_surface = font.render(
        text, True, (255, 255, 255, 0), (0, 0, 0, 0)
    )  # Color del texto, fondo transparente
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    width, height = text_surface.get_width(), text_surface.get_height()

    glRasterPos2f(x, y)
    glDrawPixels(width, height, GL_RGBA, GL_UNSIGNED_BYTE, text_data)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            if event.key in cam:
                cam[event.key] = False
            if (
                juego
                and (event.key >= K_a and event.key <= K_z)
                and (chr(event.key).upper() in keys)
            ):
                keys[chr(event.key).upper()] = False
                camina = False
                sound[3].stop()
        elif event.type == pygame.KEYDOWN:
            if event.key in cam:
                cam[event.key] = True
            if (
                (event.key >= K_a and event.key <= K_z)
                and (chr(event.key).upper() in keys)
                and juego
                and not (get_Ventana())
            ):
                keys[chr(event.key).upper()] = True
                camina = True
                sound[3].stop()
                sound[3].play()
            if event.key == pygame.K_e and juego:
                reiniciarJuego()
            if event.key == pygame.K_TAB and juego and nivel_nuevo:
                if get_lvl() < 3:
                    set_lvl(get_lvl() + 1)
                    sound[band].stop()
                    band += 1
                    sound[band].play()
                else:
                    set_lvl(1)
                    sound[band].stop()
                    band = 0
                    sound[band].play()
                    set_x_y2(-3)
                set_CajaObstaculo(mBall(0.2, 0.2, 0.2, [-20, 0, 0]))
            elif event.key == pygame.K_z:
                if juego:
                    run_tkinter(1, ajolote, finn, mapache)
                else:
                    run_tkinter(0, ajolote, finn, mapache)
            # Menú y personajes
            if not (juego):
                if event.key == pygame.K_5:
                    personaje = 1
                    pygame.display.set_caption(
                        "Pregunta T      Presiona Z para mostrar instrucciones"
                    )
                    reiniciarElementos()
                elif event.key == pygame.K_6:
                    personaje = 2
                    pygame.display.set_caption(
                        "Pregunta T      Presiona Z para mostrar instrucciones"
                    )
                    reiniciarElementos()
                elif event.key == pygame.K_7:
                    personaje = 3
                    pygame.display.set_caption(
                        "Pregunta T      Presiona Z para mostrar instrucciones"
                    )
                    reiniciarElementos()
                elif event.key == pygame.K_0:
                    personaje = 0
                    pygame.display.set_caption(
                        "Pregunta T     Presiona Z para mostrar instrucciones"
                    )
                    reiniciarElementos()
                elif event.key == pygame.K_TAB:
                    creditos = False
                    if personaje < 3:
                        pygame.display.set_caption(
                            "Pregunta T      Presiona Z para mostrar instrucciones"
                        )
                        personaje += 1
                    else:
                        pygame.display.set_caption(
                            "Pregunta T     Presiona Z para mostrar instrucciones"
                        )
                        personaje = 0
                    reiniciarElementos()
                elif event.key == pygame.K_RETURN and (ajolote or finn or mapache):
                    juego = True
                    creditos = False
                    pygame.display.set_caption(
                        "PreguntaT Presiona Z para instrucciones"
                    )
                    reiniciarElementos()
                    sound[band].play()
                elif event.key == pygame.K_RIGHT and not (finn):
                    if ajolote:
                        if cont < 6:
                            cont += 1
                        else:
                            cont = 0
                    if mapache:
                        if cont < 4:
                            cont += 1
                        else:
                            cont = 0
                    definirFondo()
                elif event.key == pygame.K_LEFT and not (finn):
                    if ajolote:
                        if cont > 0:
                            cont -= 1
                        else:
                            cont = 6
                    if mapache:
                        if cont > 0:
                            cont -= 1
                        else:
                            cont = 4
                    definirFondo()
                elif event.key >= K_a and event.key <= K_z:
                    if event.key == pygame.K_q:
                        if creditos:
                            creditos = False
                        else:
                            creditos = True
                    else:
                        creditos = False
                        val1 = chr(event.key).upper() in keys
                        if val1:
                            val2 = keys[chr(event.key).upper()] == False
                            if val1 and val2:
                                reloadKeys()
                                reproducirSonido()
                                keys[chr(event.key).upper()] = True
                            else:
                                keys[chr(event.key).upper()] = False

    movCam()
    if juego:
        movPersonaje()
        ejecucionPregunta()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    texturas()
    if creditos:
        render_text("Creado por:",-4,3.4)
        render_text("Aguirre Trujillo Wendy Violeta",-4,3)
        render_text("Lara Madero Axel",-4,2.5)
        render_text("Pavon Martel Brayham",-4,2)
    if juego:
        drawNivel(ajolote, finn, mapache)
        render_text("Vidas: " + str(get_Vidas()), -4.3, 2)
        render_text("Puntos: " + str(get_Puntos()), 3, 2)
        render_text("Nivel: " + str(get_lvl()), 0, 3)
    if ajolote:
        if juego:
            aj.dibujaAjoloteJuego(
                p_x, p_y, p_z, camina, keys["W"], keys["A"], keys["D"],getTesoro()
            )
        else:
            aj.dibujaAjolote(
                keys["C"],
                keys["H"],
                keys["A"],
                keys["D"],
                keys["E"],
                keys["T"],
                keys["M"],
                keys["I"],
                keys["L"],
                keys["P"],
                keys["O"],
                keys["V"],
                keys["K"],
            )
    elif finn:
        if juego:
            fn.dibujaFinnJuego(p_x, p_y, p_z, camina, keys["W"], keys["A"], keys["D"],getTesoro())
        else:
            fn.dibujo(
                keys["S"],
                keys["G"],
                keys["E"],
                keys["P"],
                keys["L"],
                keys["W"],
                keys["C"],
                keys["F"],
                keys["B"],
                keys["X"],
                keys["Y"],
            )

    elif mapache:
        if juego:
            mp.dibujaMapacheJuego(p_x, p_y, p_z, keys["W"], keys["A"], keys["D"])
        else:
            mp.drawMapache(
                keys["O"],
                keys["C"],
                keys["R"],
                keys["L"],
                keys["A"],
                keys["S"],
                keys["Y"],
                keys["N"],
                keys["U"],
            )
    else:
        glPushMatrix()
        glTranslated(-2, 0, -2)
        fn.dibujo(
            False, False, False, False, False, False, False, False, False, False, False
        )
        glPopMatrix()

        glPushMatrix()
        glTranslated(0, 0, 0)
        mp.drawMapache(False, False, False, False, False, False, False, False, False)
        glPopMatrix()

        glPushMatrix()
        glTranslated(2, 0, -2)
        aj.dibujaAjolote(
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        )
        glPopMatrix()

    if get_gameOver():
        set_gameOver(False)
        setTesoro(False)
        run_tkinter(6, ajolote, finn, mapache)
        reiniciarJuego()
    inicializarBrillo()
    handle_mouse_events(event)
    pygame.display.flip()
    pygame.time.wait(10)
