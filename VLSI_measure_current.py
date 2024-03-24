# note that when you run this program, 
# you should clean the txt file first,
# otherwise the data will be appended to the file

p=["ss","ff","tt","snfp","fnsp"]
TEMP=[0,25,75]
vdd=[1.62,1.8,1.98]
# First, create a  "alter.txt" in the directory where you are running this code
path = 'alter.txt'
f = open(path, 'w')

for i in p:
    for j in vdd:
        for k in TEMP:
            print(".meas tran Ic0 max I(c0)",file=f)
            print(f".alter {i} {j} {k}",file=f)
            #Second ,vt11330 -> your workstation name
            print(r'.LIB "/home/vlsi113_TJ/vt11330/UM180FDKMFC00000OA_B02/Models/Hspice/mm180_reg18_v124.lib"',i,file=f)
            print(f'.param vdd={j}',file=f)
            print(f'.TEMP={k}',file=f)
            
f.close()
