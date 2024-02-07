# decimal to 16bits unsigned binary number
# if dec>pow(2,16), will saturate at 4'hFFFF

# Using bin() or int() may be a better solution

def Dto16Bu(dec):				#type:int
    b=[]
    for p in range(15,-1,-1):
        if(dec-pow(2,p))>=0:
            b.append("1")
            dec=dec-pow(2,p)
        else:
            b.append("0")
    Bjoin="".join(b)
    return Bjoin				#type:string
