from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time import sleep
import numpy as np
import math
from random import randint
import pygame
texture=None
image_width=None
Image_height=None
def Init(w,h):
    global texture , image_height,image_width
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w/h ,0.1, 1000 )
    #glOrtho(-2000,2000,-2000,2000,-2000,2000)
    #gluLookAt(5,0,10, 0, 0, -20 ,0,1,0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glEnable(GL_DEPTH_TEST)
    texture=glGenTextures(2)
    img_data=pygame.image.load('imgs/coin_face.png')
    img=pygame.image.tostring(img_data,'RGBA',1)
    image_width=img_data.get_width()
    image_height=img_data.get_height()
    glBindTexture(GL_TEXTURE_2D,texture[0])
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR)
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP)
    gluBuild2DMipmaps(GL_TEXTURE_2D,4,image_width,image_height,GL_RGBA,GL_UNSIGNED_BYTE,img)

    img_data=pygame.image.load('imgs/wood.jpg')
    img=pygame.image.tostring(img_data,'RGBA',1)
    image_width=img_data.get_width()
    image_height=img_data.get_height()
    glBindTexture(GL_TEXTURE_2D,texture[1])
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR)
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP)
    gluBuild2DMipmaps(GL_TEXTURE_2D,4,image_width,image_height,GL_RGBA,GL_UNSIGNED_BYTE,img)
    glEnable(GL_TEXTURE_2D)
rotate_angle=10
def draw():
    global rotate_angle

    glClearColor(1,1,1,1)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glBindTexture(GL_TEXTURE_2D,texture[1])
    glBegin(GL_POLYGON)
    glTexCoord(0,1)
    glVertex(-40, 40, -40)
    glTexCoord(1,1)
    glVertex(40, 40, -40)
    glTexCoord(1,0)

    glVertex(40, -40, -40)
    glTexCoord(0,0)

    glVertex(-40, -40, -40)
    glEnd()
    glLoadIdentity()
    glBindTexture(GL_TEXTURE_2D,texture[0])
    r=10
    glTranslate(0,0,-25)
    glRotate(rotate_angle,0,1,0)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 360, .01):
        x=r*math.cos(theta*math.pi/180)
        y=r*math.sin(theta*math.pi/180)
        glTexCoord(x/22+0.503,y/22+0.5)
        glVertex(x,y)

    glEnd()
    rotate_angle +=10
    rotate_angle %=360
    glutSwapBuffers()
def timer(v):
    draw()
    glutTimerFunc(4,timer,1)
if __name__=="__main__":
    glutInit()
    glutInitWindowSize(800,800)
    glutInitWindowPosition(10,10)
    glutCreateWindow("coin")
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE)
    glutDisplayFunc(draw)
    glutTimerFunc(4,timer,1)
    Init(5,5)
    glutMainLoop()