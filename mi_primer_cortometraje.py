import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig , ejes = plt.subplots()
x = np.linspace(0,2*np.pi)

#linea, = ejes.plot(x,np.cos(x))
linea, = ejes.plot([],[])
ejes.set_xlim(x[0],x[-1]) , ejes.set_ylim(-1.1,1.1)


def inicio():
    linea.set_data([],[])
    ejes.set_xlim(x[0],x[-1]) , ejes.set_ylim(-1.1,1.1)
    return linea,
    
def cuadro(n):
    linea.set_data( x , np.cos(x - n/20) )
    return linea,

animacion = FuncAnimation(fig , cuadro , frames=100 , interval = 45 ,
                          init_func=inicio , blit=True)
#animacion = FuncAnimation(fig , cuadro , frames=100 , interval = 45 , blit=True)

#animacion.save('mi_peli.mp4')

plt.show()