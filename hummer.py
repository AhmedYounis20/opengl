from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time import sleep
def Init(w,h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w/h ,0.1, 100 )
    #glOrtho(-20,20,-20,20,-20,20)
    gluLookAt(5,0,10, 0, 0, -20 ,0,1,0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glEnable(GL_DEPTH_TEST)
x_angle=z_angle=0
y_angle=180
t=1
def draw():
    sleep(0.1)
    global t
    t+=1
    glColor(0,0.2,0.4,1)
    glLoadIdentity()
    glTranslate(0,0,-20)
    glRotate(x_angle, 1, 0 , 0)
    glRotate(y_angle, 0, 1 , 0)
    glRotate(z_angle, 0, 0 , 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_POLYGON)
    ### right side
    glColor(0.1,.4,0.5)
    glVertex(-10,5,0)
    glVertex(-10,10,0)
    glVertex(0,10,0)
    glVertex(5,7.5,0)
    glVertex(0,5,0)
    glEnd()

    ### back side
    glBegin(GL_POLYGON)
    glColor(0.7 , 0.2 , 0.5)
    glVertex(-10,5,0)
    glVertex(-10,10,0)
    glVertex(-10,10,-4)
    glVertex(-10,5,-4)
    glEnd()

    ## left side
    glBegin(GL_POLYGON)
    glColor(0.1,.4,0.5)
    glVertex(-10,5,-4)
    glVertex(-10,10,-4)
    glVertex(0,10,-4)
    glVertex(5,7.5,-4)
    glVertex(0,5,-4)
    glEnd()

    ## face side up
    glBegin(GL_POLYGON)
    glColor(1,.4,0.5)
    glVertex(0,10,0)
    glVertex(5,7.5,0)
    glVertex(5,7.5,-4)
    glVertex(0,10,-4)
    glEnd()

    ## face side down
    glBegin(GL_POLYGON)
    glColor(0,1,0.5)
    glVertex(0,5,0)
    glVertex(5,7.5,0)
    glVertex(5,7.5,-4)
    glVertex(0,5,-4)
    glEnd()

    ## upper
    glBegin(GL_POLYGON)
    glVertex(-10,10,0)
    glVertex(0,10,0)
    glVertex(0,10,-4)
    glVertex(-10,10,-4)
    glEnd()

    ## down

    glBegin(GL_POLYGON)
    glVertex(-10,5,0)
    glVertex(0,5,0)
    glVertex(0,5,-4)
    glVertex(-10,5,-4)

    glEnd()
    ################### hand
    glColor(0,0,1)
    glTranslate(-5,0,-2)
    glScale(5,10,3)
    glutSolidCube(1)


    glFlush()


def keyboard(key,x,y):
    global x_angle,y_angle,z_angle
    if key==b"d":
        y_angle+=10
        draw()

    elif key==b"a":
        y_angle-=10
        draw()
    elif key==b'w':
        x_angle+=10
        draw()

    elif key==b"s":
        x_angle-=10
        draw()
    elif key==b'c':
        z_angle+=10
        draw()

    elif key==b"v":
        z_angle-=10
        draw()




if __name__=="__main__":
    glutInit()
    glutInitWindowSize(800,800)
    glutInitWindowPosition(10,10)
    glutCreateWindow("hummer")
    glutInitDisplayMode(GLUT_DEPTH)
    glutDisplayFunc(draw)

    #glutIdleFunc(draw)
    glutKeyboardFunc(keyboard)
    Init(5,5)
    glutMainLoop()