import numpy as np

# initial conditions
t = 0
x, y = 1, 1/2
vx, vy = -1/2, 1/3
w = np.asarray([x, y, vx, vy])

# parameters
h = 0.01
tend = 12

def f(w, t):
    x, y, vx, vy = w
    return np.asarray([vx, vy, -x, -y])

while t<tend:
    w = w + h*f(w, t)
    t = t + h
    print("%3.3e %3.3e %3.3e %3.3e %3.3e" %(t, w[0], w[1], w[2], w[3]))
    
