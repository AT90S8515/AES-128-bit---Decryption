#r3=['63', 'ca', 'b7', '04', '09', '53', 'd0', '51', 'cd', '60', 'e0', 'e7', 'ba', '70', 'e1', '8c']
r2=['63', '53', 'e0', '8c', '09', '60', 'e1', '04', 'cd', '70', 'b7', '51', 'ba', 'ca', 'd0', 'e7']
#ip=['5f','72','64','15','57','f5','bc','92','f7','be','3b','29','1d','b9','f9','1a']
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
print 'Input:',r2
print 'Output:',isr(r2)
