# there's MIPStoMC.md for user guide

import re
def split_cmd(cmd):
    cmd=str.lower(cmd)
    result = re.split(r'[,\s(]+', cmd)
    #print(result)
    return(result)
def Dto5B(dec):
    b=[]
    for p in range(4,-1,-1):
        if(dec-pow(2,p))>=0:
            b.append("1")
            dec=dec-pow(2,p)
        else:
            b.append("0")
    Bjoin="".join(b)
    return Bjoin
def Dto16Bu(dec):
    b=[]
    for p in range(15,-1,-1):
        if(dec-pow(2,p))>=0:
            b.append("1")
            dec=dec-pow(2,p)
        else:
            b.append("0")
    Bjoin="".join(b)
    return Bjoin
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
def converter(res):
    MC=""
    if(res[0]=="sll"):
        #R-type: shifting
        #SLL rd,rt,sa	Shift Left Logical	rd=rt<<sa	000000	rs	rt	rd	sa	000000
        op="000000"
        rsbin="00000"
        fn="000000"
        rdint=int(res[1:])
        rdbin=Dto5B(rdint)
        rtint=int(res[2][1:])
        rtbin=Dto5B(rtint)
        saint=int(res[3])
        sabin=Dto5B(saint)
        MC=op+rsbin+rtbin+rdbin+sabin+fn
        print(op,rsbin,rtbin,rdbin,sabin,fn)
    if(res[0]=="sra"):
        #SRA rd,rt,sa	Shift Right Arithmetic	rd=rt>>sa	000000	00000	rt	rd	sa	000011
        op="000000"
        rsbin="00000"
        fn="000011"
        rdint=int(res[1:])
        rdbin=Dto5B(rdint)
        rtint=int(res[2][1:])
        rtbin=Dto5B(rtint)
        saint=int(res[3])
        sabin=Dto5B(saint)
        MC=op+rsbin+rtbin+rdbin+sabin+fn
        print(op,rsbin,rtbin,rdbin,sabin,fn)
    if(res[0]=="srl"):
        #SRL rd,rt,sa	Shift Right Logical	rd=rt>>sa	000000	rs	rt	rd	sa	000010
        op="000000"
        rsbin="00000"
        fn="000010"
        rdint=int(res[1:])
        rdbin=Dto5B(rdint)
        rtint=int(res[2][1:])
        rtbin=Dto5B(rtint)
        saint=int(res[3])
        sabin=Dto5B(saint)
        MC=op+rsbin+rtbin+rdbin+sabin+fn
        print(op,rsbin,rtbin,rdbin,sabin,fn)
    if(res[0]=="sllv"):
        #SLLV rd,rt,rs	Shift Left Logical Variable	rd=rt<<rs	000000	rs	rt	rd	00000	000100
        op="000000"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        shamt="00000"
        fn="000100"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="srav"):
        #SRAV rd,rt,rs	Shift Right Arithmetic Variable	rd=rt>>rs	000000	rs	rt	rd	00000	000111
        op="000000"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        shamt="00000"
        fn="000111"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="srlv"):
        #SRLV rd,rt,rs	Shift Right Logical Variable	rd=rt>>rs	000000	rs	rt	rd	00000	000110
        op="000000"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        shamt="00000"
        fn="000110"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    #R-type: arithmatic operation
    if(res[0]=="add"):
        #ADD rd,rs,rt   rd=rs+rt	000000	rs	rt	rd	00000	100000
        op="000000"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        shamt="00000"
        fn="100000"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="addu"):
        op="000000"
        shamt="00000"
        fn="100001"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="sub"):
        #SUB rd,rs,rt	rd=rs-rt	000000	rs	rt	rd	00000	100010
        op="000000"
        shamt="00000"
        fn="100010"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="subu"):
        op="000000"
        shamt="00000"
        fn="100011"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    #R-type: logical operation
    if(res[0]=="and"):
        op="000000"
        shamt="00000"
        fn="100100"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="nor"):
        op="000000"
        shamt="00000"
        fn="100111"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="or"):
        op="000000"
        shamt="00000"
        fn="100101"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="xor"):
        op="000000"
        shamt="00000"
        fn="100110"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    #R-type: comparison
    if(res[0]=="slt"):
        op="000000"
        shamt="00000"
        fn="101010"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="sltu"):
        op="000000"
        shamt="00000"
        fn="101011"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[3][1:])
        rtbin=Dto5B(rtint)
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    #R-type: multiplication and division
    if(res[0]=="div"):
        #DIV rs,rt	Divide	HI=rs%rt; LO=rs/rt	000000	rs	rt	0000000000	011010
        op="000000"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[2][1:])
        rtbin=Dto5B(rtint)
        rdbin="00000"
        shamt="00000"
        fn="011010"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="divu"):
        #DIVU rs,rt	Divide Unsigned	HI=rs%rt; LO=rs/rt	000000	rs	rt	0000000000	011011
        op="000000"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[2][1:])
        rtbin=Dto5B(rtint)
        rdbin="00000"
        shamt="00000"
        fn="011011"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="mult"):
        #MULT rs,rt	Multiply	HI,LO=rs*rt	000000	rs	rt	0000000000	011000
        op="000000"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[2][1:])
        rtbin=Dto5B(rtint)
        rdbin="00000"
        shamt="00000"
        fn="011000"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="multu"):
        #MULTU rs,rt	Multiply Unsigned	HI,LO=rs*rt	000000	rs	rt	0000000000	011001
        op="000000"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[2][1:])
        rtbin=Dto5B(rtint)
        rdbin="00000"
        shamt="00000"
        fn="011001"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="mfhi"):
        #MFHI rd	Move From HI	rd=HI	000000	0000000000	rd	00000	010000
        op="000000"
        rsbin="00000"
        rtbin="00000"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        shamt="00000"
        fn="010000"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="mflo"):
        #MFLO rd	Move From LO	rd=LO	000000	0000000000	rd	00000	010010
        op="000000"
        rsbin="00000"
        rtbin="00000"
        rdint=int(res[1][1:])
        rdbin=Dto5B(rdint)
        shamt="00000"
        fn="010010"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="mthi"):
        #MTHI rs	Move To HI	HI=rs	000000	rs	000000000000000	010001
        op="000000"
        rdbin="00000"
        rtbin="00000"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        shamt="00000"
        fn="010001"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="mtlo"):
        #MTLO rs	Move To LO	LO=rs	000000	rs	000000000000000	010011
        op="000000"
        rdbin="00000"
        rtbin="00000"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        shamt="00000"
        fn="010011"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    #i-type:logical and arithmatic
    if(res[0]=="addi"):
        #ADDI rt,rs,imm  ---->  001000	rs	rt	imm
        op="001000"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        immint=int(res[3])
        imm_bin=Dto16Bs(immint)
        MC=op+rsbin+rtbin+imm_bin   
        print(op,rsbin,rtbin,imm_bin)
    if(res[0]=="addiu"):
        #ADDIU rt,rs,imm	Add Immediate Unsigned	rt=rs+imm	001001	rs	rt	imm
        op="001001"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        immint=int(res[3])
        imm_bin=Dto16Bu(immint)
        MC=op+rsbin+rtbin+imm_bin   
        print(op,rsbin,rtbin,imm_bin)
    if(res[0]=="andi"):
        #ANDI rt,rs,imm	And Immediate	rt=rs&imm	001100	rs	rt	imm
        op="001100"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        immint=int(res[3])
        imm_bin=Dto16Bs(immint)
        MC=op+rsbin+rtbin+imm_bin   
        print(op,rsbin,rtbin,imm_bin)
    if(res[0]=="ori"):
        #ORI rt,rs,imm	Or Immediate	rt=rs|imm	001101	rs	rt	imm
        op="001101"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        immint=int(res[3])
        imm_bin=Dto16Bs(immint)
        MC=op+rsbin+rtbin+imm_bin   
        print(op,rsbin,rtbin,imm_bin)
    if(res[0]=="slti"):
        #SLTI rt,rs,imm	Set On Less Than Immediate	rt=rs<imm	001010	rs	rt	imm
        op="001010"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        immint=int(res[3])
        imm_bin=Dto16Bs(immint)
        MC=op+rsbin+rtbin+imm_bin   
        print(op,rsbin,rtbin,imm_bin)
    if(res[0]=="sltiu"):
        #SLTIU rt,rs,imm	Set On < Immediate Unsigned	rt=rs<imm	001011	rs	rt	imm
        op="001011"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        immint=int(res[3])
        imm_bin=Dto16Bu(immint)
        MC=op+rsbin+rtbin+imm_bin   
        print(op,rsbin,rtbin,imm_bin)
    if(res[0]=="lui"):
        #LUI rt,imm	Load Upper Immediate	rt=imm<<16	001111	rs	rt	imm
        op="001111"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        immint=int(res[3])
        imm_bin=Dto16Bu(immint)
        MC=op+rsbin+rtbin+imm_bin   
        print(op,rsbin,rtbin,imm_bin)
    if(res[0]=="xori"):
        #XORI rt,rs,imm	Exclusive Or Immediate	rt=rs^imm	001110	rs	rt	imm
        op="001110"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rsint=int(res[2][1:])
        rsbin=Dto5B(rsint)
        immint=int(res[3])
        imm_bin=Dto16Bu(immint)
        MC=op+rsbin+rtbin+imm_bin   
        print(op,rsbin,rtbin,imm_bin)
    #i-type: branches
    if(res[0]=="beq"):
        #BEQ rs,rt,offset	Branch On Equal	if(rs==rt) pc+=offset*4	000100	rs	rt	offset
        op="000100"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[2][1:])
        rtbin=Dto5B(rtint)
        offset=int(res[3])
        offset_bin=Dto16Bs(offset)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="bne"):
        #BNE rs,rt,offset	Branch On Not Equal	if(rs!=rt) pc+=offset*4	000101	rs	rt	offset
        op="000101"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtint=int(res[2][1:])
        rtbin=Dto5B(rtint)
        offset=res[3]
        offset_bin=Dto16Bs(offset)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="bgez"):
        #BGEZ rs,offset	Branch On >= 0	if(rs>=0) pc+=offset*4	000001	rs	00001	offset
        op="000001"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtbin="00001"
        offset=res[2]
        offset_bin=Dto16Bs(offset)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="bgezal"):
        #BGEZAL rs,offset	Branch On >= 0 And Link	r31=pc; if(rs>=0) pc+=offset*4	000001	rs	10001	offset
        op="000001"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtbin="10001"
        offset=res[2]
        offset_bin=Dto16Bs(offset)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="bgtz"):
        #BGTZ rs,offset	Branch On > 0	if(rs>0) pc+=offset*4	000111	rs	00000	offset
        op="000111"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtbin="00000"
        offset=res[2]
        offset_bin=Dto16Bs(offset)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="blez"):
        #BLEZ rs,offset	Branch On	if(rs<=0) pc+=offset*4	000110	rs	00000	offset
        op="000110"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtbin="00000"
        offset=res[2]
        offset_bin=Dto16Bs(offset)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="bltz"):
        #BLTZ rs,offset	Branch On < 0	if(rs<0) pc+=offset*4	000001	rs	00000	offset
        op="000001"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtbin="00000"
        offset=res[2]
        offset_bin=Dto16Bs(offset)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="bltzal"):
        #BLTZAL rs,offset	Branch On < 0 And Link	r31=pc; if(rs<0) pc+=offset*4	000001	rs	10000	offset
        op="000001"
        rsint=int(res[1][1:])
        rsbin=Dto5B(rsint)
        rtbin="10000"
        offset=res[2]
        offset_bin=Dto16Bs(offset)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="break"):
        #BREAK	Breakpoint	epc=pc; pc=0x3c	000000	code	001101
        op="000000"
        fn="001101"
        code="00000000000000000000"
        MC=op+code+fn
        print(op,code,fn)
    if(res[0]=="syscall"):
        #SYSCALL	System Call	epc=pc; pc=0x3c	000000	00000000000000000000	001100
        op="000000"
        fn="001100"
        code="00000000000000000000"
        MC=op+code+fn
        print(op,code,fn)
    #j-type
    if(res[0]=="j"):
        #J target	Jump	pc=pc_upper|(target<<2)	000010	target
        op="000010"
        target=res[1]
        MC=op+target
        print(op,target)
    if(res[0]=="jal"):
        #JAL target	Jump And Link	r31=pc; pc=target<<2	000011	target
        op="000011"
        target=res[1]
        MC=op+target
        print(op,target)
    if(res[0]=="jalr"):
        #JALR rs	Jump And Link Register	rd=pc; pc=rs	000000	rs	00000	rd	00000	001001
        op="000000"
        rsint=int(res[1])
        rsbin=Dto5B(rsint)
        rtbin="00000"
        rdbin="pcreg"
        shamt="00000"
        fn="001001"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="jr"):
        #JR rs	Jump Register	pc=rs	000000	rs	000000000000000	001000
        op="000000"
        rsint=int(res[1])
        rsbin=Dto5B(rsint)
        rtbin="00000"
        rdbin="00000"
        shamt="00000"
        fn="001000"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="mfc0"):
        #MFC0 rt,rd	Move From Coprocessor	rt=CPR[0,rd]	010000	00000	rt	rd	00000000000
        op="010000"
        rsbin="00000"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rdint=int(res[2][1:])
        rdbin=Dto5B(rdint)
        shamt="00000"
        fn="000000"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    if(res[0]=="mtc0"):
        #MTC0 rt,rd	Move To Coprocessor	CPR[0,rd]=rt	010000	00100	rt	rd	00000000000
        op="010000"
        rsbin="00100"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        rdint=int(res[2][1:])
        rdbin=Dto5B(rdint)
        shamt="00000"
        fn="000000"
        MC=op+rsbin+rtbin+rdbin+shamt+fn
        print(op,rsbin,rtbin,rdbin,shamt,fn)
    #i-type: memory access instruction
    if(res[0]=="lw"):
        #LW rt,offset(rs)	Load Word	rt=*(int*)(offset+rs)	100011	rs	rt	offset
        op="100011"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        offset=int(res[2])
        offset_bin=Dto16Bs(offset)
        rsint=int(res[3][1:-1])
        rsbin=Dto5B(rsint)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="sw"):
        #SW rt,offset(rs)	SW rt,offset(rs)	Store Word	*(int*)(offset+rs)=rt	101011	rs	rt	offset
        op="101011"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        offset=int(res[2])
        offset_bin=Dto16Bs(offset)
        rsint=int(res[3][1:-1])
        rsbin=Dto5B(rsint)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="lb"):
        #LB rt,offset(rs)	Load Byte	rt=*(char*)(offset+rs)	100000	rs	rt	offset
        op="100000"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        offset=int(res[2])
        offset_bin=Dto16Bs(offset)
        rsint=int(res[3][1:-1])
        rsbin=Dto5B(rsint)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="lbu"):
        #LBU rt,offset(rs)	Load Byte Unsigned	rt=*(Uchar*)(offset+rs)	100100	rs	rt	offset
        op="100100"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        offset=int(res[2])
        offset_bin=Dto16Bs(offset)
        rsint=int(res[3][1:-1])
        rsbin=Dto5B(rsint)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="lh"):
        #LH rt,offset(rs)	Load Halfword	rt=*(short*)(offset+rs)	100001	rs	rt	offset
        op="100001"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        offset=int(res[2])
        offset_bin=Dto16Bs(offset)
        rsint=int(res[3][1:-1])
        rsbin=Dto5B(rsint)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="lhu"):
        #LHU rt,offset(rs)	Load Halfword Unsigned	rt=*(Ushort*)(offset+rs)	100101	rs	rt	offset
        op="100101"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        offset=int(res[2])
        offset_bin=Dto16Bs(offset)
        rsint=int(res[3][1:-1])
        rsbin=Dto5B(rsint)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="sb"):
        #SB rt,offset(rs)	Store Byte	*(char*)(offset+rs)=rt	101000	rs	rt	offset
        op="101000"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        offset=int(res[2])
        offset_bin=Dto16Bs(offset)
        rsint=int(res[3][1:-1])
        rsbin=Dto5B(rsint)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    if(res[0]=="sh"):
        #SH rt,offset(rs)	Store Halfword	*(short*)(offset+rs)=rt	101001	rs	rt	offset
        op="101001"
        rtint=int(res[1][1:])
        rtbin=Dto5B(rtint)
        offset=int(res[2])
        offset_bin=Dto16Bs(offset)
        rsint=int(res[3][1:-1])
        rsbin=Dto5B(rsint)
        MC=op+rsbin+rtbin+offset_bin
        print(op,rsbin,rtbin,offset_bin)
    return MC

def main(file_path):
    output_path=file_path[:-4]+"_MC.txt"

    cmds=[]
    f = open(file_path)
    for line in f.readlines():
        cmds.append(line)
    f.close

    fout = open(output_path, 'w')
    for x in cmds:
        res=split_cmd(x)
        MC=converter(res)
        print(MC,file=fout)
    fout.close

######-----main funtion starts here-----#####

file_path=r"copy your file path here"
main(file_path)
