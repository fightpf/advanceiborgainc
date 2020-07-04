#while else用法
#當while後的布林值為False時跳至else區塊執行
#也可以理解為while區塊執行完畢後，執行else區塊


##找質數
num=eval(input("請輸入一個待檢查的數字"))
count=2
while count<num**0.5:
    if num%count==0 :
        print("不是質數")
        break
    count+=1
else:
    print("是質數")


target_num=eval(input("請輸入一個待檢查的數字"))
for num in range(2,target_num):
    count=2
    while count<=num**0.5:
        if num%count==0 : 
            break
        count+=1
    else:
        print(num)
        
        
#埃拉托色尼法
def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]

if __name__ == "__main__":
    print(eratosthenes(120))
#使用遞迴列印1~100
def countingnum(numb=0):
    print(numb)
    if numb==100:
        return 100

    else:
        return countingnum(numb+1)
countingnum()

##爬樓梯問題

##製造費波納係數列


#使用遞迴涵式製造費波納系數列
def recursor_test(numb):
    if numb==1 :
        return 1
    elif numb==0:
        return 0
    else:
        return recursor_test(numb-1)+recursor_test(numb-2)

##可使用with as 取代 open() ，優點在於不需要.close()關閉檔案
with open('demo.py', 'r', encoding='UTF-8') as file:
    for line in file:
        print(line, end='')


##例外處裡，若我們有可能遇到錯誤，但是不希望程式停下可使用以下關鍵字
#try:
#except:
#finally:
##try區塊若遇到例外事件，會跳至except並執行
#finnaly 區塊無論except區塊是否發生皆會執行
#也可以使用else關鍵字，當try區塊未觸發錯誤時，跳過except區塊至else



###沒有使用裝飾器decorator
def print_func_name(func):
    def wrap():
        print("Now use function '{}'".format(func.__name__))
        func()
    return wrap


def dog_bark():
    print("Bark !!!")


def cat_miaow():
    print("Miaow ~~~")


if __name__ == "__main__":
    print_func_name(dog_bark())
    print("---我是分隔線---")
    print_func_name(dog_bark)()
    print("---我是分隔線---")
    print_func_name(dog_bark)
    print("---我是分隔線---")    
    # print_func_name(dog_bark)只會return print_func_name本身，所以後方要再加一個括號呼叫print_func_name
    # > Now use function 'dog_bark'
    # > Bark !!!

    print_func_name(cat_miaow)()
    # > Now use function 'cat_miaow'
    # > Miaow ~~~
##使用裝飾器
def print_func_name2(func):
    def warp():
        print("Now use function '{}'".format(func.__name__))
        func()
    return warp


@print_func_name2
def dog_bark2():
    print("Bark !!!")


@print_func_name2
def cat_miaow2():
    print("Miaow ~~~")


if __name__ == "__main__":
    dog_bark2()
    # > Now use function 'dog_bark'
    # > Bark !!!

    cat_miaow2()
    # > Now use function 'cat_miaow'
    # > Bark !!!
