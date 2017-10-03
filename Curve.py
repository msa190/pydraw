from math import *
from Vector import Vector

from Canvas2 import Canvas2
from SVG import SVG
from File import File_Write

class Curve(SVG):
    Resolution=[300,300]
    Canvas=None
    Name="Curve"

    t1=0.0
    t2=2*pi
    NP=100

    Close=False

    def __init__(self):
        return

    def __str__(self):
        text=[]
        for n in range( len(self.rs) ):
            text.append(    str(self.ts[n])+": "+str(self.rs[n])   )

        return "\n".join(text)


    def Init_Canvas(self,pmin=None,pmax=None,resolution=None):
        if (not pmin): pmin=self.PMin()
        if (not pmax): pmax=self.PMax()
        if (not resolution): resolution=self.Resolution
        
        self.Canvas=Canvas2(resolution,pmin,pmax)


    def R(self,t):
        #Calculate point for parameter value t
        return Vector([
            cos(t),
            sin(t)
        ])

    def Rs(self):
        #Calculate self.NP points for parameter values between
        #self.t1 and self.t2
        dt=(self.t2-self.t1)/(1.0*(self.NP-1))

        #Store in self.rs and self.ts
        self.rs=[]
        self.ts=[]
        
        t=self.t1
        for i in range( self.NP ):
            self.rs.append( self.R(t) )
            self.ts.append(t)
            
            t+=dt

        return self.rs

    def Pxs(self,rs=[]):
        if (not rs): rs=self.rs
        
        self.pxs=self.Canvas.Points_2_Pixels(rs)

        return self.pxs
    
    def Curve_SVG_Line(self,options,rs=[]):
        #Draw curve as line segments
        if (not rs): rs=self.rs

        pxs=self.Pxs(rs)
        
        svg=[]
        for i in range( 1,self.NP ):
            svg.append(   self.SVG_Line( pxs[i-1],pxs[i],options )   )

        if (self.Close):
            svg.append(   self.SVG_Line( pxs[len(pxs)-1],pxs[0],options )   )
            
        return svg
    
    def Curve_SVG_Line_Write(self,fname,options,rs=[]):
        self.SVG_2_File(
            fname,
            self.Curve_SVG_Line(options,rs)
        )
        
