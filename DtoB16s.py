# decimal to 16bits signed binary number
# if dec>pow(2,15)-1, will saturate at 4'h7FFF
# if dec<-pow(2,15),  will saturate at 4'hFFFF

# Using bin() or int() may be a better solution

def Dto16Bs(istr):
    dec=int(istr)
    b=[]
    if(dec>=0):
        for p in range(15,-1,-1):
            if(dec-pow(2,p))>=0:
                b.append("1")
                dec=dec-pow(2,p)
            else:
                b.append("0")
    else:
        start=-pow(2,15)
        b.append("1")
        for e in range(14,-1,-1):
            if(start+pow(2,e))>dec:
                b.append("0")
            else:
                b.append("1")
                start=start+pow(2,e)
    Bjoin="".join(b)
    return Bjoin
