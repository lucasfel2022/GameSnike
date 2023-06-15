import turtle
import time
import random

posponer = 0.1

score = 0
highscore = 0


#configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego de la Serpiente Spyke")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")   
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#segmentos o cuerpo de la serpiente

#texto en la pantalla
texto = turtle.Turtle()
texto.speed(0)
texto.color("white") 
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0                 highscore:0",align="center",font=("Courier",20,"normal"))

segmentos = []
#funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "rigth"


def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
        
    if cabeza.direction == "rigth":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
        
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")     
wn.onkeypress(izquierda,"Left")     
wn.onkeypress(derecha,"Right")     

while True:
    wn.update()
    #colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        #escondiendo los segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)
        
        #limpiar la lista de los segmentos de la serpiente
        segmentos.clear()
        #reseteando el marcador
        score = 0
        texto.clear()
        texto.write("Score: {}    highscore: {}".format(score,highscore),align="center",font=("Courier",20,"normal"))
    
        
    #colisiones con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        #aumentar el marcador
        score += 10
        
        if score > highscore:
           highscore = score
        #mover el cuerpo de la serpiente
    totalseg = len(segmentos)
    for index in range(totalseg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        texto.clear()
        texto.write("Score: {}    highscore: {}".format(score,highscore),align="center",font=("Courier",20,"normal"))
        segmentos[index].goto(x,y)
    
    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    
    
    
    movimiento()

    #closiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #escondiendo los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
                
            segmentos.clear()
            
        
    
    time.sleep(posponer)