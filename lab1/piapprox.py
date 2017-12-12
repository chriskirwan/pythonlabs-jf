#Section 0: Opening Section
# #####
import matplotlib.pyplot as plt
import numpy as np 

# ####
# Section 1: Creating Circular Arc
# ####
circle_x = np.linspace(0,1,100)
circle_y = np.sqrt(1-circle_x**2) 

fig1 = plt.figure() 
fig1.set_size_inches(5, 5)
plt.plot(circle_x, circle_y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# ####
# Section 2: Generating Random Points
# ####
times= 2000
x = np.random.rand(times)
y = np.random.rand(times)

#Circular Arc with Random Points
fig2 = plt.figure() 
fig2.set_size_inches(5, 5)
plt.plot(x, y, 'o', markersize=1)
plt.plot(circle_x, circle_y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# ####
# Section 3: Calculating Pi Estimation
# ####
dist=np.sqrt(x**2 + y**2)
incircle = dist <= 1

incircle_ratio=float(np.sum(incircle))/float(len(incircle))

pi = incircle_ratio * 4
print ('The estimated value of pi is: ', pi)

# ####
# Section 4: Estimations vs Exact
# ####
cumulative_incircle = np.cumsum(incircle)
cumulative_ratios = (cumulative_incircle / np.arange(1,times+1,dtype=np.float))
pis = cumulative_ratios * 4


plt.figure() 
approx_pis, = plt.plot(pis)
pi, = plt.plot(np.repeat(np.pi, times))
plt.ylim(3.1, 3.3)
plt.xlabel("Sample Size")
plt.legend([approx_pis,pi],["Approximation","Exact Value"])
plt.show()

# ####
#Section 5: Standard Deviation vs Sample Size
# ####
def cummean(arr):
    return np.cumsum(arr)/np.arange(1,len(arr)+1,dtype=np.float)
    
def cumstd(arr):
    return np.sqrt(cummean(arr ** 2) - cummean(arr) ** 2) 

plt.figure() 
stdevs, = plt.plot(cumstd(pis))
plt.legend([stdevs], ["Standard Deviation"])
plt.xlabel("Sample Size")
plt.show()

# ####
#Section 6: Integrating x^2 
# ####
rx = np.random.rand(times)
ry = np.random.rand(times)

fig3 = plt.figure()
fig3.set_size_inches(5, 5)
xs = np.linspace(0, 1, 100)
plt.plot(xs, xs ** 2)
plt.plot(rx, ry, 'o', markersize=1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

c_inside = np.cumsum(ry < rx ** 2)
print (float(np.sum(ry < rx ** 2)) / float(times))

vs = c_inside / np.arange(1,times+1,dtype=np.float)
plt.figure()
plt.plot(vs)
plt.xlabel("Sample Size")
plt.show()

plt.figure()
plt.plot(cumstd(vs))
plt.xlabel("Sample Size")
plt.show()

# ####
#Section 7: Integrating our chosen function 
# ####

sx = np.random.rand(times)
sy = np.random.rand(times)

fig4 = plt.figure()
fig4.set_size_inches(5, 5)
xf = np.linspace(0, 1, 100)
plt.plot(xf, np.sqrt(xf))
plt.plot(sx, sy, 'o', markersize=1)
plt.show()

c_inside = np.cumsum(sy < np.sqrt(sx))
print (float(np.sum(sy < np.sqrt(sx))) / float(times))

df = c_inside / np.arange(1,times+1,dtype=np.float)
plt.figure()
plt.plot(df)
plt.xlabel("Sample Size")
plt.show()

plt.figure()
plt.plot(cumstd(df))
plt.xlabel("Sample Size")
plt.show()
