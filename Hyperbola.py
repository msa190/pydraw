from math import *

from Vector import *
from Curve  import Curve

class Hyperbola(Curve):
    
    #Center
    C=Vector([0.0,0.0])

    #Parameters
    a=1.0
    b=0.0

    t1=-2.0
    t2=2.0
    
    def __init__(self,a=1.0,b=0.0,C=None,NP=0):
        if (C):  self.C=C
        if (NP): self.NP=NP
        
        self.a=a
        self.b=b

        return
    
    def R_Hyp(self,t):
        return Vector([
            self.C[0]+self.a*cosh(t),
            self.C[1]+self.a*sin(t),
        ])
    
    def R(self,s):
        return Vector([
            self.C[0]+self.a*sqrt(1.0+s**2.0),
            self.C[1]+self.b*s
        ])

    def Assymptotes(self):
        xm=self.a*sqrt(1.0+self.t2**2.0)
        ym=self.b*xm/(1.0*self.a)

        return [
            [
                self.C+Vector([-xm,-ym]),
                self.C+Vector([ xm, ym])
            ],
            [
                self.C+Vector([ xm,-ym]),
                self.C+Vector([-xm, ym])
            ]
        ]
        
    def Assymptotes_SVG(self,options):
        svg=[]
        for assymptote in self.Assymptotes():
            px1=curve.Canvas.Point_2_Pixels(assymptote[0])
            px2=curve.Canvas.Point_2_Pixels(assymptote[1])
            
            svg.append(  self.SVG_Line(px1,px2,options)   )
            
        return svg       

    def PMin(self):
        return Vector([-self.a*sqrt(1.0+self.t2**2.0),-20.0*self.t2])
    
    def PMax(self):
        return Vector([self.a*sqrt(1.0+self.t2**2.0),20.0*self.t2])
