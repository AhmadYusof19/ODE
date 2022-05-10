# -*- coding: utf-8 -*-
"""
Created on Sun May  8 00:43:05 2022

@author: yusof
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('Results.txt', unpack=True)

ee=np.array(data[2,:])   
f=np.array(data[3,:])
nr=len(ee)
n=75 #Interval to work
defE=1239.8/0.4 #default standard deviation of Excitation
lmin=200
lmax=800

std=1e7/defE
std2=1/defE
    
for i in range(nr):
    ee[i]=1239.8/ee[i]
    
x=np.linspace(lmin,lmax,n)
Ee=np.zeros((len(x),nr))
for i in range(n):
    for j in range(nr):
        Ee[i][j]=Ee[i][j-1]+1.3062974e8*(f[j]/std)*np.exp(-((1/x[i]-1/ee[j])/std2)**2)
E1=np.zeros((len(x)))
for k in range(n):
    for l in range(nr):
        if l==nr-1:
            E1[k]=Ee[k][l]
plt.plot(x,E1)
plt.xlabel('Wavelength (nm)')
plt.ylabel("Exitation energy (Absorbsion)")
plt.title("Absorption Plot of Gaussian Distribution")          