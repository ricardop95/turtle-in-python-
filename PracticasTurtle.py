
import turtle
import random
turtle.title('Desing')   
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.showturtle()
x=1
turtle.speed(0)
while x<500:
    '''
    r= random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.pencolor(r,g,b)   
    turtle.colormode(255)
    '''#tuve que comentar este segmento de codigo por que no se me fija la ventana 
       #añadiendo el codigo desde la linea 11 hasta la linea 15 
    turtle.forward(5+x)
    turtle.right(91)
    x+=1
    



turtle.mainloop()