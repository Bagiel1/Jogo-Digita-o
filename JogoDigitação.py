import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random

fig, axis= plt.subplots()
axis.set_xlim(0,10)
axis.set_ylim(0,10)

text, = axis.plot([],[], 'bo', markersize='5')

xs= []
ys= []
temp_coord= []
condi= True

def update(frame, *fargs):
    
    x= random.randint(0,8)
    y= random.randint(0,8)
    xs.append(x)
    ys.append(y)
    print(xs)
    print(ys)
    text.set_data(xs,ys)


    
    return text

def keyp(event):
    global temp_coord
    try:
        key= int(event.key)
        temp_coord.append(key)
        if len(temp_coord) == 2:
            key1,key2 = temp_coord
            if key1 in xs and key2 in ys:
                index1= xs.index(key1)
                index2= ys.index(key2)
                if index1 == index2:
                    print(f"Deletando {xs[index1]} e {ys[index2]}")
                    del xs[index1]
                    del ys[index2]
                text.set_data(xs,ys)
                plt.draw()

            temp_coord=[]

    except ValueError:
        pass
        
fig.canvas.mpl_connect('key_press_event', keyp)


animation= FuncAnimation(fig,update, interval= 5000)
plt.show()
