import matplotlib.pyplot as plt
from numpy import *
import math
from numpy.linalg import norm

def computeFxy(x,y):
	z=x**2+2*(y**2)-x+3
	return z

def computeGxy(x,y):
	gx=x*2-1
	gy=y*4
	return array([gx,gy])

def grad_descent2(f, gradf, init_t, alpha):
    EPS = 0.01
    t = init_t.copy()
    
    max_iter = 10000
    iter = 1
    while norm(gradf(t[0], t[1])) > EPS and iter < max_iter:
        t -= alpha*gradf(t[0], t[1])
        print(iter, 'x,y:',round(t[0],5),round(t[1],5), 'z:',round(f(t[0], t[1]),5), 'Gred:',round(gradf(t[0], t[1])[0],5), round(gradf(t[0], t[1])[1],4), 'Norm:', round(norm(gradf(t[0], t[1])),5))
        iter += 1
    
    return t

grad_descent2(computeFxy, computeGxy, array([5.0, 4.0]), 0.1)
