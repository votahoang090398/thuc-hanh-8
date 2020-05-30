k=open('d:/a.txt','r')	import turtle, random
char,wc,lc=0,0,0	colors=["red","green","blue","orange","purple","pink","yellow"]
for line in k:	painter=turtle.Turtle()
    for k in rangge(0,len(line)):	painter.pensize(3)
        char +=1	for i in range(10):
        if(line[k]==' '):	    color=random.choice(colors)
            wc+=1	    painter.pencolor(color)
        if(line[k]=='\n'):	    painter.circle(100)
            wc, lc=wc+1, lc=1	    painter.right(30)
print("The no.of chars is %d\n The no.of words in%d\n The no.of lines is %d%(char,wc,lc))
