class Canvas2:

    P1=None
    P2=None
    R=None

    A=[0.0,0.0]
    B=[0.0,0.0]

    def __init__(self,r,p1,p2):
        self.R=r
        self.P1=p1
        self.P2=p2
        self.Initialize()

    def __str__(self):
       return str(self.P1)+" "+str(self.P2)+" "+str(self.R)+" "+str(self.A)+" "+ str(self.B)

    #Initialize Parameters A,B from R,P1 and P2
    
    def Initialize(self):
        self.A[0]=(1.0*(self.R[0] ))/(1.0*( self.P2[0]-self.P1[0] ))
        self.A[1]=(1.0*(self.R[1] ))/(1.0*( self.P1[1]-self.P2[1] ))
                                                   
        self.B[0]=-self.A[0]*self.P1[0]
        self.B[1]=-self.A[1]*self.P2[1]
        

    #Convert geometric point to pixels.
    
    def Point_2_Pixels(self,p):
        px=[0,0]
        for i in range(2):
            px[i]=self.A[i]*p[i]+self.B[i]
            
        return px
    
    #Convert geometric points to pixels.
    
    def Points_2_Pixels(self,ps):
        pxs=[]
        for p in ps:
            pxs.append(  self.Point_2_Pixels(p) )
            
        return pxs
