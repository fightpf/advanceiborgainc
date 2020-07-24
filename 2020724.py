# num=eval(input("請輸入一個待檢查的數字"))
# count=2
# while count<num**0.5:
#     if num%count==0 and num!=2 :
#         ##print("不是質數")##
#         break
#     count+=1
# else:
#     print("是質數")








def prime_search(target_num):
    result=[]
    #target_num=eval(input("請輸入一個待檢查的數字"))
    for num in range(2,target_num):
        count=2
        while count<=(num**0.5+1):
            if num%count==0 and num!=2 : 
                break
            count+=1
        else:
            result.append(num)
    return result
answer=prime_search(100000)
answer=prime_search(10000)
answer=prime_search(1000)
print(answer)





def testfun(n): #local 
    n=n+1
    print("這是testfun裡面")
    return n
def testfun2(n):
    n=n+2
testfun(3)



#遞迴函式
def rec(n):
    if n==1:
        return 1
    return n+rec(n-1)
print(rec(100))
n=eval(input("請輸入欲尋找費氏數數列第n項"))
count=1
while count<n:
    if n==1 and n ==2 :
        print(1)
        break
    n1=1
    n2=1
    answer=n1+n2
    n1,n2=n2,answer
    count+=1
print(answer)

n=eval(input("請輸入欲尋找費氏數數列第n項"))
count=3
n1=1
n2=1
if n==1 or n==2:
    print(1)
else:
    while count<=n:
        count+=1
        answer=n1+n2
        n1,n2=n2,answer
    print(answer)

def feb(n):
    if n==1 or n==2:
        return 1
    return feb(n-1)+feb(n-2)

def climate(n):
    global cache
    cache={}
    def feb(n):
        if n==1 or n==2:
            return 1
        if n in cache:
            return cache[n]
        cache[n]=feb(n-1)+feb(n-2)
        return cache[n]
    return feb(n)
print(climate(50))
print(cache)

print(feb(10))