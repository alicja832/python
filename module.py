import random
import math
import matplotlib.pyplot as plt
class IFS:
    "'Iterated Function System'"
    def __init__(self,p1,p2=True):
        self.x=[0]
        self.y=[0]
        self.p1=p1
        self.p2=p2
        if not p2:
            self.p2=[1 for i in p1]
    def metod(self,it):
        self.it=it
        i=1
        while((i+1)<it):
            k1=random.choices(self.p1,self.p2)
            k=k1[0]
            self.x.append(k[0]*self.x[i-1]+k[1]*self.y[i-1]+k[2])
            self.y.append(k[3]*self.x[i-1]+k[4]*self.y[i-1]+k[5])
            i+=1
    def rys(self,s):
        "'parametr'"
        plt.scatter(self.x,self.y,1)
        #plt.show()
        plt.savefig(s)
        plt.clf()

class Wektor3D:
    "'Vector 3D contains x,y,z'"
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,b):
        if not isinstance(b, Wektor3D):
            raise ValueError
        x=self.x+b.x
        y=self.y+b.y
        z=self.z+b.z
        return Wektor3D(x,y,z)
    def __sub__(self,b):
        if not isinstance(b, Wektor3D):
            raise ValueError
        x=self.x-b.x
        y=self.y-b.y
        z=self.z-b.z
        return Wektor3D(x,y,z)
    def __mul__(self,b):
        if not isinstance(b, (float,int)):
            raise ValueError
        x=b*self.x
        y=b*self.y
        z=b*self.z
        return Wektor3D(x,y,z)
    def length(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    def skalar(self,b):
        if not isinstance(b, Wektor3D):
            raise ValueError
        return self.x*b.x+self.y*b.y+self.z*b.z
    def wektor(self,b):
        if not isinstance(b, Wektor3D):
            raise ValueError
        return Wektor3D(self.y*b.z-self.z*b.y,-(self.x*b.z-self.z*b.x),self.x*b.y-self.y*b.x)
    def mixed(self,b,c):
        "'iloczyn mieszany'"
        if not isinstance(b, Wektor3D):
            raise ValueError
        r=self.wektor(b).skalar(c)
        return r
    def __str__(self):
        return f'x={self.x},y={self.y},z={self.z},'



def strumien(a,b):
    if not isinstance(a, Wektor3D) or not isinstance(b, Wektor3D):
            raise ValueError
    return a.skalar(b)

def Lorenc(g,e,v,b):
    if not isinstance(e, Wektor3D) or not isinstance(v, Wektor3D) or not isinstance(b, Wektor3D):
            raise ValueError
    return (e+v.wektor(b))*g

def Praca(g,e,v):
    if not isinstance(e, Wektor3D) or not isinstance(v, Wektor3D):
            raise ValueError
    return (q*e).skalar(v)