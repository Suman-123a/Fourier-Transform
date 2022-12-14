#Fourier transformation of
#f(x)=1-|x| range: -1 to 1
import math as mt
import numpy as np
import matplotlib.pyplot as plt

xi=-1
xf=1
n=50

def f(x):
	return 1-abs(x)
def trap(xi,xf,n,t):
	h=(xf-xi)/(n-1)
	yy=[]
	xx=[]
	for i in range(n):
		x=xi+i*h
		y=f(x)*mt.sin(t*x)
		yy.append(y)
		z=f(x)*mt.cos(t*x)
		xx.append(z)
	s=0
	p=0
	for i in range(1,n-1):
		s=s+yy[i]
		p=p+xx[i]
	s=yy[0]+2*s+yy[n-1]
	s=0.5*h*s
	p=xx[0]+2*p+xx[n-1]
	p=0.5*h*p
    
	
	return s,p
uu=[]
vv=[]
z1=np.linspace(-50,50,500)
for i in range(500):
	t=z1[i]
	y=trap(xi,xf,n,t)
	vv.append(t)
	w=((y[0]**2+y[1]**2)**(1/2))*1/(2*np.pi)**0.5
	uu.append(w)
g=np.linspace(-1,1,100)
g1=1-abs(g)

plt.axhline()
plt.axvline()
plt.plot(g,g1)
plt.plot(vv,uu)
plt.show()