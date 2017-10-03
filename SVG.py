from Tag import Tag
from File import File_Read,File_Write

class SVG(Tag):
    Header="Header.svg"

    def SVG_2_File(self,fname,svg):
        text=File_Read(self.Header)
        text=text+[ self.SVG_Start() ]
        text=text+svg
        text=text+[ self.SVG_End() ]
        
        File_Write(fname,text,True)

    def SVG_Start(self,options={}):
        roptions=dict(options)
        
        roptions[ "version" ]=1.1
        
        roptions[ "width" ]=self.Resolution[0]
        roptions[ "height" ]=self.Resolution[1]
        roptions[ "viewbox" ]=" ".join([
            '0','0',
            str(self.Resolution[0]),
            str(self.Resolution[1])
        ])
        roptions[ "xmlns" ]='http://www.w3.org/2000/svg'

        return self.Tag("svg",roptions)
    
    def SVG_End(self):
        return self.Tag_Close("svg")
        
    def SVG_Point(self,px,options={},r=5):
        roptions=dict(options)

        roptions[ "cx" ]=px[0]
        roptions[ "cy" ]=px[1]
        roptions[ "r" ]=r
        
        return self.Tag1("circle",roptions)
    
    def SVG_Line(self,px1,px2,options={}):
        roptions=dict(options)

        roptions[ "x1" ]=px1[0]
        roptions[ "y1" ]=px1[1]
        roptions[ "x2" ]=px2[0]
        roptions[ "y2" ]=px2[1]
        
        return self.Tag1("line",roptions)
