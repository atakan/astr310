import numpy as np

def Ene(w):
    x, y, vx, vy = w
    KE = 1/2*(vx*vx + vy*vy)
    PE = 1/2*(x*x + y*y)
    return KE+PE


def f(w, t):
    x, y, vx, vy = w
    return np.asarray([vx, vy, -x, -y])

# initial conditions
t = 0
x, y = 1, 1/2
vx, vy = -1/2, 1/3
w = np.asarray([x, y, vx, vy])
E0 = Ene(w)

# parameters
h = 0.01/2
tend = 12
while t<tend:
    w = w + h*f(w, t)
    t = t + h
    E = Ene(w)
    Eerr = (E-E0)/E0
    #print("%3.3e %3.3e %3.3e %3.3e %3.3e %3.3e" %(t, Eerr, w[0], w[1], w[2], w[3]))
    print("%3.3e" %(t), end=' ')
    print("%3.3e" %(Eerr), end=' ')
    print("%3.3e %3.3e %3.3e %3.3e" %(w[0], w[1], w[2], w[3]), end=' ')
    print("")
    
