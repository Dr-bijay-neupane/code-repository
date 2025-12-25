def DDA(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>abs(dy):
        steps=abs(dx)
    else:
        steps=abs(dy)
    xinc=dx/steps
    yinc=dy/steps
    x=x1
    y=y1
    print(round(x), round(y))
    for i in range (1,steps+1):
        x=x+xinc
        y=y+yinc
        print(round(x), round(y))
x1=int(input("ENTER X1"))
y1=int(input("ENTER y1"))
x2=int(input("ENTER X2"))
y2=int(input("ENTER Y2"))
DDA(x1,y1,x2,y2)
    

        


