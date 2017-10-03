from Vector  import *
from Ellipse import Ellipse

C=O()
a=2.0

b1=1.0
b2=2.0

N=100

db=1.0*(b2-b1)/( 1.0*(N-1) )

b=b1
for n in range(N):
    curve=Ellipse(a,b,C,N)
    curve.Rs()

    curve.Init_Canvas()

    fname="Ellipse/"+("%03d" % n)+".svg"
    options={
        "stroke": 'blue',
        "style": {
            "stroke-width": 2,
        }
    }
    
    curve.Curve_SVG_Line_Write(fname,options)
    b+=db
