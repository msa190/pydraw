from Vector import *
from Curve  import Curve

class Circle(Curve):

    #Center
    C=Vector([0.0,0.0])

    #Radius
    r=0.0

    def __init__(self,r=1.0,C=None,NP=0):
        if (C): self.C=C
        if (NP): self.NP=NP
        
        self.r=r
        self.Closed=True
        
        return
    
    def R(self,t):
        return self.C+e(t)*self.r

    def PMin(self):
        return Vector([-self.r,-self.r])
    
    def PMax(self):
        return Vector([self.r,self.r])
