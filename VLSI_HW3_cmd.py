# This part is  editing sp file, replace .PROBE.... by the comment below
#modify (in),(out)...by your pin lable
'''
.param vdd=1.8
.PROBE TRAN
+    I(c0)
+    I(c0)
+    V(out)
+    V(in)
.TRAN 1e-9 100e-9 START=0.0
.meas TRAN Trise TRIG V(in) VAL='0.9' RISE=2
+    TARG V(out) VAL='0.9' RISE=2
.meas TRAN Tfall TRIG V(in) VAL='0.9' FALL=2
+    TARG V(out) VAL='0.9' FALL=2

.meas TRAN Ic0 max I(c0)
'''

# This part is generating .alter case to simulate 45PVT corner
# note that when you run this program, 
# you should clean the txt file first,
# otherwise the data will be appended to the file
# copy the output text and paste before the last line "end"
p=["ss","ff","tt","snfp","fnsp"]
TEMP=[0,25,75]
vdd=[1.62,1.8,1.98]
# will create alter.txt in the directory of this python file
path = 'alter.txt'
f = open(path, 'w')

for i in p:
    for j in vdd:
        for k in TEMP:
            print(f".alter {i} {j} {k}",file=f)
            #Second ,vt11330 -> your workstation name
            print(r'.LIB "/home/vlsi113_TJ/vt11330/UM180FDKMFC00000OA_B02/Models/Hspice/mm180_reg18_v124.lib"',i,file=f)
            print(f'.param vdd={j}',file=f)
            print(f'.TEMP={k}',file=f)
            
f.close()
