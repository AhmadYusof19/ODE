import numpy as np
import matplotlib.pyplot as plt

N=1000 #Number of iterations

im=500
nr=N-im+4
nl=im+4
psiR=np.zeros([505],float)
psiL=np.zeros([505],float)     
#define wavefnctions as empty array for both sides 
h=0.02 #mesh points
x0l=-10
x0r=10
#important quantity
mc2=940
k=9.4
amin=78; amax=92; e=amin
cb=(h*h)/12 #constants of h**12

def V(x):                   #define potential wavefunciton
    v= 4.7 *x*x
    return v

# now , define the k2 for both sides and the parameters
k2l=np.zeros([1000],float)
k2r=np.zeros([1000],float)#kena buat float

#give the first value for 1st 2 value of wavefunction
psiR[0]=0; psiL[0]=0;
psiR[1]=0.00001; psiL[1]=0.00001
#define x for each side, an array
xL=np.arange(x0l,0.02,0.02); xR= np.arange(x0r,-0.02,-0.02)

#set k2 for each side, k2 = sqrt (e-v)^2

def sk2(e):
    for i in range(0,N):
        xl=x0l+i*h
        xr=x0r-i*h
        #calculate the constant,
        f=0.04829
        k2l[i]=f*(e-V(xl))
        k2r[i]=f*(e-V(xr))

# set numerov method for the adjacent solution
def numerov(N,h,k2,u,e):
    sk2(e)
    for i in range(1, N):
        u[i+1]=(((1-5*cb*k2[i])*2*u[i])-((1+cb*k2[i-1])*u[i-1]))/(1+cb*k2[i+1])
        
#last step is to find the difference, use central difference method
def beza(e):
    numerov(nl, h, k2l, psiL, e)
    numerov(nr, h, k2r, psiR, e)
    fd=(psiR[nr-3]+psiL[nl-3]-psiR[nr-5]-psiL[nl-5])/(h*psiR[nr-4])
    return fd

#calculate the eigenvalue sue bisection
tol =1e-4

istep=0 # for bisection's iteration
x1 = np.arange(-10,.02,0.02);   x2 = np.arange(10,-0.02,-0.02)
fig = plt.figure()                        
ax = fig.add_subplot(111)
ax.grid()
while abs(beza(e)) > tol:
    e=(amin+amax)/2
    print(e,istep)
    if beza(e)*beza(amax)>0:
        amax=e
    else: 
        amin= e
        plt.text(3,-200,'Energy= %10.4f'%(e),fontsize=14)
        plt.plot(x1,psiL[:-4])
        plt.plot(x2,psiR[:-4])
        plt.xlabel("x")
        plt.ylabel("$\psi(x) $", fontsize=17)
        plt.title('R & L Wavefunctions Matched at x = 0')
        istep=istep+1
        plt.pause(0.5)
plt.show()        
        

