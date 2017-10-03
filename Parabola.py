from Vector import *
from Curve  import Curve

class Parabola(Curve):

    #Parameters
    a=1.0
    b=0.0
    c=0.0

    NP=100
    t1=-2.0
    t2=2.0
    
    def __init__(self,a=1.0,b=0.0,c=0.0,NP=0):
        self.a=a
        self.b=b
        self.c=c
        if (NP): self.NP=NP
        
        return
    
    def R(self,t):
        return Vector([
            t,
            self.a*t**2.0+self.b*t+self.c
        ])

    def PMin(self):
        return Vector([self.t1,-1.0])
    
    def PMax(self):
        return Vector([self.t2,self.t2**2.0 ])
    
    def Discriminant(self):
        return self.b**2.0-4.0*self.a*self.c
    
    def Vertex(self):
        return Vector([
            -self.b/(2.0*self.a),
            -self.Discriminant()/(4.0*self.a)
        ])
