#Raghu Alluri
#April 7th, 2018
#This program will draw a rainbow and some other attributes ex.(flower)
import turtle
#Allows to convert between hsv cylinder and rgb colors
import colorsys
import random

#Defining the screen for the program to be drawn on and to be exited on by a click
wn = turtle.Screen()
wn.bgcolor('lightblue')
#Title of the new window
turtle.title('Rainbow Drawing')

#Allow python to add the imported shape to it's temporary library
global flower
turtle.register_shape("flowerpetal.gif")

#Tracer has been set to zero t allow python to draw objects faster
turtle.tracer(0, 0)
#mainLoop will draw the rainbow using hsv cylinder and rgb colors
def mainLoop(pen_space, new_x, heading):

    #Define the pen to draw the objects desired
    pen = turtle.Turtle()
    pen.pensize(0.5)
    pen.penup()

    #Variable to tell the for loop to continue that many times
    ranger = 800

    for i in range(ranger):
        #Every time it loops, the hsv cylinder shifts creating a new color of the rainbow
        new_color = colorsys.hsv_to_rgb(i / 800.0, 1.0, 1.0)

        #Tells the program where to start the rainboe and the arc of the rainbow
        pen.goto(new_x, -300)
        pen.pendown()
        pen.color(new_color)
        pen.setheading(heading)
        pen.circle(new_x, 180)
        pen.penup()

        #Reduces the x-coordinate to curve in after each arc of the rainbow
        new_x += pen_space
        #Updates the display everytime an arc is drawn to show the rainbow
        turtle.update()

#This function draws a ground for the rainbow to be on
def ground(x_coordinate, y_coordinate, heading):

    #Defining another pen to draw the ground
    global pen2

    pen2 = turtle.Turtle()
    pen2.pensize(3)
    pen2.penup()
    pen2.setheading(heading - 90)
    pen2.goto(x_coordinate, y_coordinate)
    pen2.color("green", "green")

    #Rectangular shape for the ground
    pen2.pendown()
    pen2.begin_fill()
    pen2.forward(1200)
    pen2.right(heading)
    pen2.forward(100)
    pen2.right(heading)
    pen2.forward(1200)
    pen2.right(heading)
    pen2.forward(100)
    pen2.end_fill()

    #Updating display to show the new created ground
    turtle.update()

#Function that will draw a flower beneath the ranboe on top of the ground
def flower(stem_height, heading):
    #Telling the pen to draw the stem of the flower
    pen2.penup()
    pen2.goto(0, -300)
    pen2.pensize(10)
    pen2.color("green")
    pen2.setheading(heading)
    pen2.pendown()
    pen2.forward(stem_height)

    #Telling the pen to change it's shape to an imported image and set its position on top of the stem
    pen2.penup()
    pen2.shape("flowerpetal.gif")
    pen2.goto(0, -300 + stem_height)

    #Updates the display after the flower has been drawn
    turtle.update()

#This function will create rain droplets
def droplets(d_height, d_width):
    global drop1, drop2, drop3, drop4, drop5, drop6, drop7, drop8, drop9
    global drop10, drop11, drop12, drop13, drop14, drop15, drop16, drop17, drop18
    global drop19, drop20

    #These blocks of code here define and create the rain drops themselves above the screen

    drop1 = turtle.Turtle()
    drop1.shape("square")
    drop1.shapesize(d_height, d_width)
    drop1.color('blue')
    drop1.penup()

    drop2 = turtle.Turtle()
    drop2.shape("square")
    drop2.shapesize(d_height, d_width)
    drop2.color('blue')
    drop2.penup()

    drop3 = turtle.Turtle()
    drop3.shape("square")
    drop3.shapesize(d_height, d_width)
    drop3.color('blue')
    drop3.penup()

    drop4 = turtle.Turtle()
    drop4.shape("square")
    drop4.shapesize(d_height, d_width)
    drop4.color('blue')
    drop4.penup()

    drop5 = turtle.Turtle()
    drop5.shape("square")
    drop5.shapesize(d_height, d_width)
    drop5.color('blue')
    drop5.penup()

    drop6 = turtle.Turtle()
    drop6.shape("square")
    drop6.shapesize(d_height, d_width)
    drop6.color('blue')
    drop6.penup()

    drop7 = turtle.Turtle()
    drop7.shape("square")
    drop7.shapesize(d_height, d_width)
    drop7.color('blue')
    drop7.penup()

    drop8 = turtle.Turtle()
    drop8.shape("square")
    drop8.shapesize(d_height, d_width)
    drop8.color('blue')
    drop8.penup()

    drop9 = turtle.Turtle()
    drop9.shape("square")
    drop9.shapesize(d_height, d_width)
    drop9.color('blue')
    drop9.penup()

    drop10 = turtle.Turtle()
    drop10.shape("square")
    drop10.shapesize(d_height, d_width)
    drop10.color('blue')
    drop10.penup()

    drop11 = turtle.Turtle()
    drop11.shape("square")
    drop11.shapesize(d_height, d_width)
    drop11.color('blue')
    drop11.penup()

    drop12 = turtle.Turtle()
    drop12.shape("square")
    drop12.shapesize(d_height, d_width)
    drop12.color('blue')
    drop12.penup()

    drop13 = turtle.Turtle()
    drop13.shape("square")
    drop13.shapesize(d_height, d_width)
    drop13.color('blue')
    drop13.penup()

    drop14 = turtle.Turtle()
    drop14.shape("square")
    drop14.shapesize(d_height, d_width)
    drop14.color('blue')
    drop14.penup()

    drop15 = turtle.Turtle()
    drop15.shape("square")
    drop15.shapesize(d_height, d_width)
    drop15.color('blue')
    drop15.penup()

    drop16 = turtle.Turtle()
    drop16.shape("square")
    drop16.shapesize(d_height, d_width)
    drop16.color('blue')
    drop16.penup()

    drop17 = turtle.Turtle()
    drop17.shape("square")
    drop17.shapesize(d_height, d_width)
    drop17.color('blue')
    drop17.penup()

    drop18 = turtle.Turtle()
    drop18.shape("square")
    drop18.shapesize(d_height, d_width)
    drop18.color('blue')
    drop18.penup()

    drop19 = turtle.Turtle()
    drop19.shape("square")
    drop19.shapesize(d_height, d_width)
    drop19.color('blue')
    drop19.penup()

    drop20 = turtle.Turtle()
    drop20.shape("square")
    drop20.shapesize(d_height, d_width)
    drop20.color('blue')
    drop20.penup()

    #Display is updated after each one of them is drawn above the screen
    turtle.update()

#This function will cause the rain to fall and keep falling
def rainmovement():

    finish = False

    #Setting starting position for drop1 and starting while loop to get the drops to fall
    drop1.goto(0, random.randint(170, 450))
    while not finish:
        #The speed in which the drops will fall is the drop_speed
        drop_speed = random.randint(50, 100)

        #Each block defines each dropelts movement down the screen
        y = drop1.ycor()
        y -= drop_speed
        drop1.sety(y)

        y = drop2.ycor()
        y -= drop_speed
        drop2.sety(y)

        y = drop3.ycor()
        y -= drop_speed
        drop3.sety(y)

        y = drop4.ycor()
        y -= drop_speed
        drop4.sety(y)

        y = drop5.ycor()
        y -= drop_speed
        drop5.sety(y)

        y = drop6.ycor()
        y -= drop_speed
        drop6.sety(y)

        y = drop7.ycor()
        y -= drop_speed
        drop7.sety(y)

        y = drop8.ycor()
        y -= drop_speed
        drop8.sety(y)

        y = drop9.ycor()
        y -= drop_speed
        drop9.sety(y)

        y = drop10.ycor()
        y -= drop_speed
        drop10.sety(y)

        y = drop11.ycor()
        y -= drop_speed
        drop11.sety(y)

        y = drop12.ycor()
        y -= drop_speed
        drop12.sety(y)

        y = drop13.ycor()
        y -= drop_speed
        drop13.sety(y)

        y = drop14.ycor()
        y -= drop_speed
        drop14.sety(y)

        y = drop15.ycor()
        y -= drop_speed
        drop15.sety(y)

        y = drop16.ycor()
        y -= drop_speed
        drop16.sety(y)

        y = drop17.ycor()
        y -= drop_speed
        drop17.sety(y)

        y = drop18.ycor()
        y -= drop_speed
        drop18.sety(y)

        y = drop19.ycor()
        y -= drop_speed
        drop19.sety(y)

        y = drop20.ycor()
        y -= drop_speed
        drop20.sety(y)

        #These blocks of code tell each droplet to go back to the top of the scren after they have hit the ground
        if drop1.ycor() < -300:
            drop1.hideturtle()
            drop1.goto(random.randint(-600, 600), random.randint(170, 450))
            drop1.showturtle()

        if drop2.ycor() < -300:
            drop2.hideturtle()
            drop2.goto(random.randint(-600, 600), random.randint(170, 450))
            drop2.showturtle()

        if drop3.ycor() < -300:
            drop3.hideturtle()
            drop3.goto(random.randint(-600, 600), random.randint(170, 450))
            drop3.showturtle()

        if drop4.ycor() < -300:
            drop4.hideturtle()
            drop4.goto(random.randint(-600, 600), random.randint(170, 450))
            drop4.showturtle()

        if drop5.ycor() < -300:
            drop5.hideturtle()
            drop5.goto(random.randint(-600, 600), random.randint(170, 450))
            drop5.showturtle()

        if drop6.ycor() < -300:
            drop6.hideturtle()
            drop6.goto(random.randint(-600, 600), random.randint(170, 450))
            drop6.showturtle()

        if drop7.ycor() < -300:
            drop7.hideturtle()
            drop7.goto(random.randint(-600, 600), random.randint(170, 450))
            drop7.showturtle()

        if drop8.ycor() < -300:
            drop8.hideturtle()
            drop8.goto(random.randint(-600, 600), random.randint(170, 450))
            drop8.showturtle()

        if drop9.ycor() < -300:
            drop9.hideturtle()
            drop9.goto(random.randint(-600, 600), random.randint(170, 450))
            drop9.showturtle()

        if drop10.ycor() < -300:
            drop10.hideturtle()
            drop10.goto(random.randint(-600, 600), random.randint(170, 450))
            drop10.showturtle()

        if drop11.ycor() < -300:
            drop11.hideturtle()
            drop11.goto(random.randint(-600, 600), random.randint(170, 450))
            drop11.showturtle()

        if drop12.ycor() < -300:
            drop12.hideturtle()
            drop12.goto(random.randint(-600, 600), random.randint(170, 450))
            drop12.showturtle()

        if drop13.ycor() < -300:
            drop13.hideturtle()
            drop13.goto(random.randint(-600, 600), random.randint(170, 450))
            drop13.showturtle()

        if drop14.ycor() < -300:
            drop14.hideturtle()
            drop14.goto(random.randint(-600, 600), random.randint(170, 450))
            drop14.showturtle()

        if drop15.ycor() < -300:
            drop15.hideturtle()
            drop15.goto(random.randint(-600, 600), random.randint(170, 450))
            drop15.showturtle()

        if drop16.ycor() < -300:
            drop16.hideturtle()
            drop16.goto(random.randint(-600, 600), random.randint(170, 450))
            drop16.showturtle()

        if drop17.ycor() < -300:
            drop17.hideturtle()
            drop17.goto(random.randint(-600, 600), random.randint(170, 450))
            drop17.showturtle()

        if drop18.ycor() < -300:
            drop18.hideturtle()
            drop18.goto(random.randint(-600, 600), random.randint(170, 450))
            drop18.showturtle()

        if drop19.ycor() < -300:
            drop19.hideturtle()
            drop19.goto(random.randint(-600, 600), random.randint(170, 450))
            drop19.showturtle()

        if drop20.ycor() < -300:
            drop20.hideturtle()
            drop20.goto(random.randint(-600, 600), random.randint(170, 450))
            drop20.showturtle()

        #This will then update the display after all of the above code has been done
        turtle.update()


#These variables are defined to be put as parameters into the funtions
x_cor = -600
y_cor = -300
penspace = 0.25
penheading = 90
stemheight = 100
droplet_width = 0.1
droplet_height = 1.5

#All the loops are called at the end to be active
mainLoop(penspace, x_cor, penheading)
ground(x_cor, y_cor, penheading)
flower(stemheight, penheading)
droplets(droplet_height, droplet_width)
rainmovement()
#This will close the screen once the user clicks of the screen
wn.exitonclick()
