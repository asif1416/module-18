import turtle           
colors = [ "red","purple","blue","green","orange","yellow"]  #creating list of colors
my_pen = turtle.Pen()
turtle.bgcolor("black") #background color of canvas
for x in range(360): #iterate loop for 360 times
   my_pen.pencolor(colors[x % 6]) #changing pen color
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)