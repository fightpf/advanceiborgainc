#例外處理
try:
    a=list(range(20))
    for i in range(30):
        print(a[i])   #out of range

except:
    print("你的list長度不對")