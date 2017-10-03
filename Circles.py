from Vector import Vector,O
from Circle import Circle

C=O()
for n in range(2,101):
    curve=Circle(1.0,C,n)
    curve.Rs()

    curve.Init_Canvas()

    fname="Circle/"+("%03d" % n)+".svg"
    options={
        "stroke": 'black',
        "style": {
            "stroke-width": 2,
        }
    }
    
    curve.Curve_SVG_Line_Write(fname,options)
