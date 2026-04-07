import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig , ejes = plt.subplots()
x = np.linspace(0,2*np.pi)

linea, = ejes.plot(x,np.cos(x))

def cuadro(n):
    linea.set_ydata( np.cos(x - n/20) )
    return linea,

animacion = FuncAnimation(fig,cuadro,frames=100, interval = 45,blit=False)

plt.show()