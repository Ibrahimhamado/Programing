desmantNumber=[]
binaryNumber=[]
y=0
while True:
    x=input("enter number")
    for i in range(len(x)):
        if x[i]=='0' or x[i]=='1' :
            b=int(x[i])
            y=b*2**(len(x)-i-1)
            binaryNumber.append(x[i])
            desmantNumber.append(y)
        else:
            print('invaled input')
            break
    print("the number is:",x[:],sum(desmantNumber[:]))
    z=input('prees any key to continue or n to finsh')
    desmantNumber.clear()
    if z=='N' or z=='n':
        break
print('finish')