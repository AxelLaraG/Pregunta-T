from OpenGL.GL import *
from OpenGL.GLU import *
from mBall import mBall

cajaObstaculo = mBall(0.2, 0.2, 0.2, [-20, 0, 0])
x = -3
puntos = 0
vidas = 3
nivel = 1
visible = [1, 1, 1, 1, 1, 1, 1, 1]
cajas = []
cont = 0
numP = 0
respuesta = ""
err = False
preguntas_Ajolote = [
    "¿Cuál es la capital de México?",  # Ciudad de México o CDMX
    "¿Cuál es el océano que está al oeste de México?",  # Pacífico
    "¿Quién fue el primer presidente de México?",  # Guadalupe Victoria
    "¿Cuál es la pirámide más famosa de México, construida por los antiguos mayas?",  # Chichén Itzá
    "¿Cuál es el nombre de la fiesta mexicana que se celebra el 16 de septiembre?",  # Independencia
    "¿Qué famosa pintora mexicana es conocida por sus autorretratos?",  # Frida Khalo
    "¿Cuál es el río más largo de México?",  # Usumacinta
    "¿En qué año se llevó inició la Revolución Mexicana?",  # 1910
    # Nivel 2
    "¿Qué civilización construyó la ciudad de Teotihuacán en México?",  # Teotihuacana
    "¿Cuál es la moneda oficial de México?",  # Peso Mexicano
    "¿Quién fue el presidente de México que promulgó la Constitución de 1917?",  # Venustiano Carranza
    "¿Qué batalla ocurrió el 5 de mayo en México?",  # Batalla de Puebla
    "¿Cuál es el nombre de la cadena montañosa que atraviesa México desde el norte al sur?",  # Sierra Madre
    "¿En qué año México se independizó de España?",  # 1821
    "¿Cuál es el nombre de la antigua ciudad maya en la costa de la península de Yucatán?",  # Tulum
    "¿Quién es considerado el 'Padre de la Patria' en México?",  # Mguel Hidalgo y Costilla
    # Nivel 3
    "¿Cuál es el nombre del tratado que puso fin a la Guerra México-Estados Unidos en 1848?",  # Tratado de Guadalupe Hidalgo
    "¿Qué emperador reinó en México durante la Segunda Intervención Francesa?",  # Maximiliano I
    "¿Cuál es la cascada más alta de México y una de las más altas del mundo?",  # Basaseachi
    "¿Qué famoso muralista mexicano pintó 'Sueño de una tarde dominical en la Alameda Central'?",  # Diego Rivera
    "¿Cuál es el estado de México que alberga a la ciudad de Guadalajara?",  # Jalisco
    "¿En qué año se fundó la UNAM?",  # 1910
    "¿Quién fue el líder revolucionario zapatista conocido por su lema 'Tierra y Libertad'?",  # Emiliano Zapata
    "¿Cuál es la reserva de la biosfera en Chiapas que alberga una gran diversidad de plantas y animales?",  # El Triunfo
]

preguntas_Mapache = [
    "¿Qué es una exposición en el contexto de la comunicación?",  # presentación oral o escrita sobre un tema
    "¿Qué es un debate?",  # discusión estructurada
    "¿Cuál es el propósito principal de un texto argumentativo?",  # persuadir o convencer
    "¿Qué tipo de texto se centra en contar una historia y desarrollar personajes?",  # texto narrativo
    "¿Cuál es el propósito de un texto descriptivo?",  # describir o detallar
    "¿Cuál es el primer paso para hacer un resumen?",  # leer el texto completo
    "¿Qué tipo de lenguaje se utiliza en una exposición formal?",  # formal
    "¿Qué es un argumento en un debate o texto argumentativo?",  # afirmación respaldada por evidencias o razones
    # Nivel 2
    "¿Qué elementos componen una narrativa, además de la trama y los personajes?",  # entorno,tiempo y conflicto
    "En un debate, ¿cuál es el propósito de la presentación de argumentos?",  # persuadir a un público
    "¿Qué es un organizador gráfico y cómo se utiliza en la organización de información?",  # herramienta visual usada para representar ideas
    "¿Cuál es el propósito de una exposición informativa?",  # proporcionar información
    "¿Cuál es la importancia de la estructura en un texto argumentativo?",  # organiza y representa argumentos
    "¿Qué tipo de lenguaje se utiliza en un texto narrativo?",  # descriptivo y narrativo
    "En un debate, ¿qué es una contra-argumentación?",  # argumento que refuta
    "¿Por qué es importante seleccionar información relevante al hacer un resumen?",  # resumir la idea principal y puntos clave
    # Nivel 3
    "¿?",
    "¿?",
    "¿?",
    "¿?",
    "¿?",
    "¿?",
    "¿?",
    "¿?",
]

preguntas_Finn = [
    "Si tienes 3/4 de una pizza y comes la mitad de lo que tienes, ¿cuánta pizza has comido?",  # 3/8
    "Si tienes 0.5 dólares y le das a tu amigo 0.25 dólares, ¿cuánto dinero te queda?",  # 0.25 dólares
    "Si una docena de huevos cuesta $24, ¿cuánto cuesta cada huevo?",  # 2
    "Coloca el número siguiente del patrón: 2, 4, 6, ...",  # 8
    "¿Cuántas rectas paralelas puedes dibujar a otra recta en un plano?",  # Infinitas
    "¿Cuál es el resultado de 7^2?",  # 49
    "¿Cuál es el número entero neutro que está entre -2 y 3?",  # 0
    "Si 18 es el 10% de un número, ¿cuál es ese número?",  # 180
    # Nivel 2
    "Resta 1/3 de 2/5",  # 1/15
    "Si multiplicas 0.6 por 0.25, ¿cuál es el resultado?",  # 0.15
    "Si divides 7.5 entre 1.5, ¿cuál es el resultado?",  # 5
    "Encuentra la raíz cuadrada de 144.",  # 12
    "Si sumas -3 y 8, ¿cuál es el resultado?",  # 5
    "Si tienes un patrón de números impares crecientes, ¿cuál es el siguiente número después de 13?",  # 15
    "¿Cuántas rectas perpendiculares puedes dibujar a otra recta en un plano?",  # Infinitas
    "Si 15 es el 25% de un número, ¿cuál es ese número?",  # 60
    # Nivel 3
    "Realiza la operación: (0.75 * 0.2) + (0.3 * 0.5).",  # 0.18
    "Si divides 5 entre 1.25, ¿cuál es el resultado?",  # 4
    "Si tienes un patrón de números pares disminuyentes, ¿cuál es el siguiente número antes de 10?",  # 8
    "Si 80 es el 40% de un número, ¿cuál es ese número?",  # 200
    "¿Cuál es el resultado de 3^5?",  # 243
    "Si tienes 6 bolitas rojas y 4 bolitas verdes en una bolsa, ¿cuál es la razón de bolitas rojas a verdes?",  # 3:2
    "Si restas 6 de -8, ¿cuál es el resultado?",  # -14
    "Encuentra la raíz cuadrada de 225.",  # 15
]


def set_vidas(value):
    global vidas
    vidas = value


def get_CajaObstaculos():
    global cajaObstaculo
    return cajaObstaculo


def set_x(value):
    global x
    x = value


def set_CajaObstaculo(value):
    global cajaObstaculo
    cajaObstaculo = value


def set_puntos(val):
    global puntos
    puntos = val


def set_lvl(lvl):
    global nivel, numP
    nivel = lvl
    if lvl == 1:
        numP = 0
    if lvl == 2:
        numP = 8
    if lvl == 3:
        numP = 9


def get_Puntos():
    global puntos
    return puntos


def get_Vidas():
    global vidas
    return vidas


def get_numP():
    global numP
    return numP


def get_error():
    global err
    return err


def modificarPregunta():
    global numP
    numP += 1


def modificarPuntos():
    global puntos
    puntos += 10


def set_Respuesta(res):
    global respuesta
    respuesta = res


def validarRespuesta(ajolote, finn, mapache):
    global respuesta, err
    err = True
    if numP == 0:
        if (
            (
                ajolote
                and (
                    "ciudad de méxico" in respuesta.lower()
                    or "cdmx" in respuesta.lower()
                )
            )
            or (finn and ("3/8" in respuesta))
            or (
                mapache
                and (
                    "presentación oral" in respuesta.lower()
                    or "presentación escrita" in respuesta.lower()
                )
            )
        ):
            err = False
    elif numP == 1:
        if (
            (ajolote and ("pacífico" in respuesta.lower()))
            or (finn and ("0.25" in respuesta))
            or (mapache and ("discusión estructurada" in respuesta.lower()))
        ):
            err = False
    elif numP == 2:
        if (
            (ajolote and ("guadalupe victoria" in respuesta.lower()))
            or (finn and ("2" in respuesta))
            or (
                mapache
                and (
                    "persuadir" in respuesta.lower() or "convencer" in respuesta.lower()
                )
            )
        ):
            err = False
    elif numP == 3:
        if (
            (ajolote and ("chichén itzá" in respuesta.lower()))
            or (finn and ("8" in respuesta))
            or (mapache and ("texto narrativo" in respuesta.lower()))
        ):
            err = False
    elif numP == 4:
        if (
            (ajolote and ("independencia" in respuesta.lower()))
            or (finn and ("infinitas" in respuesta.lower()))
            or (
                mapache
                and (
                    "describir" in respuesta.lower() or "detallar" in respuesta.lower()
                )
            )
        ):
            err = False
    elif numP == 5:
        if (
            (ajolote and ("frida khalo" in respuesta.lower()))
            or (finn and ("49" in respuesta))
            or (mapache and ("leer texto completo" in respuesta.lower()))
        ):
            err = False
    elif numP == 6:
        if (
            (ajolote and ("usumacinta" in respuesta.lower()))
            or (finn and ("0" in respuesta))
            or (mapache and ("formal" in respuesta.lower()))
        ):
            err = False
    elif numP == 7:
        if (
            (ajolote and ("1910" in respuesta.lower()))
            or (finn and ("180" in respuesta.lower()))
            or (
                mapache
                and (
                    "afirmación respaldada por evidencias" in respuesta.lower()
                    or "información respaldada por razones" in respuesta.lower()
                )
            )
        ):
            err = False
    elif numP == 8:
        if (
            (ajolote and ("teotihuacana" in respuesta.lower()))
            or (finn and ("1/15" in respuesta))
            or (
                mapache
                and (
                    "entorno" in respuesta.lower()
                    and (
                        "tiempo" in respuesta.lower()
                        and ("conflicto" in respuesta.lower())
                    )
                )
            )
        ):
            err = False
    elif numP == 9:
        if (ajolote and ("peso mexicano" in respuesta.lower())) or (
            finn and ("0.15" in respuesta)
        ) or (mapache and ("persuadir a un público" in respuesta.lower())):
            err = False
    elif numP == 10:
        if (ajolote and ("venustiano carranza" in respuesta.lower())) or (
            finn and ("5" in respuesta)
        ) or (mapache and ("herramienta visual usada para representar ideas" in respuesta.lower())):
            err = False
    elif numP == 11:
        if (ajolote and ("batalla de puebla" in respuesta.lower())) or (
            finn and ("12" in respuesta)
        ) or (mapache and ("proporcionar información" in respuesta.lower())):
            err = False
    elif numP == 12:
        if (ajolote and ("sierra madre" in respuesta.lower())) or (
            finn and ("5" in respuesta)
        ) or (mapache and ()):
            err = False
    elif numP == 13:
        if (ajolote and ("1821" in respuesta)) or (finn and ("15" in respuesta)):
            err = False
    elif numP == 14:
        if (ajolote and ("tulum" in respuesta.lower())) or (
            finn and ("infinitas" in respuesta.lower())
        ):
            err = False
    elif numP == 15:
        if (ajolote and ("miguel hidalgo y costilla" in respuesta.lower())) or (
            finn and ("60" in respuesta)
        ):
            err = False


def set_golden_material():
    mat_ambient = [0.8, 0.6, 0.0, 1.0]
    mat_diffuse = [0.8, 0.6, 0.0, 1.0]
    mat_specular = [0.8, 0.8, 0.8, 1.0]
    shine = 51.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_red_material():
    mat_ambient = [0.81, 0.0, 0.0, 1.0]
    mat_diffuse = [0.815, 0.227, 0.545, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def levelCleared():
    global visible
    for i in range(len(visible)):
        if visible[i] == 1:
            return False

    return True


def interseccion(caja1, caja2):
    if abs(caja1.centro[0] - caja2.centro[0]) > (caja1.extend[0] + caja2.extend[0]):
        return False
    if abs(caja1.centro[1] - caja2.centro[1]) > (caja1.extend[1] + caja2.extend[1]):
        return False
    if abs(caja1.centro[2] - caja2.centro[2]) > (caja1.extend[2] + caja2.extend[2]):
        return False
    return True


def reducirVidas():
    global vidas
    vidas -= 1


def clearCaja():
    global cont, cajas, visible, vidas, numP
    cont = 0
    vidas = 3
    numP = 0
    for i in range(len(visible)):
        visible[i] = 1
    cajas.clear()


def crearCaja(centro):
    global cajas, cont
    caja = mBall(0.2, 0.2, 0.2, centro)
    if cont < 8:
        cajas.append(caja)
        cont += 1


def drawObstaculos(radius, y):
    global nivel, x
    if x >= -4 and x <= 4:
        x += 0.1
    else:
        x = -4
    set_red_material()
    glPushMatrix()
    glTranslate(x, y, 0)
    gluSphere(gluNewQuadric(), radius, 20, 20)  # Dibuja la esfera
    glPopMatrix()
    if nivel == 3:
        glPushMatrix()
        glTranslate(x, y, 0)
        gluSphere(gluNewQuadric(), radius, 20, 20)  # Dibuja la esfera
        glPopMatrix()


def drawNivel(ajolote, finn, mapache):
    global visible, cont, nivel, numP, x, cajaObstaculo
    radius = 0.2  # Radio de las esferas
    if finn:
        y = 0.7
    if mapache:
        y = 1
    if ajolote:
        y = 0.5
    if nivel == 2:
        drawObstaculos(radius, y)
        centro = [x, y, 0]
        cajaObstaculo = mBall(0.2, 0.2, 0.2, centro)
    if cont < 8:
        crearCaja((4, y, -1.5))
        crearCaja((-4.0, y, -1.5))
        crearCaja((0.0, y, 3.0))
        crearCaja((3.0, y, 2.5))
        crearCaja((1.0, y, -2.0))
        crearCaja((-3.0, y, 0.5))
        crearCaja((2.0, y, -3.0))
        crearCaja((-2.0, y, -4.0))
    for i in range(len(visible)):
        set_golden_material()
        if visible[i] == 1:
            glPushMatrix()
            if i == 0:
                glTranslate(4.0, y, -1.5)  # Aumenta la separación en X
            elif i == 1:
                glTranslate(-4.0, y, -1.5)  # Aumenta la separación en X
            elif i == 2:
                glTranslate(0.0, y, 3.0)  # Aumenta la separación en Z
            elif i == 3:
                glTranslate(3.0, y, 2.5)  # Aumenta la separación en Z
            elif i == 4:
                glTranslate(1.0, y, -2.0)  # Aumenta la separación en X
            elif i == 5:
                glTranslate(-3.0, y, 0.5)  # Aumenta la separación en X
            elif i == 6:
                glTranslate(2.0, y, -3.0)  # Aumenta la separación en Z
            elif i == 7:
                glTranslate(-2.0, y, -4.0)  # Aumenta la separación en Z
            gluSphere(gluNewQuadric(), radius, 20, 20)  # Dibuja la esfera
            glPopMatrix()
