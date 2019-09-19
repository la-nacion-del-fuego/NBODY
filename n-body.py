#!/usr/bin/env python3
#
# n-body.py Solve the n-body problem using Newton
# 
# Copyright (C) 2019  Victor De la Luz (vdelaluz@enesmorelia.unam.mx)
#                      
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


G=6.674e-11         #m^3kg^-1s^-2

class Particle:
    """
    Particle
    =======
    Es una clase que permite analizar el comportamiento de 2 particulas

    METODOS:

      *setdt: p boligatoria, v obligatoria, m obligatoria, dt opcional
          Asigna la delta t
      
      *computeR: dt obligatoria
         Calcula la distancia de las particulas

      *computeU: p1 obligatoria
         Calcula el verctor direccion

      *integrate: B boligatoria
         Se encargaba de integrar la varaible sobre algo

      *getPosition:
         Regresa la posicion de la particula
    """
    def __init__(self, p, v, m, dt=1):
        self.p = p
        self.v = v
        self.m = m
        self.dt = dt

    def setdt(self,dt):
        self.dt = dt
    
    def computeR(self,p1):
        r = math.sqrt( (p1[0]-self.p[0])**2 + (p1[1]-self.p[1])**2 + (p1[2]-self.p[2])**2)
        return r

    def computeU(self,p1):
        u=[0,0,0]
        i=0
        for a,b in zip(self.p,p1):
            u[i] = b - a
            i+=1
        return u
    
    #def integrate(self,dt,p1,m1):
    def integrate(self,B):
        r = self.computeR(B.p)
        u = self.computeU(B.p)

        Vx=(G*B.m*self.dt/(r**3))*u[0]
        Vy=(G*B.m*self.dt/(r**3))*u[1]
        Vz=(G*B.m*self.dt/(r**3))*u[2]

        self.v[0] += Vx
        self.v[1] += Vy
        self.v[2] += Vz
        
        self.p = [self.p[0]+ (self.v[0]+Vx) *dt,self.p[1]+ (self.v[1]+Vy)*dt,self.p[2]+ (self.v[2]+Vz)*dt]

    def getPosition(self):
        return self.p

    def getVelocity(self):
        return self.v

    def getKineticEnergy(self):
        k= (1/2)*self.m*(math.sqrt( self.v[0]^2 +self.v[1]^2+self.v[2]^2))
        return k

    #def setdt(self):
        
#def plotting(fig,ax,time,y1,title,filename,caption):
#    ax.plot(time,y1,label=caption)
#    ax.set(x)

    
p0=[5e-2, 1e-2, 0.0]  #m
v0=[0.0, 0.0, 0.0]  #m/s
m=1e6               #kg

p1=[0.0, 0.0, 0.0]  #m
v1=[1.0, 0.0, 0.0]  #m/s
m1=1.0               #kg


dt=0.001              #sec

A = Particle(p0,v0,m)
B = Particle(p1,v1,m1)

B.setdt(dt)

x=[] #tiempo
y = [] #posicion
v = [] #velocidad
a = [] #aceleracion

x.append(0.0)
#y.append(B.getPosition()[0])
y.append(B.getPosition())
v.append(B.getVelocity()[0])
a.append(0.0)
v1 = B.getVelocity()[0]
#lastX = B.getPosition()[0]



#for t in range(1,100):
#    lastX = B.getPosition()[0]
#    lastV = v1
#    B.integrate(A)
#    print(B.getPosition())
#    x.append(float(t)*dt)
#    y.append(B.getPosition()[0])
#    v1 = (B.getPosition()[0]-lastX)/B.dt
#    v.append(v1)
#    a.append((v1-lastV)/B.dt)

for t in range(1,100):
    B.integrate(A)
    x.append(float(t)*dt)
    y.append(B.getPosition())

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

for point in y:
    ax.scatter(point[0],point[1],point[2],marker=m)
#fig,ax = plt.subplots(3)
#ax[0].plot(x,y)
#ax[0].set(xlabel="time [sec]",ylabel="distance [km]",title="n-body")
#ax[0].grid()

#ax[1].plot(x,v)
#ax[1].set(xlabel="time [Sec]", ylabel="distance [km]")
#ax[1].grid()

#ax[2].plot(x,a)
#ax[2].set(xlabel="time [sec]", ylabel="acceleration [km/s^2]")
#ax[2].grid()

plt.show()


