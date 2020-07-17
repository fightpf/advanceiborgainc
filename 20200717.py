a=[0,7,1,5,4,9,11,555,12,313,561,23125,123,253,12]
for i in range(len(a)):        #將len(a)個數字，作排列
    for j in range(len(a)-i-1):#將最大的數字推到最右
        if a[j]>a[j+1]:        #當前數比後數大就交換
            a[j],a[j+1]=a[j+1],a[j]
print(a)


a=5
#*
#**
#***
#****
#*****
for i in range(1,a+1):
    print("*"*i)
#str(), + 合併字串
#       * 連續輸出字串

for i in range(a):
    for j in range(i+1):
        print("*",end="")
    print("")

a=153
b=[100,50,10,5,1]
#c=[1,1,0,0,3]
c=[]
for i in b:
    answer=a//i# first i==50
    a=a%i
    c.append(answer)
for i in range(len(c)):
    print("需要",b[i],"元",c[i],"個")
#1個100元
#1個50元
#0個10元
#0個5元
#3個1元
c=[]
answer=3
c.append(answer)    #[3]
c.append(2)         #[3,2]
c.append(1)         #[3,2,1]
#print(c)            #[3,2,1]


#迴圈控制
num=1
while num<=100: 
    if num%2==0:       #遇到偶數跳過
        num+=1
        continue
    print(num)
    num+=1
    
#continue  強制進入下一層迴圈
#break     結束目前迴圈
#pass      什麼多不做

#3 5 7 9 最小公倍數
num=10000
while True:
    if num%3==0 and num%5==0 and num%7==0 and num%9==0:
        print(num)
        break 
    num-=1 #num+=1 == num=num+1 
           #num-=1 == num=num-1

#3 5 7 9 小於10000中 最大的倍數

while False:   #  當while迴圈順利結束時 執行else 
    pass
else:
    pass


target=eval(input("請輸入一個質數"))
for j in range(2,int(target**0.5)+1):
    if target%j==0:
        print(target,"不是質數")       #100
                                      #2,4,5,10,20,25,50
        break
else:
    print(target,"是質數")

#輸入1000，印出1000以下所有質數

