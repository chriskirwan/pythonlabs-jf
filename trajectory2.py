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


# ###############
# traj_fric(): function that computes trajectory 
#              for some launch angle and starting 
#              velocity x,y component of v0
# ##############

def traj_fric(angle,v0) :
    vx0=math.cos(angle)*v0  
    vy0=math.sin(angle)*v0  

    x=np.zeros(len(time))
    y=np.zeros(len(time))
   

    x[0],y[0]=0,0   #initial position (0,0) 
    x[1],y[1]=x[0]+vx0*dt,y[0]+vy0*dt #secoond elements of x and y are determined by v0

    i=1
    f=0.5*0.005*(100-y[i])*dt
    while y[i]>=0:
        x[i+1]=(2*x[i]-x[i-1] + f*x[i-1])/((1+f))
        y[i+1]=((2*y[i]-y[i-1])+(f*y[i-1])-g*dt**2)/(1+f)
    
        i=i+1
    x=x[0:i+1]
    y=y[0:i+1]
    return x,y, (dt*i),x[i]

x, y, duration_fric, distance_fric = traj_fric(angle,v0)
print ('Distance:',distance_fric)
print ('Duration:',duration_fric)

fig1=plt.figure()
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")

v=30
angles=np.linspace(0,math.pi/2,v)
maxrange=np.zeros(v)


for i in range(v):
        x,y,duration_fric,maxrange[i] = traj_fric(angles[i],v0)

angles=angles/2/math.pi*360   # conversion of rads to deg  
  
fig2=plt.figure()
plt.plot(angles,maxrange)
plt.xlabel("Launch Angle")
plt.ylabel("Range")


print ("Optimum Angle:",angles[np.where(maxrange==np.max(maxrange))])

z=30
velocities=np.linspace(0,40,z)
maxrange=np.zeros(z)

for i in range(z):
    x,y,duration_fric,maxrange[i] = traj_fric(angle,velocities[i])
    
fig3=plt.figure()
plt.plot(velocities,maxrange)
plt.xlabel("Launch Velocity")
plt.ylabel("Range")