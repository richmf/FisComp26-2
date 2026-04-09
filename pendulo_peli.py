import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si
from matplotlib.animation import FuncAnimation


def pendulo_doble(t,th_vth):
    g = 9.81
    # th_vth = [th1 , th2 , vth1 , vth2]
    dth1 = th_vth[2]
    dth2 = th_vth[3]
    d_th1th2 = th_vth[0]-th_vth[1]
    den = 3 -np.cos(2*d_th1th2)
    dvth1 = -3*g*np.sin(th_vth[0]) - g*np.sin(th_vth[0]-2*th_vth[1]) 
    -2*np.sin(d_th1th2)*(th_vth[3]**2 + th_vth[2]**2*np.cos(d_th1th2))
    dvth1 = dvth1/den
    dvth2 = 2*np.sin(d_th1th2)*(2*th_vth[2]**2 + 
                                2*g*np.cos(th_vth[0]) + th_vth[3]**2*np.cos(d_th1th2))
    dvth2 = dvth2/den
    return np.array([dth1,dth2,dvth1,dvth2])

def th2xy(th_vth):
    x1 = np.sin(th_vth[0])
    y1 = -np.cos(th_vth[0])
    x2 = x1 + np.sin(th_vth[1])
    y2 = y1 -np.cos(th_vth[1])
    return x1,y1,x2,y2

ci = [0.5,0.5,0,0]
titf = (0,100)
sol_pendulo = si.solve_ivp(pendulo_doble,titf,ci,rtol=1e-8,atol=1e-10,
                        dense_output=True)
print(sol_pendulo.success)

t = np.linspace(titf[0],titf[1],1000)
th_vth = sol_pendulo.sol(t)
x1,y1,x2,y2 = th2xy(th_vth)

figura , ejes = plt.subplots()

masa1, = ejes.plot(x1[0],y1[0],'o')
masa2, = ejes.plot(x2[0],y2[0],'o')
cuerda1, = ejes.plot([0,x1[0]],[0,y1[0]])
cuerda2, = ejes.plot( [x1[0],x2[0]] , [y1[0],y2[0]])
ejes.set_xlim([-2.1,2.1]) , ejes.set_ylim([-2.1,0])

def cuadro(n):
    masa1.set_xdata(x1[n])
    masa1.set_ydata(y1[n])
    masa2.set_xdata(x2[n])
    masa2.set_ydata(y2[n])
    cuerda1.set_data([0,x1[n]],[0,y1[n]])
    cuerda2.set_data([x1[n],x2[n]],[y1[n],y2[n]])
    return masa1,masa2,

animacion = FuncAnimation(figura,cuadro,frames=len(t), interval = 41,blit=False)

plt.show()











