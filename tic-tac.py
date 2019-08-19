import turtle
import time
t1=turtle.Turtle('square')
wn=turtle.Screen()
wn.setup(500,500)

t1.shapesize(2.9)
t1.color('green')
t1.penup()
t1.hideturtle()
t1.goto(0,0)
t1.showturtle()
t1.goto(-100,100)

t1.speed(10)
def grid():
    for m in range(3):
        
        for n in range (3):
                t1.goto(-100+60*n,100-60*m)
                t1.stamp()
grid()
reference=[(-100,100),(-40,100),(20,100),(-100,40),(-40,40),(20,40)\
           ,(-100,-20),(-40,-20),(20,-20)]
delta=[100,100,100,100,100,100,100,100,100]

q=-1
t=turtle.Turtle('square')
t.shapesize(1.5)
t.hideturtle()
t.speed(10)

crs=[0,0,0,0,0,0,0,0,0]
circ=[0,0,0,0,0,0,0,0,0]
z=[0,0,0,0,0,0,0,0,0]


def loopp():
    for u in range(9):
        crs[u]=0
        circ[u]=0
        z[u]=0
    

def h(x, y):
    sum=0
    global q
    #global zz
    
    t.penup()
    t.goto(x, y)
    q=q+1
    #print('q=',q)
    
    for s in range(9):
            if q%2==0:
                t.shape('square')
                t.shapesize(1.5)    
                t.color('red')
            else:
                t.shape('circle')
                t.shapesize(1.5)
                t.color('blue')
            
            delta[s]= t.distance(reference[s])
            print(z[s])
            X0,Y0=t.position()
            if X0<-130 or X0>50 or Y0>130 or Y0<-50:
                exit()
            
            if delta[s]>40:
                t.hideturtle()
            if delta[s]<40 and z[s]==0:
                t.hideturtle()
                
                t.setposition(reference[s])
                t.showturtle()
                z[s]=1
                print('s=',s)
                #print('z[s]=',z[s])
                q1=q
                t.stamp()
                X,Y=t.position()
                
                for w in range(3):
                    if Y==(100-w*60):
                        if q%2==0:
                            crs[w]=crs[w]+X
                            if crs[w]==-120:
                                print('cross win')
                                time.sleep(2)
                                q=-1
                                grid()
                                loopp()
                        else:
                            circ[w]=circ[w]+X
                            if circ[w]==-120:
                                print('circle win')
                                    
                                time.sleep(2)
                                q=-1
                                grid()
                                loopp()
                                
                for w1 in range(3):
                    if X==-(100-w1*60):
                        if q%2==0:
                            crs[3+w1]=crs[3+w1]+Y
                            if crs[3+w1]==120:
                                print('cross win')
                                time.sleep(2)
                                q=-1
                                grid()
                                loopp()
                        else:
                            circ[3+w1]=circ[3+w1]+Y
                            if circ[3+w1]==120:
                                print('circle win')
                                time.sleep(2)
                                q=-1
                                grid()
                                loopp()
                        
                if (X==-100 and Y==100) or (X==-40 and Y==40) or (X==20 and Y==-20):
                    if q%2==0:
                        crs[6]=crs[6]+Y
                        if crs[6]==120:
                            print('cross win')
                            time.sleep(2)
                            q=-1
                            grid()
                            loopp()
                    else:
                        circ[6]=circ[6]+Y
                        if circ[6]==120:
                            print('circle win')
                            time.sleep(2)
                            q=-1
                            grid()
                            loopp()
                                                          
                if (X==-100 and Y==-20) or (X==-40 and Y==40) or (X==20 and Y==100):
                    if q%2==0:
                        crs[7]=crs[7]+Y
                        if crs[7]==120:
                            print('cross win')
                            time.sleep(2)
                            q=-1
                            grid()
                            loopp()
                    else:
                        circ[7]=circ[7]+Y
                        if circ[7]==120:
                            print('circle win')
                            time.sleep(2)
                            q=-1
                            grid()
                            loopp()

    for s in range (9):
        sum=sum+z[s]
    print('sum=',sum)
    if sum==9:
    
        print('q=',q)
        print('Draw')
        time.sleep(2)
        q=-1
        grid()
        loopp()
wn.onclick(h)
