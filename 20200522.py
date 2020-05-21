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
#使用遞迴列印1~100
def countingnum(numb=0):
    print(numb)
    if numb==100:
        return 100

    else:
        return countingnum(numb+1)


#使用遞迴涵式製造費波納系數列
def recursor_test(numb):
    if numb==1 :
        return 1
    elif numb==0:
        return 0
    else:
        return recursor_test(numb-1)+recursor_test(numb-2)


    

countingnum()
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