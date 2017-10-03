from Vector   import *
from Parabola import Parabola

a=1.0
c=0.0

b1=-2.0
b2=2.0

N=100
NP=100

db=1.0*(b2-b1)/( 1.0*(N-1) )

parabola=Parabola(-a,0.0,c,NP)
parabola.Rs()

b=b1
for n in range(N):
    curve=Parabola(a,b,c,NP)
    curve.Rs()

    curve.Init_Canvas()

    #Transfer Canvas
    parabola.Canvas=curve.Canvas

    fname="Parabola/"+("%03d" % n)+".svg"
    options={
        "stroke": 'blue',
        "style": {
            "stroke-width": 2,
        }
    }

    svg=[]
    svg=svg+curve.Curve_SVG_Line(options)
    
    options[ "stroke" ]='green'
    svg=svg+parabola.Curve_SVG_Line(options)

    vertex=curve.Vertex()
    vertexx=curve.Canvas.Point_2_Pixels(vertex)
    options[ "stroke" ]='red'
    svg=svg+[ curve.SVG_Point(vertexx,options) ]

    curve.SVG_2_File(fname,svg)
    
    b+=db
