import matplotlib.pyplot as plt
import numpy as np
import math

def basicPlotXY(x, y, title, xt, yt):
# Plot input and output data
    fig, ax = plt.subplots()
    plt.title(title)
    plt.xlabel(xt)
    plt.ylabel(yt)
    ax.plot(x, y, linewidth=2.0)
    
def pointLabelXY(x, y, label="", xOffset=1, yOffset=1):
    plt.plot(x, y, 'ro', ms=5.0)
    x=x+xOffset
    y=y+yOffset
    plt.text(x, y,label)
    
def computeFx(x):
    y=x**2-x+3
    g=2*x-1
    return [y, g]


x = np.linspace(-4.1, 5.1, 1000)
[y,g] = computeFx(x)
basicPlotXY(x,computeFx(x)[0], "f(x) plot", "x", "f(x)")


x_0 = 5
lr = 0.2

xSteps = []
ySteps = []

xStep = x_0
step=50
finalStep=0

dyStop=0.01

for i in range(step):
    xSteps.append(xStep)
    [y,g] = computeFx(xStep)
    ySteps.append(y)
    xStep = xStep - lr * g 
    print('x'+str(i)+'=', round(xSteps[-1],3) , ', gradient'+str(i)+'=', round(g,3), 'y'+str(i)+'=', round(y,5))

    if i>1 and abs(g) < dyStop: 
        finalStep = i
        break

print('\nMinimum: x'+str(finalStep)+'=', round(xSteps[finalStep],3), ', y'+str(finalStep)+'=', round(ySteps[finalStep],5))

for i in range(finalStep):  
    xyLocStr = str(i)+': ('+str(xSteps[i])+", "+str(ySteps[i])+')'
    pointLabelXY(xSteps[i], ySteps[i], '',.2,-1.5)
    
pointLabelXY(xSteps[finalStep], ySteps[finalStep],'('+str(round(xSteps[finalStep],3))+', '+str(round(ySteps[finalStep],3))+' )',0,-1.5)

plt.show()
