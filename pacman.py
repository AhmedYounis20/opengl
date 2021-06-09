
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
import math


def init():

    glClearColor(1,1,1,1)
    glColor(0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-100,100,-100,100,-100,100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)


ball_x=95
def draw_ball():
    global ball_x

    if ball_x>15:
        ball_x-=1
    else:
        ball_x=95

    glColor(1,0,0)
    glTranslate(ball_x,0,-3)
    glutSolidSphere(4,100,100)
def draw_face(t):
    glColor(1,1,0)
    glBegin(GL_POLYGON)
    glVertex(0,0)
    for theta in range(0+t, 360-t, 1):
        x = 70 * math.cos(theta * math.pi / 180)
        y = 70 * math.sin(theta * math.pi / 180)
        glVertex(x,y)
    glEnd()
angel=30
t=angel
direction=1
def draw1():

    global t,direction
    if t==0:
        direction =0
    elif t==angel:
        direction=1
    if direction==1:
        if t>0:
            t-=1
    else:
        if t<angel:
            t+=1
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_face(t)
    draw_ball()

    glutSwapBuffers()




def timer(v):
    draw1()
    glutTimerFunc(15,timer,1)


def Main():
    glutInit()
    glutInitWindowSize(1000,1000)
    glutInitWindowPosition(10,10)
    glutCreateWindow("Pacman")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH)
    glutDisplayFunc(draw1)
    glutTimerFunc(15,timer,1)
    init()
    glutMainLoop()


Main()


