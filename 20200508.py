a=2
b=3
print("a為",a,"b為",b)
c=a
a=b
b=c
print("a為",a,"b為",b)

###不使用額外記憶體 但使用額外計算

a=a+b
b=a-b
a=a-b
print("a為",a,"b為",b)
##python也支援多重賦值
a,b=b,a

##變數命名規則,盡量不要重複覆蓋預設變數名稱，會導致某些相互引用的部分出錯
# 1.不可使用數字當頭
# 2.不可使用字符串以外特殊符號%^#$!@/
# 3.底線符號為字符串

#ex1 jimmy_so_fat
#ex2 JimmySoFat

##幾種常見的資料型別，發生溢位時會有不可預期的錯誤
#int  整數型別 相當於數學的正整數
#float浮點數型別 相當於數學的小數，但是用1024去近似科學記號 64位元在小數點後17位失真
#int與float型別可使用eval()分別取得，兩者皆可使用數學運算子、關係以及邏輯運算子
#str 字串型別 相當於文字，使用單引號''或是雙引號""將文字夾住
#bool 布林值 Ture 與 False 兩種 分別對應到數學裡的真與假
#tuple() 元組型別，可放入多個資料，但不可更改
#list[]  串列(序列)型別，可放多入個資料，可更改
#set{}   集合型別，可放入多個以及多種型別資料，可修改 dict()對映型態(字典)屬於其中一種，分別為key以及value相互對應
# int1=2222+3333
# print("這次數字相加",int1)
# str1="2222"+"3333"
# print("這是字串相加",str1)

#數學運算子
#x+y 加法
#x-y 減法
#x*y 乘法
#x/y 除法
#x**y 次方 相當於pow(x,y)
#x//y 商數，極其重要
#x%y  餘數，極其重要
# result=10+6
# print("10+6",result)
# result=10-6
# print("10-6",result)
# result=10*6
# print("10*6",result)
# result=10/6
# print("10/6",result)
# result=10//6
# print("10//6",result)
# result=10%6
# print("10%6",result)

#邏輯運算子與關係運算子
#>  大於
#<  小於
#== 相當於數學中的等式
#>= 大於等於
#<= 小於等於
#!= 不等於
#and    兩者為真才為真
#or     兩者其一為真即為真
#not    反轉邏輯

#print(3>4)
#print(3>2 or 4>3)
#print(not(3>4))

#跳脫字元，特殊符號但是會被判斷為關鍵字時使用
#\' 單引號
#\""雙引號
#\n 換行
#\t tab
#\
#print('hello\nworld')

#位元運算子
#<<	向左位移	a << n
#>>	向右位移	a >> n
#&	位元且	a & b
#|	位元包含或	a | b
#^	位元互斥或	a ^ b
#~	位元相反	~a

#有條件執行if 判斷式
#if expression :  expression為布林值
#if a>0:
# print("a大於零")
#else :
# print("a小於零")
#迴圈:符合條件的重複執行
#while expression :
#迴圈:計次型的重複執行
#for A in B : B為可迭代物件
