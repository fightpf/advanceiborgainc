def test(name='這裡是主程式'):#預設值
    print("helloworld",name)



if __name__=="__main__":##__XXXX__ 屬性
    pass


#執行程式時，將程式化為一個python物件
#該執行的程式名稱即為main
#希望我寫的程式，被外部引用時
#在__name__:__main__裡的都不會執行

#蒙地卡羅模擬 當一個模型明確的邊界條件
# import random as rd
# n=1000000
# count=1
# answer=0
# while count<=n:
#     x=rd.uniform(-1,1)
#     y=rd.uniform(-1,1)
#     if (x**2+y**2)**0.5 <=1:
#         answer+=1
#     count+=1
# answer=answer/n
# print(answer*4)

poker=list(range(1,53))
import random as rd
n=0
count=1000
while n<=count:
    rdnum1,rdnum2=int(rd.random()*52%52),int(rd.random()*52%52)
    while rdnum2==rdnum1:
        rdnum2=int(rd.random()*52%52)
    poker[rdnum1],poker[rdnum2]=poker[rdnum2],poker[rdnum1]
    n+=1
first,second=poker[0],poker[1]
def drop_card(card):  
    kind,num=card//13,card%13
    if num==0: 
        kind=kind-1
        num=13
    if kind==0: print("黑桃",end=" ")
    if kind==1: print("愛心",end=" ")
    if kind==2: print("菱形",end=" ")
    if kind==3: print("梅花",end=" ")
    print(num)
drop_card(first),drop_card(second)
