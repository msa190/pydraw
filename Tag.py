
class Tag():
    def Options_2_Text(self,options):
        #Get a copy!
        roptions=dict(options)

        if options.has_key("style"):
            styles=[]
            for opt in roptions[ "style" ]:
                text=opt+": "+str(   roptions[ "style" ][ opt ]   )
                styles.append(text)

            roptions[ "style" ]="; ".join(styles)

        rroptions=[]
        for key in roptions.keys():
            text=key+'="'+str(   roptions[ key ]   )+'"'
            rroptions.append(text)

        empty=""
        if (len(rroptions)>0): empty=" "

        return empty+" ".join(rroptions)
    
    def Tag(self,tag,options):
        return "<"+tag+self.Options_2_Text(options)+">"
    
    def Tag1(self,tag,options):
        return "<"+tag+self.Options_2_Text(options)+"/>"
    
    def Tags(self,tag,contents,options):
        return "<"+tag+self.Options_2_Text(options)+">"+contents+self.Tag_Close(tag)
    
    def Tag_Close(self,tag):
        return "</"+tag+">"
    
