def File_Read(fname):
    f=open(fname,"r" )
    if (not f):
        print "Unable to read from file: ".fname
        exit()
        
    lines=f.read()

    f.close()
    return lines.split("\n")


def File_Write(fname,lines,tell=False):
    #Remove trailing empty lines
    while (lines and not lines[ len(lines)-1 ]):
        lines.pop(len(lines)-1)

    f=open(fname,"w" )
    if (not f):
        print "Unable to write to file: ".fname
        exit()
        
    size=0
    for line in lines:
        f.write("%s\n" % line)
        size+=len(line)
            
    f.close()

    if (tell):
        if (tell!=True):
            fname=tell
        print "\t"+fname+" ("+str(size)+" bytes)"
    return True

