import matplotlib.pyplot as plt
import numpy as np 
import math

g=9.81   #gravitational constant
dt=1e-3   #integration time step ie. Delta-t
v0=40   #initial speed at t=0

angle = math.pi/5    # launch angle (in radians); math.pi = 3.14
time = np.arange(0,10,dt)   # time axis
vx0=math.cos(angle)*v0    # initital velocity (x-axis)
vy0=math.sin(angle)*v0    #initial velocity (y-axis)

xa=vx0*time   #compute x-coordinate
ya=-0.5*g*time**2+vy0*time   #compute y-coordinate#

fig1=plt.figure()
plt.plot(xa,ya)
plt.xlabel("x")
plt.ylabel("y")

# ############
# traj() : function that computes trajectory 
#          for some launch angle ans starting 
#          velocity x,y component of v0
# ############
def traj(angle,v0) :
    vx0=math.cos(angle)*v0  
    vy0=math.sin(angle)*v0  

    x=np.zeros(len(time))
    y=np.zeros(len(time))

    x[0],y[0]=0,0   #initial position (0,0) 
    x[1],y[1]=x[0]+vx0*dt,y[0]+vy0*dt #secoond elements of x and y are determined by v0

    i=1
    while y[i]>=0:
        x[i+1]=(2*x[i]-x[i-1])
        y[i+1]=(2*y[i]-y[i-1])-g*dt**2
    
        i=i+1
    x=x[0:i+1]
    y=y[0:i+1]
    return x,y, (dt*i),x[i]

x, y, duration, distance = traj(angle,v0)
print ('Distance:',distance)
print ('Duration:',duration)

# ####
# Calculating 
# ####

n=31
angles=np.linspace(0,math.pi/2,n)
maxrange=np.zeros(n)

for i in range(n): 
    x,y,duration,maxrange[i] = traj(angles[i],v0)

angles=angles/2/math.pi*360   # conversion of rads to deg

fig2=plt.figure()
plt.plot(angles,maxrange)
plt.xlabel("Launch Angle")
plt.ylabel("Range")

print ("Optimum Angle:",angles[np.where(maxrange==np.max(maxrange))])


z=31
velocities=np.linspace(0,40,z)
maxrrange=np.zeros(z)

for i in range(z):
    x,y,duration,maxrange[i] = traj(angle, velocities[i])
    
fig3=plt.figure()
plt.plot(velocities, maxrange)
plt.xlabel("Launch Velocity")
plt.ylabel("Range")
