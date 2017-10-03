from Vector  import *
from Hyperbola import Hyperbola

C=O()
a=2.0

b1=1.0
b2=20.0

N=100

db=1.0*(b2-b1)/( 1.0*(N-1) )

A=[
    [-1.0,0.0],
    [0.0,1.0],
]

R=[
    [0.0,-1.0],
    [1.0,0.0],
]



b=b1
for n in range(N):
    curve=Hyperbola(a,b,C,N)
    curve.Rs()

    curve.Init_Canvas()

    fname="Hyperbola/"+("%03d" % n)+".svg"
    options={
        "stroke": 'blue',
        "style": {
            "stroke-width": 2,
        }
    }
    svg=[]
    
    #Hyperbolas embracing X

    #Left hand part
    rsm=Map_Affin_Vectors(curve.rs,A)
    
    svg=svg+curve.Curve_SVG_Line(options,curve.rs)
    svg=svg+curve.Curve_SVG_Line(options,rsm)
    
    #Hyperbolas embracing Y
    rsp=curve.rs
    
    #Upper part
    rsp=Map_Affin_Vectors(curve.rs,R,None,1)
    
    
    options[ "stroke" ]='green'
    svg=svg+curve.Curve_SVG_Line(options,rsp)
    
    options[ "stroke" ]='red'
    assymptotes=curve.Assymptotes()
    for assymptote in assymptotes:
        px1=curve.Canvas.Point_2_Pixels(assymptote[0])
        px2=curve.Canvas.Point_2_Pixels(assymptote[1])
        svg=svg+[ curve.SVG_Line(px1,px2,options) ]
            
    

    curve.SVG_2_File(fname,svg)
    
    b+=db
