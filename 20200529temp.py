poker=list(range(1,53))
import random as rd
#rd.seed(30)
n=0
count=1000
while n<=count:
    rdnum1,rdnum2=int(rd.random()*51),int(rd.random()*51)
    while rdnum2==rdnum1:
        rdnum2=int(rd.random()*51)
    poker[rdnum1],poker[rdnum2]=poker[rdnum2],poker[rdnum1]
    n+=1
first,second=poker[0],poker[1]
def drop_card(card):  
    kind,num=card//13,card%13
    if kind==0: print("黑桃",end=" ")
    if kind==1: print("愛心",end=" ")
    if kind==2: print("菱形",end=" ")
    if kind==3: print("梅花",end=" ")
    print(num+1)
drop_card(first),drop_card(second)






a=[1,2,3,4,5,6,7,8]
b=[1,2,3,4,5,6,7,8]
length=0
for i in a:
    for j in b:
        if i==j:
            length+=1
            break
print(length)

