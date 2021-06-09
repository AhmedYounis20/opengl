import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
############################ setting up for screen window ##################################


window_width=1000
window_height=800

######################################   Ball   ###########################################

class Ball :
    def __init__(self,x=window_width//2,y=window_height//2,z=40):
        self.x=x
        self.y=y
        self.z=z
############################# used global variable ########################################
mouse={'x':0,'y':0}
ball=Ball()
r=20
moving=1
t=1
y_direction=1
x_direction=1
bat_x=500
player_score=computer_score=0
ball_height_band=window_height-r
ball_width_band=window_width-r
bat_width_band=window_width-window_width/10
###################################### Initialize  #########################################
def init():
    glClearColor(0.6,0.4,0.2,1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(120, 1 , 1 ,100 )

    glOrtho(0,window_width,0,window_height,0,1000)
    #glOrtho(-1,1,-1,1,-1,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

##################################### Ball Behaviour ##########################################
def moving_ball():
    global x_direction , y_direction ,  ball,player_score,computer_score
    if ball.y<=55 and ball.x-bat_x<=5.5*(window_width/50) and ball.x-bat_x>=-5.5*(window_width/50):
        y_direction*=-1
        ball.x+=x_direction*1
        ball.y+=y_direction*1
        player_score+=1
        print("player:",player_score,"computer:",computer_score)
    if ball.y<=20:
        computer_score+=1
        print("player:",player_score,"computer:",computer_score)


    if ball.x<ball_width_band and ball.x> r:
        ball.x+=x_direction*1
    else:
        x_direction*=-1
        ball.x+=x_direction*1
    if ball.y<ball_height_band and ball.y> r:
        ball.y+=y_direction*1
    else:
        y_direction*=-1
        ball.y+=y_direction*1



##################################### Drawing Function ###################################

def draw():
    global t,x_direction,y_direction,moving,mouse,bat_x

    if moving:
        t+=1
        glClear(GL_COLOR_BUFFER_BIT)
        # if  mouse['x'] >=-9 and  mouse['x'] <=9:


        glLoadIdentity()
        glTranslate(ball.x,ball.y,-40)
        moving_ball()
        glColor(1,1,1)
        glutSolidSphere(r,200,200)

        glLoadIdentity()

        glColor(0,0,1)
        glTranslate(bat_x,10,-40)
        glScale(window_width/50,5,1)
        glutSolidCube(11)

        glutSwapBuffers()



############################# track mouse moves ########################
def Mousetrack(x, y):
    global bat_x
    if int(x)< bat_width_band and int(x)>window_width/10:

        bat_x=int(x)
    elif int(x)>=bat_width_band:
        bat_x=bat_width_band
    else:
        bat_x=window_width/10
time_interval=1

def timer(v):
    draw()
    glutTimerFunc(time_interval, timer,1)
def Main():
    glutInit()
    glutInitWindowSize(window_width,window_height)
    glutInitWindowPosition(10,10)
    glutCreateWindow("ball moving")
    glutInitDisplayMode(GLUT_DOUBLE)
    glClear(GL_COLOR_BUFFER_BIT)
    glutDisplayFunc(draw)
    glutTimerFunc(time_interval, timer,1)
    glutPassiveMotionFunc(Mousetrack)
    init()
    glutMainLoop()


Main()