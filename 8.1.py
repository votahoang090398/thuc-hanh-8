input_file=open('D:/a.txt','r')	import turtle
for line in input_file:	window=turtle.Screen()
    l=len(line)	window.bgcolor("lightgreen")
    s=' '	
    while(l>=1):	painter=turtle.Turtle()
        s=s+line[l-1]	painter.fillcolor('blue')
        l=l-1	painter.pencolor('blue')
    print(s)	painter.pensize(3)
input_file.close()
