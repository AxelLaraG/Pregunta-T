from OpenGL.GL import *
from OpenGL.GLU import *
import math
from mBall import mBall

centro = [0, 0.0, 0]
cajaCabeza = mBall(1, 1, 1, centro)

SLICES = 40
STACKS = 40
q = gluNewQuadric()


def drawMapache(
    original,
    chiquito,
    levantarBrazo,
    levantarBrazos,
    enojado,
    mueca,
    llorar,
    emocionado,
    confundido,
):
    gluQuadricDrawStyle(q, GLU_FILL)
    gluQuadricOrientation(q, GLU_OUTSIDE)
    gluQuadricNormals(q, GLU_SMOOTH)
    x = " "

    if original:  ##queda
        x = "O"
    elif chiquito:  ##queda
        x = "C"
    elif levantarBrazo:  ##queda
        x = "R"
    elif levantarBrazos:  ##queda
        x = "L"
    elif enojado:  ##queda
        x = "A"
    elif mueca:  ##queda
        x = "S"
    elif llorar:  ##queda
        x = "Y"
    elif emocionado:  ##queda
        x = "N"
    elif confundido:  ##queda
        x = "U"

    if x == " " or x == "O":
        dibujaCara(" ")
        dibujaBrazos(" ")
        dibujaPiernas(" ")
        dibujaPies(" ")
        dibujaCuerpo(" ")

    if x == "C":
        dibujaCara("C")
        dibujaBrazos("C")
        dibujaPiernas(" ")
        dibujaPies(" ")
        dibujaCuerpo("C")

    if x == "R":
        dibujaCara(" ")
        dibujaBrazos("R")
        dibujaPiernas(" ")
        dibujaPies(" ")
        dibujaCuerpo(" ")

    if x == "L":
        dibujaCara(" ")
        dibujaBrazos("L")
        dibujaPiernas(" ")
        dibujaPies(" ")
        dibujaCuerpo(" ")

    if x == "A":
        dibujaCara("A")
        dibujaBrazos(" ")
        dibujaPiernas(" ")
        dibujaPies(" ")
        dibujaCuerpo(" ")

    if x == "S":
        dibujaCara("S")
        dibujaBrazos(" ")
        dibujaPiernas(" ")
        dibujaPies(" ")
        dibujaCuerpo(" ")

    if x == "Y":
        dibujaCara("Y")
        dibujaBrazos(" ")
        dibujaPiernas(" ")
        dibujaPies(" ")
        dibujaCuerpo(" ")

    if x == "N":
        dibujaCara("N")
        dibujaBrazos(" ")
        dibujaPiernas(" ")
        dibujaPies(" ")
        dibujaCuerpo(" ")

    if x == "U":
        dibujaCara("U")
        dibujaBrazos(" ")
        dibujaPiernas(" ")
        dibujaPies(" ")
        dibujaCuerpo(" ")


def dibujaMapacheJuego(x, y, z, frente, izquierda, derecha):
    global centro, cajaCabeza
    glPushMatrix()
    glTranslate(x, y, z)
    centro = [x, y, z]
    cajaCabeza = mBall(1, 1, 1, centro)
    if frente:
        glRotate(180, 0.0, 1.0, 0.0)
    if izquierda:
        glRotate(-90, 0.0, 1.0, 0)
    if derecha:
        glRotate(90, 0.0, 1.0, 0)
    dibujaCara("C")
    dibujaBrazos("C")
    dibujaPiernas(" ")
    dibujaPies(" ")
    dibujaCuerpo("C")
    glPopMatrix()


def dibujaCuerpo(tipo):  # Funcion para crear el cuerpo
    if tipo == " ":  # original
        set_light_grey_material()

        glPushMatrix()  # cabeza
        glTranslatef(0, 2, 0)
        glRotatef(90, 0, 1, 0)
        gluSphere(q, 0.8, SLICES, STACKS)
        glPopMatrix()

        set_light_grey_material()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(0, 0.0, 0)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(q, 2, 0.8, 3.5, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()  ##pancita
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(0.0, 0.0, 0)
        glRotatef(-90, 1, 0, 0)
        draw_half_sphere(2.7, 32, 16)
        glPopMatrix()

    if tipo == "C":
        set_light_grey_material()

        glPushMatrix()  # cabeza
        glTranslatef(0, 1, 0)
        glRotatef(90, 0, 1, 0)
        gluSphere(q, 0.8, SLICES, STACKS)
        glPopMatrix()

        set_light_grey_material()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(0, -2.0, 0)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(q, 2, 0.8, 3.5, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()  ##pancita
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(0.0, -2.0, 0)
        glRotatef(-90, 1, 0, 0)
        draw_half_sphere(2.6, 32, 16)
        glPopMatrix()


def dibujaPiernas(tipo):
    if tipo == " ":
        set_light_grey_material()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1, -1.0, 0)
        glRotatef(90, 1, 0, 0)
        gluCylinder(q, 0.3, 0.4, 2.5, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(1, -1.0, 0)
        glRotatef(90, 1, 0, 0)
        gluCylinder(q, 0.3, 0.4, 2.5, SLICES, STACKS)
        glPopMatrix()

    # if tipo == "S":
    # if tipo == "C":
    # if tipo == "A":
    # elif tipo == "D":


def dibujaBrazos(tipo):
    if tipo == " ":
        set_light_grey_material()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(1.0, 3.3, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(62, 1, 0, 0)
        gluCylinder(q, 0.2, 0.5, 2.7, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.0, 3.3, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(118, 1, 0, 0)
        gluCylinder(q, 0.2, 0.5, 2.7, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(-3.0, 1.3, 0)
        glRotatef(90, 0, 1, 0)
        glRotatef(-62, 1, 0, 0)
        draw_half_sphere(0.7, 32, 16)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(3.0, 1.3, 0)
        glRotatef(90, 0, 1, 0)
        glRotatef(-118, 1, 0, 0)
        draw_half_sphere(0.7, 32, 16)
        glPopMatrix()

    if tipo == "C":
        set_light_grey_material()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(1.0, 0.5, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(62, 1, 0, 0)
        gluCylinder(q, 0.2, 0.5, 1.7, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.0, 0.5, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(118, 1, 0, 0)
        gluCylinder(q, 0.2, 0.5, 1.7, SLICES, STACKS)
        glPopMatrix()

        set_black_material()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(-2.25, -1.45, 0)
        glRotatef(90, 0, 1, 0)
        glRotatef(-62, 1, 0, 0)
        draw_half_sphere(0.7, 32, 16)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(2.25, -1.45, 0)
        glRotatef(90, 0, 1, 0)
        glRotatef(-118, 1, 0, 0)
        draw_half_sphere(0.7, 32, 16)
        glPopMatrix()

    if tipo == "R":
        set_light_grey_material()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(1.0, 3.3, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(62, 1, 0, 0)
        gluCylinder(q, 0.2, 0.5, 2.7, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.0, 3.0, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(210, 1, 0, 0)
        gluCylinder(q, 0.2, 0.5, 2.7, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(-4.3, 5.7, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(40, 1, 0, 0)
        draw_half_sphere(0.7, 32, 16)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(3.0, 1.3, 0)
        glRotatef(90, 0, 1, 0)
        glRotatef(-118, 1, 0, 0)
        draw_half_sphere(0.7, 32, 16)
        glPopMatrix()

    if tipo == "L":
        set_light_grey_material()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.0, 3.0, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(210, 1, 0, 0)
        gluCylinder(q, 0.2, 0.5, 2.7, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(-4.3, 5.7, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(40, 1, 0, 0)
        draw_half_sphere(0.7, 32, 16)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(1.0, 3.0, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(330, 1, 0, 0)
        gluCylinder(q, 0.2, 0.5, 2.7, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(4.3, 5.7, 0.0)
        glRotatef(90, 0, 1, 0)
        glRotatef(140, 1, 0, 0)
        draw_half_sphere(0.7, 32, 16)
        glPopMatrix()


def dibujaCara(tipo):
    if (
        tipo == " "
        or tipo == "H"
        or tipo == "A"
        or tipo == "U"
        or tipo == "S"
        or tipo == "Y"
        or tipo == "M"
        or tipo == "N"
        or tipo == "D"
        or tipo == "F"
        or tipo == "L"
        or tipo == "Q"
    ):
        set_black_material()

        glPushMatrix()  # pupila izquiero
        glTranslatef(-0.3, 2.0, 0.65)
        gluSphere(q, 0.2, SLICES, STACKS)
        glPopMatrix()

        set_black_material()
        glPushMatrix()  # pupila derecha
        glTranslatef(0.3, 2.0, 0.65)
        gluSphere(q, 0.2, SLICES, STACKS)
        glPopMatrix()

        ##orejas
        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.9, 7.0, 0.1)
        glRotatef(90, 0, 1, 0)
        glRotatef(45, 1, 0, 0)
        gluCylinder(q, 0.1, 0.4, 1.2, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(1.9, 7.0, 0.1)
        glRotatef(90, 0, 1, 0)
        glRotatef(135, 1, 0, 0)
        gluCylinder(q, 0.1, 0.4, 1.2, SLICES, STACKS)
        glPopMatrix()

        ##nariz
        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(0.0, 3.5, 1.6)
        glRotatef(90, 0, 1, 0)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(q, 0.09, 0.7, 0.8, SLICES, STACKS)
        glPopMatrix()

        set_grey_material()

        glPushMatrix()
        glTranslatef(0.0, 1.8, 0.3)
        glRotatef(30, 1, 0, 0)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()  # ojo derecho
        glTranslatef(0.3, 2.0, 0.4)
        gluSphere(q, 0.4, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()  # ojo izquiero
        glTranslatef(-0.3, 2.0, 0.4)
        gluSphere(q, 0.4, SLICES, STACKS)
        glPopMatrix()

        ##bigotes
        set_white_material()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.2, 3.8, 1.7)
        glRotatef(90, 0, 1, 0)
        gluCylinder(q, 0.03, 0.03, 2.5, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.2, 3.5, 1.7)
        glRotatef(90, 0, 1, 0)
        glRotatef(345, 1, 0, 0)
        gluCylinder(q, 0.03, 0.03, 2.5, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.2, 4.1, 1.7)
        glRotatef(90, 0, 1, 0)
        glRotatef(11, 1, 0, 0)
        gluCylinder(q, 0.03, 0.03, 2.5, SLICES, STACKS)
        glPopMatrix()

        if tipo == "A":
            set_black_material()
            ##cejas
            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(-1.2, 5.9, 1.8)
            glRotatef(90, 0, 1, 0)
            glRotatef(20, 1, 0, 0)
            gluCylinder(q, 0.1, 0.1, 1.2, SLICES, STACKS)
            glPopMatrix()

            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(0.2, 5.5, 1.8)
            glRotatef(90, 0, 1, 0)
            glRotatef(-20, 1, 0, 0)
            gluCylinder(q, 0.1, 0.1, 1.2, SLICES, STACKS)
            glPopMatrix()

        if tipo == "U":
            set_black_material()
            ##cejas
            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(-1.2, 5.9, 1.8)
            glRotatef(90, 0, 1, 0)
            gluCylinder(q, 0.1, 0.1, 1.2, SLICES, STACKS)
            glPopMatrix()

            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(0.2, 5.5, 1.8)
            glRotatef(90, 0, 1, 0)
            gluCylinder(q, 0.1, 0.1, 1.2, SLICES, STACKS)
            glPopMatrix()

        if tipo == "S":
            set_black_material()
            ##cejas
            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(-1.2, 6.0, 1.8)
            glRotatef(90, 0, 1, 0)
            gluCylinder(q, 0.1, 0.1, 1.0, SLICES, STACKS)
            glPopMatrix()

            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(0.2, 6.0, 1.8)
            glRotatef(90, 0, 1, 0)
            gluCylinder(q, 0.1, 0.1, 1.0, SLICES, STACKS)
            glPopMatrix()

            set_light_pink_material()

            glPushMatrix()
            glScalef(0.3, 0.3, 0.3)
            glTranslatef(0.0, 5.0, 2.3)
            glRotatef(180, 1, 0, 0)
            draw_half_sphere(0.55, 32, 16)
            glPopMatrix()

        if tipo == "Y":
            set_light_blue_material()

            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(0.8, 4.8, 2.1)
            glRotatef(90, 1, 0, 0)
            gluCylinder(q, 0.2, 0.2, 1.2, SLICES, STACKS)
            glPopMatrix()

            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(-0.8, 4.8, 2.1)
            glRotatef(90, 1, 0, 0)
            gluCylinder(q, 0.2, 0.2, 1.2, SLICES, STACKS)
            glPopMatrix()

        if tipo == "N":
            set_purple_material()

            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(-0.78, 5.9, 1.9)
            glRotatef(90, 0, 1, 0)
            glRotatef(90, 1, 0, 0)
            gluCylinder(q, 0.0, 0.4, 0.7, SLICES, STACKS)
            glPopMatrix()

            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(-0.78, 4.0, 1.9)
            glRotatef(90, 0, 1, 0)
            glRotatef(-90, 1, 0, 0)
            gluCylinder(q, 0.0, 0.4, 0.7, SLICES, STACKS)
            glPopMatrix()

            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(0.78, 5.9, 1.9)
            glRotatef(90, 0, 1, 0)
            glRotatef(90, 1, 0, 0)
            gluCylinder(q, 0.0, 0.4, 0.7, SLICES, STACKS)
            glPopMatrix()

            glPushMatrix()
            glScalef(0.4, 0.4, 0.4)
            glTranslatef(0.78, 4.0, 1.9)
            glRotatef(90, 0, 1, 0)
            glRotatef(-90, 1, 0, 0)
            gluCylinder(q, 0.0, 0.4, 0.7, SLICES, STACKS)
            glPopMatrix()

            glPushMatrix()  # pupila izquiero
            glTranslatef(-0.3, 2.0, 0.75)
            gluSphere(q, 0.2, SLICES, STACKS)
            glPopMatrix()

            glPushMatrix()  # pupila derecha
            glTranslatef(0.3, 2.0, 0.75)
            gluSphere(q, 0.2, SLICES, STACKS)
            glPopMatrix()

    if tipo == "C":
        set_black_material()

        glPushMatrix()  # pupila izquiero
        glTranslatef(-0.3, 0.9, 0.65)
        gluSphere(q, 0.2, SLICES, STACKS)
        glPopMatrix()

        set_black_material()
        glPushMatrix()  # pupila derecha
        glTranslatef(0.3, 0.9, 0.65)
        gluSphere(q, 0.2, SLICES, STACKS)
        glPopMatrix()

        ##orejas
        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.9, 4.5, 0.1)
        glRotatef(90, 0, 1, 0)
        glRotatef(45, 1, 0, 0)
        gluCylinder(q, 0.1, 0.4, 1.2, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(1.9, 4.5, 0.1)
        glRotatef(90, 0, 1, 0)
        glRotatef(135, 1, 0, 0)
        gluCylinder(q, 0.1, 0.4, 1.2, SLICES, STACKS)
        glPopMatrix()

        ##nariz
        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(0.0, 1.12, 1.6)
        glRotatef(90, 0, 1, 0)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(q, 0.09, 0.55, 0.5, SLICES, STACKS)
        glPopMatrix()

        set_grey_material()

        glPushMatrix()
        glTranslatef(0.0, 0.82, 0.3)
        glRotatef(30, 1, 0, 0)
        gluSphere(q, 0.5, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()  # ojo derecho
        glTranslatef(0.3, 0.9, 0.4)
        gluSphere(q, 0.4, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()  # ojo izquiero
        glTranslatef(-0.3, 0.9, 0.4)
        gluSphere(q, 0.4, SLICES, STACKS)
        glPopMatrix()

        ##bigotes
        set_white_material()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.3, 1.2, 1.9)
        glRotatef(90, 0, 1, 0)
        glRotatef(345, 1, 0, 0)
        gluCylinder(q, 0.03, 0.03, 2.5, SLICES, STACKS)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-1.3, 1.6, 1.7)
        glRotatef(90, 0, 1, 0)
        glRotatef(11, 1, 0, 0)
        gluCylinder(q, 0.03, 0.03, 2.5, SLICES, STACKS)
        glPopMatrix()

        ##Paleta
        glPushMatrix()
        glScalef(0.4, 0.4, 0.4)
        glTranslatef(-2.0, -0.2, 0.35)
        glRotatef(90, 0, 1, 0)
        glRotatef(90, 1, 0, 0)
        gluCylinder(q, 0.07, 0.07, 1.1, SLICES, STACKS)
        glPopMatrix()

        set_green_material()
        glPushMatrix()
        glTranslatef(-0.8, 0.0, 0.17)
        gluSphere(q, 0.2, SLICES, STACKS)
        glPopMatrix()


def dibujaPies(tipo):
    if tipo == " " or tipo == "C":
        set_black_material()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(-1.3, -5.0, 0)
        glRotatef(90, 1, 0, 0)
        draw_half_sphere(1.0, 32, 16)
        glPopMatrix()

        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        glTranslatef(1.3, -5.0, 0)
        glRotatef(90, 1, 0, 0)
        draw_half_sphere(1.0, 32, 16)
        glPopMatrix()


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


def draw_half_sphere(radius, slices, stacks):
    quadric = gluNewQuadric()
    gluQuadricOrientation(quadric, GLU_OUTSIDE)
    gluQuadricDrawStyle(quadric, GLU_FILL)

    for i in range(0, stacks // 2):
        lat0 = (math.pi / stacks) * i - (math.pi / 2)
        lat1 = (math.pi / stacks) * (i + 1) - (math.pi / 2)

        glBegin(GL_QUAD_STRIP)
        for j in range(0, slices + 1):
            lng = (2 * math.pi / slices) * j
            x0 = radius * math.cos(lng) * math.cos(lat0)
            y0 = radius * math.sin(lng) * math.cos(lat0)
            z0 = radius * math.sin(lat0)

            x1 = radius * math.cos(lng) * math.cos(lat1)
            y1 = radius * math.sin(lng) * math.cos(lat1)
            z1 = radius * math.sin(lat1)

            glNormal3f(x0, y0, z0)
            glVertex3f(x0, y0, z0)

            glNormal3f(x1, y1, z1)
            glVertex3f(x1, y1, z1)

        glEnd()

    gluDeleteQuadric(quadric)


def draw_cylinder_with_custom_caps(top_radius, bottom_radius, height, slices, stacks):
    quadric = gluNewQuadric()
    gluQuadricOrientation(quadric, GLU_OUTSIDE)
    gluQuadricDrawStyle(quadric, GLU_FILL)

    # Dibuja la tapa inferior
    glBegin(GL_TRIANGLE_FAN)
    glNormal3f(0, 0, -1)
    glVertex3f(0, 0, 0)
    for i in range(slices + 1):
        angle = (2 * math.pi * i) / slices
        x = bottom_radius * math.cos(angle)
        y = bottom_radius * math.sin(angle)
        glVertex3f(x, y, 0)
    glEnd()

    # Dibuja el cuerpo del cilindro
    gluCylinder(quadric, bottom_radius, top_radius, height, slices, stacks)

    # Dibuja la tapa superior
    glBegin(GL_TRIANGLE_FAN)
    glNormal3f(0, 0, 1)
    glVertex3f(0, 0, height)
    for i in range(slices + 1):
        angle = (2 * math.pi * i) / slices
        x = top_radius * math.cos(angle)
        y = top_radius * math.sin(angle)
        glVertex3f(x, y, height)
    glEnd()

    gluDeleteQuadric(quadric)


def draw_sphere_cover(radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Centro del círculo
    for i in range(num_segments + 1):
        theta = 2.0 * 3.1415926 * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    ################## MATERIAL_COLORES ############################


def set_grey_material():
    mat_ambient = [0.251, 0.251, 0.251, 0.0]
    mat_diffuse = [0.251, 0.251, 0.251, 0.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_light_grey_material():
    mat_ambient = [
        0.502,
        0.502,
        0.502,
        0.1529,
    ]  # Color ambiente (rojo en 0.8, verde en 0.4, azul en 0)
    mat_diffuse = [
        0.502,
        0.502,
        0.502,
        0.1529,
    ]  # Color difuso (rojo en 0.8, verde en 0.4, azul en 0)
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)


def set_black_material():
    mat_ambient = [0.0, 0.0, 0.0, 1.0]
    mat_diffuse = [0, 0, 0, 1]
    mat_specular = [0.9, 0.8, 0.9, 1.0]
    shine = 128

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_white_material():
    mat_ambient = [1.0, 1.0, 1.0, 1.0]
    mat_diffuse = [1.0, 1.0, 1.0, 1.0]
    mat_specular = [0.9, 0.9, 0.9, 1.0]
    shine = 128

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_brown_material():
    mat_ambient = [0.7294, 0.5804, 0.4078, 0.0]
    mat_diffuse = [0.7294, 0.5804, 0.4078, 0.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)


def set_orange_material():
    mat_ambient = [1.0, 0.5, 0.0, 1.0]
    mat_diffuse = [1.0, 0.5, 0.0, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shine)


def set_light_pink_material():
    mat_ambient = [1.0, 0.4, 0.4, 1.0]
    mat_diffuse = [1.0, 0.4, 0.4, 1.0]
    mat_specular = [0.94509, 0.81960, 0.94901, 1.0]
    shine = 125.2

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)


def set_red_material():
    mat_ambient = [0.3, 0.0, 0.0, 1.0]
    mat_diffuse = [0.7, 0.0, 0.0, 1.0]
    mat_specular = [0.9, 0.8, 0.9, 1.0]
    shine = 125

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)


def set_red1_material():
    mat_ambient = [0.8, 0.2, 0.2, 1.0]
    mat_diffuse = [0.7, 0.2, 0.2, 0.8]
    mat_specular = [0.9, 0.8, 0.9, 1.0]
    shine = 125

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)


def set_red_light_material():
    mat_ambient = [0.7, 0.2, 0.2, 1.0]
    mat_diffuse = [0.9, 0.3, 0.3, 1.0]
    mat_specular = [0.9, 0.8, 0.9, 1.0]
    shine = 125

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)


def set_purple_material():
    mat_ambient = [0.6, 0.2, 1.0, 1.0]
    mat_diffuse = [0.6, 0.2, 1.0, 1.0]
    mat_specular = [0.9, 0.8, 0.9, 1.0]
    shine = 125

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)


def set_light_blue_material():
    mat_ambient = [0.0, 0.4, 0.8, 1.0]
    mat_diffuse = [0.0, 0.7, 1.0, 1.0]
    mat_specular = [0.9, 0.8, 0.9, 1.0]
    shine = 128

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)


def set_green_material():
    mat_ambient = [0.5, 0.5, 0.0, 1.0]
    mat_diffuse = [0.7, 0.7, 0.0, 1.0]
    mat_specular = [0.9, 0.9, 0.9, 1.0]
    shine = 125

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)


def set_slightly_yellow_material():
    mat_ambient = [0.7, 0.5, 0.0, 1.0]
    mat_diffuse = [0.8, 0.8, 0.0, 1.0]
    mat_specular = [1.0, 1.0, 0.9, 1.0]
    shine = 125

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)
