import turtle

#ABLAK

ablak = turtle.Screen()
ablak.setup(width=800, height=600)
ablak.bgcolor("black")
ablak.title("PONG")
ablak.tracer(0)

#Bal oldali utö
bal_uto = turtle.Turtle()
bal_uto.speed(0)
bal_uto.shape("square")
bal_uto.color("blue")
bal_uto.shapesize(stretch_wid=5, stretch_len=1)
bal_uto.penup()
bal_uto.goto(-350,0)

#Jobb oldali utö
jobb_uto = turtle.Turtle()
jobb_uto.speed(0)
jobb_uto.shape("square")
jobb_uto.color("red")
jobb_uto.shapesize(stretch_wid=5, stretch_len=1)
jobb_uto.penup()
jobb_uto.goto(350,0)

#labda
labda = turtle.Turtle()
labda.speed(0)
labda.shape("circle")
labda.color("yellow")
labda.penup()
labda.goto(0,0)
labda.dx = 1
labda.dy = -1

#Pontszam
jobb_pontszam = 0
bal_pontszam = 0

pontszam = turtle.Turtle()
pontszam.speed(1)
pontszam.color("white")
pontszam.hideturtle
pontszam.penup()
pontszam.goto(0,260)
pontszam.write(f"Bal jatekos: {bal_pontszam} Jobb jatekos: {jobb_pontszam}", align="center", font=("Courier", 24, "normal"))


def bal_uto_fel():
    y = bal_uto.ycor()
    y += 30
    bal_uto.sety(y)

def bal_uto_le():
    y = bal_uto.ycor()
    y -= 30
    bal_uto.sety(y)

def jobb_uto_fel():
    y = jobb_uto.ycor()
    y += 30
    jobb_uto.sety(y)

def jobb_uto_le():
    y = jobb_uto.ycor()
    y -= 30
    jobb_uto.sety(y)

ablak.onkey(bal_uto_fel, "w")
ablak.onkey(bal_uto_le, "s")

ablak.onkey(jobb_uto_fel, "p")
ablak.onkey(jobb_uto_le, "l")

ablak.listen()

while True:

    #frissul a program kirajzolasa
    ablak.update()

    labda.setx(labda.xcor() + labda.dx)
    labda.sety(labda.ycor() + labda.dy)

    #tetejeröl pattanjon vissza
    if labda.ycor() > 288:
        labda.sety(288)
        labda.dy *= -1

     #aljarol pattanjon vissza
    if labda.ycor() < -288:
        labda.sety(-288)
        labda.dy *= -1

    #jobb oldal erintese
    if labda.xcor() > 388:
        labda.goto(0,0)
        labda.dx *= -1
        bal_pontszam += 1
        pontszam.clear()
        pontszam.write(f"Bal jatekos: {bal_pontszam} Jobb jatekos: {jobb_pontszam}", 
            align="center", font=("Courier", 24, "normal"))


     #bal oldal erintese
    if labda.xcor() < -388:
        labda.goto(0,0)
        labda.dx *= -1
        jobb_pontszam += 1
        pontszam.clear()
        pontszam.write(f"Bal jatekos: {bal_pontszam} Jobb jatekos: {jobb_pontszam}", 
            align="center", font=("Courier", 24, "normal"))
    
    #jobb oldali utöröl visszapattan
    if jobb_uto.xcor()-20 < labda.xcor() < jobb_uto.xcor() and jobb_uto.ycor()-40 < labda.ycor() < jobb_uto.ycor() + 40:
        labda.setx(jobb_uto.xcor()-20)
        labda.dx *= -1

    #bal oldali utöröl visszapattan
    if bal_uto.xcor()+20 > labda.xcor() > bal_uto.xcor() and bal_uto.ycor()-40 < labda.ycor() < bal_uto.ycor() + 40:
        labda.setx(bal_uto.xcor()+20)
        labda.dx *= -1


