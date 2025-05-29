tmp=[0]*10
s=input()
for i in s: tmp[int(i)]+=1
if (sum(tmp[3:8])+tmp[9])>0: print(0)
else:
    if tmp[0]>0 and tmp[1]>0 and tmp[2]>0 and tmp[8]>0 :
        if tmp[0]== tmp[1] ==tmp[2]==tmp[8]: print(8)
        else: print(2)
    else: print(1)