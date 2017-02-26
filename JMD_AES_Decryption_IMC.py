import math
def rshift(N,N1):return N[-N1:]+N[:-N1]
sbox=[['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76'],['ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0'],['b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15'],['04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75'],['09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84'],['53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf'],['d0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8'],['51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2'],['cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73'],['60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db'],['e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79'],['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08'],['ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a'],['70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e'],['e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df'],['8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16']]
s14=[['00', '0e', '1c', '12', '38', '36', '24', '2a', '70', '7e', '6c', '62', '48', '46', '54', '5a'], ['e0', 'ee', 'fc', 'f2', 'd8', 'd6', 'c4', 'ca', '90', '9e', '8c', '82', 'a8', 'a6', 'b4', 'ba'], ['db', 'd5', 'c7', 'c9', 'e3', 'ed', 'ff', 'f1', 'ab', 'a5', 'b7', 'b9', '93', '9d', '8f', '81'], ['3b', '35', '27', '29', '03', '0d', '1f', '11', '4b', '45', '57', '59', '73', '7d', '6f', '61'], ['ad', 'a3', 'b1', 'bf', '95', '9b', '89', '87', 'dd', 'd3', 'c1', 'cf', 'e5', 'eb', 'f9', 'f7'], ['4d', '43', '51', '5f', '75', '7b', '69', '67', '3d', '33', '21', '2f', '05', '0b', '19', '17'], ['76', '78', '6a', '64', '4e', '40', '52', '5c', '06', '08', '1a', '14', '3e', '30', '22', '2c'], ['96', '98', '8a', '84', 'ae', 'a0', 'b2', 'bc', 'e6', 'e8', 'fa', 'f4', 'de', 'd0', 'c2', 'cc'], ['41', '4f', '5d', '53', '79', '77', '65', '6b', '31', '3f', '2d', '23', '09', '07', '15', '1b'], ['a1', 'af', 'bd', 'b3', '99', '97', '85', '8b', 'd1', 'df', 'cd', 'c3', 'e9', 'e7', 'f5', 'fb'], ['9a', '94', '86', '88', 'a2', 'ac', 'be', 'b0', 'ea', 'e4', 'f6', 'f8', 'd2', 'dc', 'ce', 'c0'], ['7a', '74', '66', '68', '42', '4c', '5e', '50', '0a', '04', '16', '18', '32', '3c', '2e', '20'], ['ec', 'e2', 'f0', 'fe', 'd4', 'da', 'c8', 'c6', '9c', '92', '80', '8e', 'a4', 'aa', 'b8', 'b6'], ['0c', '02', '10', '1e', '34', '3a', '28', '26', '7c', '72', '60', '6e', '44', '4a', '58', '56'], ['37', '39', '2b', '25', '0f', '01', '13', '1d', '47', '49', '5b', '55', '7f', '71', '63', '6d'], ['d7', 'd9', 'cb', 'c5', 'ef', 'e1', 'f3', 'fd', 'a7', 'a9', 'bb', 'b5', '9f', '91', '83', '8d']]
s11=[['00', '0b', '16', '1d', '2c', '27', '3a', '31', '58', '53', '4e', '45', '74', '7f', '62', '69'], ['b0', 'bb', 'a6', 'ad', '9c', '97', '8a', '81', 'e8', 'e3', 'fe', 'f5', 'c4', 'cf', 'd2', 'd9'], ['7b', '70', '6d', '66', '57', '5c', '41', '4a', '23', '28', '35', '3e', '0f', '04', '19', '12'], ['cb', 'c0', 'dd', 'd6', 'e7', 'ec', 'f1', 'fa', '93', '98', '85', '8e', 'bf', 'b4', 'a9', 'a2'], ['f6', 'fd', 'e0', 'eb', 'da', 'd1', 'cc', 'c7', 'ae', 'a5', 'b8', 'b3', '82', '89', '94', '9f'], ['46', '4d', '50', '5b', '6a', '61', '7c', '77', '1e', '15', '08', '03', '32', '39', '24', '2f'], ['8d', '86', '9b', '90', 'a1', 'aa', 'b7', 'bc', 'd5', 'de', 'c3', 'c8', 'f9', 'f2', 'ef', 'e4'], ['3d', '36', '2b', '20', '11', '1a', '07', '0c', '65', '6e', '73', '78', '49', '42', '5f', '54'], ['f7', 'fc', 'e1', 'ea', 'db', 'd0', 'cd', 'c6', '0f', 'a4', 'b9', 'b2', '83', '88', '95', '9e'], ['47', '4c', '51', '5a', '6b', '60', '7d', '76', '1f', '14', '09', '02', '33', '38', '25', '2e'], ['8c', '87', '9a', '91', 'a0', 'ab', 'b6', 'bd', 'd4', 'df', 'c2', 'c9', 'f8', 'f3', 'ee', 'e5'], ['3c', '37', '2a', '21', '10', '1b', '06', '0d', '64', '6f', '72', '79', '48', '43', '5e', '55'], ['01', '0a', '17', '1c', '2d', '26', '3b', '30', '59', '52', '4f', '44', '75', '7e', '63', '68'], ['b1', 'ba', 'a7', 'ac', '9d', '96', '8b', '80', 'e9', 'e2', 'ff', 'f4', 'c5', 'ce', 'd3', 'd8'], ['7a', '71', '6c', '67', '56', '5d', '40', '4b', '22', '29', '34', '3f', '0e', '05', '18', '13'], ['ca', 'c1', 'dc', 'd7', 'e6', 'ed', 'f0', 'fb', '92', '99', '84', '8f', 'be', 'b5', 'a8', 'a3']]
s13=[['00', '0d', '1a', '17', '34', '39', '2e', '23', '68', '65', '72', '7f', '5c', '51', '46', '4b'], ['d0', 'dd', 'ca', 'c7', 'e4', 'e9', 'fe', 'f3', 'b8', 'b5', 'a2', 'af', '8c', '81', '96', '9b'], ['bb', 'b6', 'a1', 'ac', '8f', '82', '95', '98', 'd3', 'de', 'c9', 'c4', 'e7', 'ea', 'fd', 'f0'], ['6b', '66', '71', '7c', '5f', '52', '45', '48', '03', '0e', '19', '14', '37', '3a', '2d', '20'], ['6d', '60', '77', '7a', '59', '54', '43', '4e', '05', '08', '1f', '12', '31', '3c', '2b', '26'], ['bd', 'b0', 'a7', 'aa', '89', '84', '93', '9e', 'd5', 'd8', 'cf', 'c2', 'e1', 'ec', 'fb', 'f6'], ['d6', 'db', 'cc', 'c1', 'e2', 'ef', 'f8', 'f5', 'be', 'b3', 'a4', 'a9', '8a', '87', '90', '9d'], ['06', '0b', '1c', '11', '32', '3f', '28', '25', '6e', '63', '74', '79', '5a', '57', '40', '4d'], ['da', 'd7', 'c0', 'cd', 'ee', 'e3', 'f4', 'f9', 'b2', 'bf', 'a8', 'a5', '86', '8b', '9c', '91'], ['0a', '07', '10', '1d', '3e', '33', '24', '29', '62', '6f', '78', '75', '56', '5b', '4c', '41'], ['61', '6c', '7b', '76', '55', '58', '4f', '42', '09', '04', '13', '1e', '3d', '30', '27', '2a'], ['b1', 'bc', 'ab', 'a6', '85', '88', '9f', '92', 'd9', 'd4', 'c3', 'ce', 'ed', 'e0', 'f7', 'fa'], ['b7', 'ba', 'ad', 'a0', '83', '8e', '99', '94', 'df', 'd2', 'c5', 'c8', 'eb', 'e6', 'f1', 'fc'], ['67', '6a', '7d', '70', '53', '5e', '49', '44', '0f', '02', '15', '18', '3b', '36', '21', '2c'], ['0c', '01', '16', '1b', '38', '35', '22', '2f', '64', '69', '7e', '73', '50', '5d', '4a', '47'], ['dc', 'd1', 'c6', 'cb', 'e8', 'e5', 'f2', 'ff', 'b4', 'b9', 'ae', 'a3', '80', '8d', '9a', '97']]
s9 =[['00', '09', '12', '1b', '24', '2d', '36', '3f', '48', '41', '5a', '53', '6c', '65', '7e', '77'], ['90', '99', '82', '8b', 'b4', 'bd', 'a6', 'af', 'd8', 'd1', 'ca', 'c3', 'fc', 'f5', 'ee', 'e7'], ['3b', '32', '29', '20', '1f', '16', '0d', '04', '73', '7a', '61', '68', '57', '5e', '45', '4c'], ['ab', 'a2', 'b9', 'b0', '8f', '86', '9d', '94', 'e3', 'ea', 'f1', 'f8', 'c7', 'ce', 'd5', 'dc'], ['76', '7f', '64', '6d', '52', '5b', '40', '49', '3e', '37', '2c', '25', '1a', '13', '08', '01'], ['e6', 'ef', 'f4', 'fd', 'c2', 'cb', 'd0', 'd9', 'ae', 'a7', 'bc', 'b5', '8a', '83', '98', '91'], ['4d', '44', '5f', '56', '69', '60', '7b', '72', '05', '0c', '17', '1e', '21', '28', '33', '3a'], ['dd', 'd4', 'cf', 'c6', 'f9', 'f0', 'eb', 'e2', '95', '9c', '87', '8e', 'b1', 'b8', 'a3', 'aa'], ['ec', 'e5', 'fe', 'f7', 'c8', 'c1', 'da', 'd3', 'a4', 'ad', 'b6', 'bf', '80', '89', '92', '9b'], ['7c', '75', '6e', '67', '58', '51', '4a', '43', '34', '3d', '26', '2f', '10', '19', '02', '0b'], ['d7', 'de', 'c5', 'cc', 'f3', 'fa', 'e1', 'e8', '9f', '96', '8d', '84', 'bb', 'b2', 'a9', 'a0'], ['47', '4e', '55', '5c', '63', '6a', '71', '78', '0f', '06', '1d', '14', '2b', '22', '39', '30'], ['9a', '93', '88', '81', 'be', 'b7', 'ac', 'a5', 'd2', 'db', 'c0', 'c9', 'f6', 'ff', 'e4', 'ed'], ['0a', '03', '18', '11', '2e', '27', '3c', '35', '42', '4b', '50', '59', '66', '6f', '74', '7d'], ['a1', 'a8', 'b3', 'ba', '85', '8c', '97', '9e', 'e9', 'e0', 'fb', 'f2', 'cd', 'c4', 'df', 'd6'], ['31', '38', '23', '2a', '15', '1c', '07', '0e', '79', '70', '6b', '62', '5d', '54', '4f', '46']]
mc=['14','11','13','9']
def binary(N):# hex(string) to binary(string) conversion 
    log=int(math.log(16,2))
    bits=len(N)*log
    return str(bin(int(N,16))[2:].zfill(bits))
def seg(N):
    oseg=[]
    for i in N:
        oseg.append(i)
    return oseg
def nonlst(N):
    s1=map(str,N)
    s1=''.join(s1)
    return s1
def hexa(N):# binary(string) to hex(string) conversion
    N=int(N,2)
    return hex(N).split('x')[1]
def devide(N):
    rpt1=0
    w=[]
    w1=[]
    w2=[]
    w3=[]
    w4=[]
    while rpt1<len(N):
        w.append(N[rpt1:(rpt1+2)])
        rpt1+=2
    w1.append(w[0])
    w1.append(w[1])
    w1.append(w[2])
    w1.append(w[3])
    w2.append(w[4])
    w2.append(w[5])
    w2.append(w[6])
    w2.append(w[7])
    w3.append(w[8])
    w3.append(w[9])
    w3.append(w[10])
    w3.append(w[11])
    w4.append(w[12])
    w4.append(w[13])
    w4.append(w[14])
    w4.append(w[15])
    return [w1,w2,w3,w4]
def select(N):#no
    if N=='14':
        N1=s14

    if N=='11':
        N1=s11

    if N=='13':
        N1=s13

    if N=='9':
        N1=s9
    return N1
def XOR(N,N1):#input:N=['11','22','33','44'],N1=['aa','bb','cc','dd'],output: xor of(N,N1)
    xora=[]
    rpt=0
    while rpt<4:
        bxor=seg(binary(N[rpt]))#converts '10' to '0','0','0','1','0','0','0','0'
        bxor1=seg(binary(N1[rpt]))#converts '10' to '0','0','0','1','0','0','0','0'
        oxor=xor(bxor,bxor1)#x oring gives binary out
        oxor=fixf(hexa(nonlst(oxor)))# converts segmented binary to hex
        xora.append(oxor)
        rpt+=1
    return xora
def lbyte(N):#input:['11','22','33','44'],output:['22','33','44','11']
    return N[1:]+N[:1]
def bs(r1):#no input:['11','22','33','44'];variable, output:BS of['11','22','33','44']
    r2=[]
    for i1 in r1:
        temp1=binary(i1)
        t1=temp1[0:4]
        t2=temp1[4:8]
        t1=int(t1,2)
        t2=int(t2,2)
        k2=sbox[t1][t2]
        r2.append(k2)
    return r2
def fix(N):#no IP:'00', OUT='00000000'
    N1=[[]for i in xrange(2)]
    N1[0]=bin(int(N[0],16)).split('b')[1]
    N1[1]=bin(int(N[1],16)).split('b')[1]
    j=0
    while j<2:
        var=N1[j]
        i=0
        ctr='0'
        while i<(4-len(var)-1):
            ctr=ctr+'0'
            i+=1
        if len(var)==4:
            pass
        else:
            N1[j]=ctr+var
        j+=1
    return (N1[0]+N1[1])
def fixf(N):
    if N=='0':
        N='00'
    elif N=='1':
        N='01'
    elif N=='2':
        N='02'
    elif N=='3':
        N='03'
    elif N=='4':
        N='04'
    elif N=='5':
        N='05'
    elif N=='6':
        N='06'
    elif N=='7':
        N='07'
    elif N=='8':
        N='08'
    elif N=='9':
        N='09'
    elif N=='a':
        N='0a'
    elif N=='b':
        N='0b'
    elif N=='c':
        N='0c'
    elif N=='d':
        N='0d'
    elif N=='e':
        N='0e'
    elif N=='f':
        N='0f'
    else:
        pass
    return N
def xor(N,N2):# N2(string) xor N3(string)[bitlevel]; output e is string list
    e=[]
    for i,j in zip(N,N2):
        if i==j:
            c='0'
        else:
            c='1'
        e.append(c)
    return e
def XORA(N,N1):#no IP:'00','11', OUT:'11'
    N=fix(N)
    N1=fix(N1)
    var1=''.join(xor(N,N1))
    return fixf(hex(int(var1,2)).split('x')[1])
def ri(N,N1):##for e xor r(i)##input:N: i.e.'1b',N1:integer(range(4,8,16,..,40)),output:string(hex(r of input))
    if N1==4:
        eri='01'

    if N1==8:
        eri='02'

    if N1==12:
        eri='04'

    if N1==16:
        eri='08'

    if N1==20:
        eri='10'

    if N1==24:
        eri='20'

    if N1==28:
        eri='40'

    if N1==32:
        eri='80'

    if N1==36:
        eri='1b'

    if N1==40:
        eri='36'
    rio= fixf(hexa(nonlst(xor(seg(binary(eri)),seg(binary(N))))))# e xor r(i):output:i.e.'1b'
    return rio
def transform(N,N1):#input:['11','22','33','44'], output:transform of['11','22','33','44']
    tf=bs(lbyte(N))
    tf1=ri(tf[0],N1)
    del tf[0]
    tf.insert(0,tf1)
    return tf
def poly(N):#no
    j=0
    opoly=[]
    while j<len(N):
        mc1=rshift(mc,j)
        i=0
        temp='00'
        while i<len(N):
            sp=select(mc1[i])
            temp=XORA(temp,sp[int(N[i][0],16)][int(N[i][1],16)])
            i+=1
        opoly.append(temp)
        j+=1
    return opoly
def step(N):# make a word of 2 hex digits
    t=0
    din=[]
    while t<len(N):
        a1=N[t]+N[t+1]
        din.append(a1)
        t+=2
    return din
def ibs(r1):#input:['11','22','33','44'];variable, output: ibs of ['11','22','33','44']
    r2=[]
    for i1 in r1:
        for i,x in enumerate(sbox):
            if i1 in x:
                a=hex(i).split('x')[1]+hex(x.index(i1)).split('x')[1]
                r2.append(a)
    return r2
def isr(r3):
    i=0
    r4=[]
    while i<(len(r3)/4):
        j=0
        while j<len(r3):
            r4.append(r3[i+j])
            j+=4
        i+=1
    r5=[[] for i in xrange(4)]
    i=j=0
    while i<len(r4):
        r5[j]=r4[i:i+4]
        r5[j]=r5[j][-j:]+r5[j][:-j]
        i+=4
        j+=1
    r6=r5[0]+r5[1]+r5[2]+r5[3]
    i=0
    r4=[]
    while i<(len(r6)/4):
        j=0
        while j<len(r6):
            r4.append(r6[i+j])
            j+=4
        i+=1
    return r4
def imc(N):
    rm5=[[] for i in xrange(4)]
    i=j=0
    while i<len(N):
        rm5[j]=N[i:i+4]
        i+=4
        j+=1
    return poly(rm5[0])+poly(rm5[1])+poly(rm5[2])+poly(rm5[3])
def iark(data,chavi):
    i=0
    rark=[]
    while i<len(data):
        rark.append(XORA(data[i],chavi[i]))
        i+=1
    return rark
def ks(N):
    Win=devide(N)
    indx=4
    while indx<44:
        if (indx%4)==0:
            tempks=XOR(Win[(indx-4)],transform(Win[(indx-1)],indx))
            Win.append(tempks)
        else:
            tempks=XOR(Win[(indx-4)],Win[(indx-1)])
            Win.append(tempks)
        indx+=1
    rpt=rpt1=0
    Roundin=[]
    while rpt<11:
        tround=Win[rpt1]+Win[rpt1+1]+Win[rpt1+2]+Win[rpt1+3]
        Roundin.append(tround)
        rpt+=1
        rpt1+=4
    return Roundin
#ip=['5f','72','64','15','57','f5','bc','92','f7','be','3b','29','1d','b9','f9','1a']
def iaes(cipher,Key):
    Round=ks(Key)
    step1=iark(step(cipher),Round[10])
    step1=isr(step1)
    step1=ibs(step1)
    i=0
    j=9
    while i<9:
        step1=iark(step1,Round[j])
        step1=imc(step1)
        step1=isr(step1)
        step1=ibs(step1)
        i+=1
        j-=1
    step1=iark(step1,Round[0])
    return ''.join(step1)
ip=raw_input('Enter Cipher text:')
key=raw_input('Enter the Encryption Key:')
print 'The Plain text:',iaes(ip,key)
