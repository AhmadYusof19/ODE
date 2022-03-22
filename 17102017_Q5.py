# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

n=10
h=1
p=0
x0=0
u0=240
u1=150
x0b=0
fx=0


a=np.zeros([n-1,n-1])
for i in range(n-1):
    for j in range(n-1):
        x0=x0+h
        q=0.15
        if j==i-1:
            a[i][j]=-(1+0.5*p*h)
        if j==i:
            a[i][j]=(2+q*h**2)
        if j==i+1:
            a[i][j]=-(1-0.5*p*h)
            
print(a)

b=np.zeros([n-1])
for i in range(n-1):
    x0b=x0b+h
    u0=240
    u1=150
    if i==0:
        b[i]=(-h**2*fx)+u0*(1+0.5*h*p)
    else:
        b[i]=-h**2*fx
    if i==n-2:
        b[i]=(-h**2*fx)+u1*(1-0.5*h*p)    
    
    
        
print(b) 

y=np.linalg.solve(a,b)
print(y)


x=np.linspace(1,10,9)
plt.plot(x, y,"o-")
plt.title("Solution for question 3")
plt.xlabel("X values")
plt.ylabel("Y values that fit the solution")
plt.savefig('17102017.png')
plt.show()    