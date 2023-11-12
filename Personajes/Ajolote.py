from OpenGL.GL import *
from OpenGL.GLU import *
import math
from mBall import mBall

centro = [0, 0.52, -0.01]
cajaCabeza = mBall(0.55, 0.55, 0.55, centro)


SLICES = 40
STACKS = 40
q = gluNewQuadric()


def dibujaAjolote(
    camina,
    habla,
    moverA,
    moverD,
    enojado,
    triste,
    muerto,
    ira,
    llorar,
    patasDelante,
    patasDetras,
    sacarLengua,
    mareado,
):
    gluQuadricDrawStyle(q, GLU_FILL)
    gluQuadricOrientation(q, GLU_OUTSIDE)
    gluQuadricNormals(q, GLU_SMOOTH)

    c = " "

    if camina:
        c = "C"
    elif habla:
        c = "H"
    elif moverA:
        c = "A"
    elif moverD:
        c = "D"
    elif enojado:
        c = "E"
    elif triste:
        c = "T"
    elif muerto:
        c = "M"
    elif ira:
        c = "I"
    elif llorar:
        c = "L"
    elif patasDelante:
        c = "P"
    elif patasDetras:
        c = "O"
    elif sacarLengua:
        c = "V"
    elif mareado:
        c = "K"

    if c == " ":
        dibujaCabeza(" ")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")

    if c == "C":
        dibujaCabeza(" ")
        dibujaCuerpo("C")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje("C")

    if c == "H":
        dibujaCabeza("H")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")

    if c == "A":
        dibujaCabeza(" ")
        dibujaCuerpo(" ")
        dibujaCola("A")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")

    if c == "D":
        dibujaCabeza(" ")
        dibujaCuerpo(" ")
        dibujaCola("D")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")

    if c == "E":
        dibujaCabeza("E")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")

    if c == "T":
        dibujaCabeza("T")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")

    if c == "M":
        dibujaCabeza("M")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")

    if c == "I":
        dibujaCabeza("I")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz("I")
        dibujaCuernoDr("I")
        dibujaMono()
        dibujaTraje(" ")
    if c == "L":
        dibujaCabeza("L")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")
    if c == "P":
        dibujaCabeza(" ")
        dibujaCuerpo("P")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje("P")
    if c == "O":
        dibujaCabeza(" ")
        dibujaCuerpo("O")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje("O")
    if c == "V":
        dibujaCabeza("V")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")
    if c == "K":
        dibujaCabeza("K")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")


def dibujaAjoloteJuego(x, y, z, camina, frente, izquierda, derecha):
    global centro, cajaCabeza
    glPushMatrix()
    glTranslate(x, y, z)
    centro = [x, y, z]
    cajaCabeza = mBall(0.55, 0.55, 0.55, centro)
    if frente:
        glRotate(180, 0.0, 1.0, 0.0)
    if izquierda:
        glRotate(-90, 0.0, 1.0, 0)
    if derecha:
        glRotate(90, 0.0, 1.0, 0)
    if camina:
        dibujaCabeza(" ")
        dibujaCuerpo("C")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje("C")
    else:
        dibujaCabeza(" ")
        dibujaCuerpo(" ")
        dibujaCola(" ")
        dibujaCuernoIz(" ")
        dibujaCuernoDr(" ")
        dibujaMono()
        dibujaTraje(" ")
    glPopMatrix()


def dibujaCabeza(tipo):
    if tipo == "E":
        set_black2_material()
        glPushMatrix()
        glScalef(0.25, 0.05, 0.05)
        glTranslatef(-1.4, 17.4, 6.7)
        glRotatef(-35, 0, 0, 1)
        
        glPopMatrix()
        glPushMatrix()
        glScalef(0.25, 0.05, 0.05)
        glTranslatef(1.0, 18.4, 6.7)
        glRotatef(35, 0, 0, 1)
        glRotatef(180, 0, 0, 1)
        
        glPopMatrix()
        # Craneo
        set_lightpink_material()
        glPushMatrix()
        glTranslatef(0.0, 0.52, -0.01)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()
        # Cara
        set_black_material()
        glPushMatrix()
        glTranslatef(0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(0.0, 0.59, 0.1)
        glRotatef(90, 1, 0, 0)
        draw_torus(0.3, 0.1, SLICES, STACKS)
        glPopMatrix()
    if tipo == "T":
        set_black2_material()
        glPushMatrix()
        glScalef(0.25, 0.05, 0.05)
        glTranslatef(-1.2, 17.4, 6.7)
        glRotatef(25, 0, 0, 1)
        
        glPopMatrix()
        glPushMatrix()
        glScalef(0.25, 0.05, 0.05)
        glTranslatef(1.7, 18.4, 6.7)
        glRotatef(-25, 0, 0, 1)
        glRotatef(180, 0, 0, 1)
        
        glPopMatrix()
        # CRANEO
        set_lightpink_material()
        glPushMatrix()
        glTranslatef(0.0, 0.52, -0.01)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()
        # CARA
        set_black_material()
        glPushMatrix()
        glTranslatef(0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(0.0, 0.59, 0.1)
        glRotatef(90, 1, 0, 0)
        draw_torus(0.3, 0.1, SLICES, STACKS)
        glPopMatrix()
    if tipo == "M":
        # CRANEO
        set_lightpink_material()
        glPushMatrix()
        glTranslatef(0.0, 0.52, -0.01)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()
        # CARA
        set_white_material()
        glPushMatrix()
        glTranslatef(0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        set_black_material()
        glPushMatrix()
        glTranslatef(0.0, 0.59, 0.1)
        glRotatef(90, 1, 0, 0)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0, 0.05, -0.35)
        draw_torus(0.1, 0.05, SLICES, STACKS)
        set_red_material()
        glRotatef(180, 1, 0, 0)
        glTranslatef(0, 0, 0.01)
        gluCylinder(q, 0.1, 0.05, 0.1, SLICES, STACKS)
        glRotatef(180, 1, 0, 0)
        glTranslatef(0, 0, -0.1)
        gluDisk(q, 0, 0.05, SLICES, STACKS)
        glPopMatrix()

    if tipo == " ":
        # CRANEO
        set_lightpink_material()
        glPushMatrix()
        glTranslatef(0.0, 0.52, -0.01)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()
        # CARA
        set_black_material()
        glPushMatrix()
        glTranslatef(0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(0.0, 0.59, 0.1)
        glRotatef(90, 1, 0, 0)
        draw_torus(0.3, 0.1, SLICES, STACKS)
        glPopMatrix()

    if tipo == "H":
        # CRANEO
        set_lightpink_material()
        glPushMatrix()
        glTranslatef(0.0, 0.52, -0.01)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()
        # CARA
        set_black_material()
        glPushMatrix()
        glTranslatef(0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(0.0, 0.59, 0.1)
        glRotatef(90, 1, 0, 0)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0, 0.05, -0.35)
        draw_torus(0.1, 0.05, SLICES, STACKS)
        glPopMatrix()
    if tipo == "I":
        set_black2_material()
        glPushMatrix()
        glScalef(0.25, 0.05, 0.05)
        glTranslatef(-1.4, 17.4, 6.7)
        glRotatef(-35, 0, 0, 1)
        
        glPopMatrix()
        glPushMatrix()
        glScalef(0.25, 0.05, 0.05)
        glTranslatef(1.0, 18.4, 6.7)
        glRotatef(35, 0, 0, 1)
        glRotatef(180, 0, 0, 1)
        
        glPopMatrix()
        # CRANEO
        set_red_material()
        glPushMatrix()
        glTranslatef(0.0, 0.52, -0.01)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()
        # CARA
        set_black_material()
        glPushMatrix()
        glTranslatef(0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(0.0, 0.59, 0.1)
        glRotatef(90, 1, 0, 0)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0, 0.05, -0.35)
        draw_torus(0.1, 0.05, SLICES, STACKS)
        glPopMatrix()

    if tipo == "L":
        set_black2_material()
        glPushMatrix()
        glScalef(0.25, 0.05, 0.05)
        glTranslatef(-1.2, 17.4, 6.7)
        glRotatef(25, 0, 0, 1)
        
        glPopMatrix()
        glPushMatrix()
        glScalef(0.25, 0.05, 0.05)
        glTranslatef(1.7, 18.4, 6.7)
        glRotatef(-25, 0, 0, 1)
        glRotatef(180, 0, 0, 1)
        
        glPopMatrix()
        # CRANEO
        set_lightpink_material()
        glPushMatrix()
        glTranslatef(0.0, 0.52, -0.01)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()
        # CARA
        set_black_material()
        glPushMatrix()
        glTranslatef(0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glTranslatef(0.05, -0.08, 0.09)
        set_cyan_material()
        gluSphere(q, 0.04, SLICES, STACKS)
        glTranslatef(0.0, -0.08, 0.0)
        gluSphere(q, 0.04, SLICES, STACKS)
        glTranslatef(0.0, -0.08, 0.0)
        gluSphere(q, 0.04, SLICES, STACKS)
        glPopMatrix()
        set_black_material()
        glPushMatrix()
        glTranslatef(-0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glTranslatef(-0.05, -0.08, 0.09)
        set_cyan_material()
        gluSphere(q, 0.04, SLICES, STACKS)
        glTranslatef(0.0, -0.08, 0.0)
        gluSphere(q, 0.04, SLICES, STACKS)
        glTranslatef(0.0, -0.08, 0.0)
        gluSphere(q, 0.04, SLICES, STACKS)
        glPopMatrix()
        set_black_material()
        glPushMatrix()
        glTranslatef(0.0, 0.59, 0.1)
        glRotatef(90, 1, 0, 0)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0, 0.05, -0.35)
        draw_torus(0.07, 0.05, SLICES, STACKS)
        glPopMatrix()

    if tipo == "K":
        # CRANEO
        set_green2_material()
        glPushMatrix()
        glTranslatef(0.0, 0.52, -0.01)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()
        set_white_material()
        glPushMatrix()
        glTranslatef(0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        set_black_material()
        glPushMatrix()
        glTranslatef(0.0, 0.59, 0.1)
        glRotatef(90, 1, 0, 0)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0, 0.05, -0.35)
        draw_torus(0.1, 0.05, SLICES, STACKS)
        set_green_material()
        glRotatef(180, 1, 0, 0)
        glTranslatef(0, 0, 0.01)
        gluCylinder(q, 0.1, 0.05, 0.1, SLICES, STACKS)
        glRotatef(180, 1, 0, 0)
        glTranslatef(0, 0, -0.1)
        gluDisk(q, 0, 0.05, SLICES, STACKS)
        glPopMatrix()

    if tipo == "V":
        # CRANEO
        set_lightpink_material()
        glPushMatrix()
        glTranslatef(0.0, 0.52, -0.01)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()
        # CARA
        set_black_material()
        glPushMatrix()
        glTranslatef(0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.2, 0.72, 0.3)
        gluSphere(q, 0.1, SLICES, STACKS)
        glPopMatrix()
        set_black_material()
        glPushMatrix()
        glTranslatef(0.0, 0.59, 0.1)
        glRotatef(90, 1, 0, 0)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0, 0.05, -0.35)
        draw_torus(0.1, 0.05, SLICES, STACKS)
        set_red_material()
        glRotatef(180, 1, 0, 0)
        glTranslatef(0, 0, 0.01)
        gluCylinder(q, 0.1, 0.05, 0.1, SLICES, STACKS)
        glRotatef(180, 1, 0, 0)
        glTranslatef(0, 0, -0.1)
        gluDisk(q, 0, 0.05, SLICES, STACKS)
        glPopMatrix()


def dibujaCuerpo(tipo):
    set_lightpink_material()
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslatef(0.0, 0.0, -0.5)
    glRotatef(90, 1, 0, 0)
    gluCylinder(q, 0.5, 0.5, 1, SLICES, STACKS)
    glRotatef(180, 1, 0, 0)
    glTranslatef(0, 0, -1.05)
    gluDisk(q, 0, 0.5, SLICES, STACKS)
    glPopMatrix()

    if tipo == "C":
        # BRAZO DERECHO
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.8)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        glTranslatef(0.0, 0.2, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.1, 0.1, 0.5, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO IZQUIERDO
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.8)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        glTranslatef(0.0, -0.2, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.1, 0.1, 0.5, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO DERECHO INFERIOR
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.7)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        glTranslatef(0.0, 0.2, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.1, 0.1, 0.4, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO IZQUIERDO INFERIOR
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.7)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        glTranslatef(0.0, -0.2, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.1, 0.1, 0.4, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
    if tipo == " ":
        # BRAZO DERECHO
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.8)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        gluCylinder(q, 0.1, 0.1, 0.5, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO IZQUIERDO
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.8)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        gluCylinder(q, 0.1, 0.1, 0.5, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO DERECHO INFERIOR
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.7)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        gluCylinder(q, 0.1, 0.1, 0.4, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO IZQUIERDO INFERIOR
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.7)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        gluCylinder(q, 0.1, 0.1, 0.4, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
    if tipo == "P":
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.8)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        glTranslatef(0.0, 0.2, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.1, 0.1, 0.5, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO IZQUIERDO
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.8)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        glTranslatef(0.0, -0.2, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.1, 0.1, 0.5, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO DERECHO INFERIOR
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.7)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        gluCylinder(q, 0.1, 0.1, 0.4, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO IZQUIERDO INFERIOR
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.7)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        gluCylinder(q, 0.1, 0.1, 0.4, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
    elif tipo == "O":
        # BRAZO DERECHO INFERIOR
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.7)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        glTranslatef(0.0, 0.2, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.1, 0.1, 0.4, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO IZQUIERDO INFERIOR
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.7)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        glTranslatef(0.0, -0.2, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.1, 0.1, 0.4, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO DERECHO
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.8)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        gluCylinder(q, 0.1, 0.1, 0.5, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()
        # BRAZO IZQUIERDO
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.8)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        gluCylinder(q, 0.1, 0.1, 0.5, SLICES, STACKS)
        glRotatef(180, 0, 1, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(35, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glRotatef(-70, 1, 0, 0)
        gluCylinder(q, 0.1, 0.0, 0.15, SLICES, STACKS)
        glPopMatrix()


def dibujaCola(tipo):
    if tipo == " ":
        set_lightpink_material()
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        glTranslatef(0.0, 0.0, 0.5)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0.0, -1.0, 1.0)
        gluCylinder(q, 0.5, 0.0, 1.5, SLICES, STACKS)
        glPopMatrix()
    if tipo == "A":
        set_lightpink_material()
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        glTranslatef(0.0, 0.0, 0.5)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0.0, -1.0, 1.0)
        glRotatef(25, 0, 1, 0)
        gluCylinder(q, 0.5, 0.0, 1.5, SLICES, STACKS)
        glPopMatrix()

    if tipo == "D":
        set_lightpink_material()
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        glTranslatef(0.0, 0.0, 0.5)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0.0, -1.0, 1.0)
        glRotatef(-25, 0, 1, 0)
        gluCylinder(q, 0.5, 0.0, 1.5, SLICES, STACKS)
        glPopMatrix()


def dibujaCuernoIz(tipo):
    if tipo == "I":
        set_red2_material()
    else:
        set_pink_material()

    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    glRotatef(90, 0, 1, 0)
    glRotatef(45, 1, 0, 0)
    glTranslatef(0.0, -0.4, 0.85)
    gluCylinder(q, 0.05, 0.0, 0.3, SLICES, STACKS)
    glPopMatrix()
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    glRotatef(90, 0, 1, 0)
    glRotatef(45, 1, 0, 0)
    glTranslatef(0.0, -0.3, 0.85)
    gluCylinder(q, 0.05, 0.0, 0.2, SLICES, STACKS)
    glPopMatrix()


def dibujaCuernoDr(tipo):
    if tipo == "I":
        set_red2_material()
    else:
        set_pink_material()

    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    glRotatef(90, 0, 1, 0)
    glRotatef(45, 1, 0, 0)
    glRotatef(90, 1, 0, 0)
    glTranslatef(0.0, 0.4, 0.85)
    gluCylinder(q, 0.05, 0.0, 0.3, SLICES, STACKS)
    glPopMatrix()
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    glRotatef(90, 0, 1, 0)
    glRotatef(45, 1, 0, 0)
    glRotatef(90, 1, 0, 0)
    glTranslatef(0.0, 0.3, 0.85)
    gluCylinder(q, 0.05, 0.0, 0.2, SLICES, STACKS)
    glPopMatrix()


def dibujaMono():
    # PARTE DERECHA
    set_green_material()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glRotatef(5, 1, 0, 0)
    glTranslatef(-0.51, 0.55, -0.55)
    glRotatef(90, 0, 0, 1)
    glTranslatef(-0.55, -0.5, 0)
    gluCylinder(q, 0.05, 0, 0.5, SLICES, STACKS)
    glPopMatrix()
    set_white_material()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslatef(-0.51, 0.55, -0.5)
    glRotatef(90, 0, 0, 1)
    glTranslatef(-0.55, -0.5, -0.05)
    gluCylinder(q, 0.05, 0, 0.5, SLICES, STACKS)
    glPopMatrix()
    set_red_material()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glRotatef(-5, 1, 0, 0)
    glTranslatef(-0.51, 0.55, -0.45)
    glRotatef(90, 0, 0, 1)
    glTranslatef(-0.55, -0.5, -0.1)
    gluCylinder(q, 0.05, 0, 0.5, SLICES, STACKS)
    glPopMatrix()
    # PARTE IZQUIERDA
    set_green_material()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glRotatef(5, 1, 0, 0)
    glTranslatef(-0.51, 0.55, 0.45)
    glRotatef(180, 0, 1, 0)
    glRotatef(90, 0, 0, 1)
    glTranslatef(-0.55, 0.5, -0.05)
    gluCylinder(q, 0.05, 0, 0.5, SLICES, STACKS)
    glPopMatrix()
    set_white_material()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslatef(-0.51, 0.55, 0.50)
    glRotatef(180, 0, 1, 0)
    glRotatef(90, 0, 0, 1)
    glTranslatef(-0.55, 0.5, 0)
    gluCylinder(q, 0.05, 0, 0.5, SLICES, STACKS)
    glPopMatrix()
    set_red_material()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glRotatef(-5, 1, 0, 0)
    glTranslatef(-0.51, 0.55, 0.55)
    glRotatef(180, 0, 1, 0)
    glRotatef(90, 0, 0, 1)
    glTranslatef(-0.55, 0.5, 0.05)
    gluCylinder(q, 0.05, 0, 0.5, SLICES, STACKS)
    glPopMatrix()


def dibujaTraje(tipo):
    if tipo == " ":
        # MANGA CAM==A DERECHA
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.75)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE DERECHA
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.7)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAM==A DERECHA INFERIOR
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.65)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE DERECHA INFERIOR
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.6)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAM==A IZQUIERDA
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.75)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE IZQUIERDA
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.7)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAM==A IZQUIERDA INFERIOR
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.65)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE IZQUIERDA INFERIOR
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.6)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()

    if tipo == "C":
        # MANGA CAM==A DERECHA
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.75)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        glTranslatef(0.0, 0.18, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE DERECHA
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.7)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        glTranslatef(0.0, 0.16, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAM==A DERECHA INFERIOR
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.65)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        glTranslatef(0.0, 0.18, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE DERECHA INFERIOR
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.6)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        glTranslatef(0.0, 0.16, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAM==A IZQUIERDA
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.75)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        glTranslatef(0.0, -0.18, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE IZQUIERDA
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.7)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        glTranslatef(0.0, -0.16, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAM==A IZQUIERDA INFERIOR
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.65)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        glTranslatef(0.0, -0.18, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE IZQUIERDA INFERIOR
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.6)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        glTranslatef(0.0, -0.16, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()

    if tipo == "P":
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.75)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        glTranslatef(0.0, 0.18, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE DERECHA
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.7)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        glTranslatef(0.0, 0.16, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAMISA IZQUIERDA
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.75)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        glTranslatef(0.0, -0.18, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE IZQUIERDA
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.7)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        glTranslatef(0.0, -0.16, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAMISA DERECHA INFERIOR
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.65)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE DERECHA INFERIOR
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.6)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAMISA IZQUIERDA INFERIOR
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.65)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE IZQUIERDA INFERIOR
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.6)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()

    if tipo == "O":
        # MANGA CAMISA DERECHA INFERIOR
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.65)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        glTranslatef(0.0, 0.18, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE DERECHA INFERIOR
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, -0.6)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, -1.2, -0.0)
        glTranslatef(0.0, 0.16, 0)
        glRotatef(30, 100, 0, 0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAMISA IZQUIERDA INFERIOR
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.65)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        glTranslatef(0.0, -0.18, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE IZQUIERDA INFERIOR
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, -0.4, 0.6)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.8, 1.2, -0.0)
        glTranslatef(0.0, -0.16, 0)
        glRotatef(-30, 100, 0, 0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAMISA DERECHA
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.75)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE DERECHA
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, -0.7)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, -0.4, -0.0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA CAMISA IZQUIERDA
        set_white_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.75)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        gluCylinder(q, 0.11, 0.11, 0.4, SLICES, STACKS)
        glPopMatrix()
        # MANGA TRAJE IZQUIERDA
        set_black_material()
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-0.3, 0.4, 0.7)
        glRotated(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        glTranslatef(0.0, 0.4, -0.0)
        gluCylinder(q, 0.12, 0.12, 0.4, SLICES, STACKS)
        glPopMatrix()

    # CUERPO NEGRO
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslatef(0.0, 0.01, -0.5)
    glRotatef(90, 1, 0, 0)
    gluCylinder(q, 0.52, 0.52, 1.1, SLICES, STACKS)
    glPopMatrix()
    # CUERPO ROJO
    set_red_material()
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslatef(0.0, 0.01, -0.1)
    glRotatef(90, 1, 0, 0)
    glTranslatef(0.0, -0.4, 0.5)
    gluCylinder(q, 0.53, 0.53, 0.3, SLICES, STACKS)
    glPopMatrix()
    # DISK
    set_white_material()
    glPushMatrix()
    glTranslatef(0.0, 0.5, 0.01)
    glRotatef(90, 1, 0, 0)
    glRotatef(90, 1, 0, 0)
    draw_torus(0.5, 0.05, SLICES, STACKS)
    glPopMatrix()


def set_darkyellow_material():
    mat_ambient = [0.823, 0.729, 0.0, 1.0]
    mat_diffuse = [0.815, 0.227, 0.545, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_black_material():
    mat_ambient = [0.0, 0.0, 0.0, 1.0]
    mat_diffuse = [0, 0, 0, 1]
    mat_specular = [0.9, 0.8, 0.9, 1.0]
    shine = 128

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_black2_material():
    mat_ambient = [0.0, 0.0, 0.0, 1.0]
    mat_diffuse = [0, 0, 0, 1]
    mat_specular = [0, 0, 0, 1.0]
    shine = 128

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_white_material():
    mat_ambient = [1.0, 1.0, 1.0, 1.0]
    mat_diffuse = [0.815, 0.227, 0.545, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_red_material():
    mat_ambient = [1.0, 0.0, 0.0, 1.0]
    mat_diffuse = [0.815, 0.227, 0.545, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_green_material():
    mat_ambient = [0.0, 0.501, 0.0, 1.0]
    mat_diffuse = [0.815, 0.227, 0.545, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_pink_material():
    mat_ambient = [0.815, 0.227, 0.545, 1.0]
    mat_diffuse = [0.815, 0.227, 0.545, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_green2_material():
    mat_ambient = [0.266, 1.0, 0.164, 1.0]
    mat_diffuse = [0.94509, 0.81960, 0.94901, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_lightpink_material():
    mat_ambient = [1.0, 0.501, 0.992, 1.0]
    mat_diffuse = [0.94509, 0.81960, 0.94901, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_red2_material():
    mat_ambient = [0.81, 0.0, 0.0, 1.0]
    mat_diffuse = [0.815, 0.227, 0.545, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_cyan_material():
    mat_ambient = [0.0, 0.854, 0.956, 1.0]
    mat_diffuse = [0.94509, 0.81960, 0.94901, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def draw_torus(R, r, N, n):
    maxn = 1000
    n = min(n, maxn - 1)
    N = min(N, maxn - 1)
    rr = 1.5 * r
    dv = 2 * math.pi / n
    dw = 2 * math.pi / N
    v = 0.0
    w = 0.0

    while w < 2 * math.pi + dw:
        v = 0.0
        glBegin(GL_TRIANGLE_STRIP)
        while v < 2 * math.pi + dv:
            glNormal3d(
                (R + rr * math.cos(v)) * math.cos(w)
                - (R + r * math.cos(v)) * math.cos(w),
                (R + rr * math.cos(v)) * math.sin(w)
                - (R + r * math.cos(v)) * math.sin(w),
                rr * math.sin(v) - r * math.sin(v),
            )
            glVertex3d(
                (R + r * math.cos(v)) * math.cos(w),
                (R + r * math.cos(v)) * math.sin(w),
                r * math.sin(v),
            )

            glNormal3d(
                (R + rr * math.cos(v + dv)) * math.cos(w + dw)
                - (R + r * math.cos(v + dv)) * math.cos(w + dw),
                (R + rr * math.cos(v + dv)) * math.sin(w + dw)
                - (R + r * math.cos(v + dv)) * math.sin(w + dw),
                rr * math.sin(v + dv) - r * math.sin(v + dv),
            )
            glVertex3d(
                (R + r * math.cos(v + dv)) * math.cos(w + dw),
                (R + r * math.cos(v + dv)) * math.sin(w + dw),
                r * math.sin(v + dv),
            )

            v += dv

        glEnd()
        w += dw



