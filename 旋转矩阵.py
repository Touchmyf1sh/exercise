import numpy as np

a = np.array([[1,2],
              [2,3]])
b = np.array([[np.cos(90*np.pi/180),-np.sin(90*np.pi/180)],
              [np.sin(90*np.pi/180),np.cos(90*np.pi/180)]]) #顺时针旋转90度

c = np.dot(a,b)
print(a)
print(b)
print(c)