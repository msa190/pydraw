from math import *

from Vector import *
from Curve  import Curve

class Ellipse(Curve):
    
    #Center
    C=Vector([0.0,0.0])
    
    #Half axis'
    a=0.0
    b=0.0
    
    def __init__(self,a=1.0,b=2.0,C=None,NP=0):
        if (C):  self.C=C
        if (NP): self.NP=NP
        
        self.a=a
        self.b=b
        
        self.Closed=True
        
        return
    
    def R(self,t):
        return Vector([
            self.C[0]+self.a*cos(t),
            self.C[1]+self.b*sin(t),
        ])
    
    def PMin(self):
        return Vector([-self.a,-self.a])
    
    def PMax(self):
        return Vector([self.a,self.a])
