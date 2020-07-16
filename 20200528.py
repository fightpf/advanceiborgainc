#物件導向設計
##在python 中 萬物皆為物件

#物件導向設計的好處在於，同一個模式，可以代入不同的東西，產生類似的效果
#舉例來說 胖 是一種屬性(attributes)，可以用來形容人，也可以形容貓、狗、動物但是不能用來形容書本
#但是人以及其他動物是屬於實體物件(instance)、人還有高、矮、帥、美等其他屬性，也可以執行其他方法(method，也就是python的def)例如，計算數學、拿起東西、起立、蹲下

#因此 我們可以建立的是一個物件(object)在python中使用類別(class)來宣告
#class就像一個模型，可以將壓入的黏土塑造成它的形狀，也可以視為設計圖以及產品
class math_test:
    def summation(self,*arg):
        result=0
        for i in range(len(arg)):
            result+=arg[i]
        return result
    def average(self,*arg):
        return self.summation(*arg)/len(arg)

#這是一個object，可以產生多的實體物件
a=math_test()
b=math_test()
print(id(a),id(b))
print(a.summation(1,2,3),b.summation(4,5,6))
#最重要的是，在物件中放入屬性(左右各兩個底線)
class math_test2():
    def __init__(self,number):   ##最重要的初始化屬性    
        super().__init__()##super是繼承父物件的方法
        self.number=number
    def summation(self):
        result=0
        for i in range(len(self.number)):
            result+=self.number[i]
        return result
    def average(self):
        return self.summation()/len(self.number)
#只加一個底線成為保護屬性，可取不可存 ex._name 可以列印、不能更改
#也可以只在屬性左邊加兩個底線，ex. __name  則該屬性不可外部存取 ex. 不可列印、不可更改

a=math_test2([1,2,3])
print(a.summation(),a.average())
#ex2.
class temptest2:
    def __init__(self): #def __init__(self,x,y):
        self.a=0        #self.a=x
        self.b=1        #self.b=y 
t2=temptest2()
print(t2.a)
print(t2.b)
class temptest3:
    def __init__(self,x,y): 
        self.a=x        
        self.b=y         
    def distance(self,point_x,point_y):
        return  ((self.a-point_x)**2+(self.b-point_y)**2)**0.5 
t3=temptest3(6,8)
answer=t3.distance(0,0)
print(answer)
#因此，當你在執行任一個python程式時，也會被存成一個物件，而這個物件的名字叫做main(主程式)
#以屬性印出就是__main__，則 if __name__=="__main__"代表，該段程式碼在該程式為主程式時才被執行，由外部呼叫為副程式時不執行
#------------------分隔線---------------------
#python強大的地方在於套件(module)的引用
#from 從..套件
#import 引入套件的某個...套件
#as  將套件存取為物件
#ex.產生一個亂數
import random as rd
print(rd.random())

#電腦是一個由人類規定好規則的東西，因此無法隨機生成一個數字，否則我們的數學函式怎麼能得到一樣的結果?
#因此randomg是在電腦中以一定的複雜函式產生一組隨機數字，而每一組隨機數字有自己的"亂數種"(seed)
#為了在不同電腦的到相同的模擬結果，我們可以規定相同的亂數種
#ex.
rd.seed(30)
print(rd.random())
##看看你的電腦否有一樣的結果 0.5390815646058106

#試著使用randrange
a=[]
for i in range(54):
    a.append(rd.randrange(1,54,1))
print(a)
a.sort()
print(a)
##試著使用random做蒙地卡羅模擬
#當模型有明確的邊界條件，或是機率模型時可適用
hit=0
trial=100000
for i in range(trial):
    x=rd.uniform(-1,1)
    y=rd.uniform(-1,1)
    if x**2+y**2<=1:
        hit+=1
    
ans=4*hit/trial
print(ans)

#請試著用random建立一個終極密碼的遊戲




##SQL套件
#---------------------
# import sqlite3

# conn = sqlite3.connect("myfirst.db")
# # sql = '''create table students(
# #         id int,
# #         name text,
# #         gender text)'''
# # conn.execute(sql)

# print('請輸入mysecond資料庫students表單資料')
# while True:
#     new_id = int(input("請輸入id  :"))
#     new_name = input("請輸入name : ")
#     new_gender = input("請輸入gender :")
#     x = (new_id, new_name, new_gender )
#     sql = '''insert into students values(?,?,?)'''
#     conn.execute(sql,x)
#     conn.commit()
#     again = input("繼續(y/n)?")
#     if again[0].lower()=="n":
#         break
# conn.close()

#----------------------------------
##三元運算子

a=3
b=a if a==3 else 2
print(b)


##lambda 表達式# 在lambda後先宣告會用到的變數，做為input，接著打冒號: 後方做為運算式output
#我們可以用一個簡單的lambda而不使用def製造一個函式
f = lambda x :x*x
print(f(5))

def max_temp(m,n):
    return m if m > n else n
#等價於
max_temp2= lambda m , n :m if m > n else n
##list comprehension
#list = [(expression) (for loop)* (if statment)*]

x = [i for i in range(10) if i % 2 ==0]
#等價於
x = []
for i in range(10):
    if i % 2 == 0:
        x.append(i)



