#氣泡排序法 bubble sort
a=[0,7,1,5,4,9]#element
  #0,1,2,3,4,5 index
lena=len(a)                         #len()將a取出其長度，這裡為6
for j in range(lena-1):
    for i in range(lena-j-1):       #因為經過j次交換後，最右邊已是最大值，只需交換lena-j-1次  
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]  
print(a)
#時間複雜度
#O(n2)


##列印99乘法表
#思維:第一個column的i不變j變
#問題點:注意列印的內容資料型別為變數還是字串，如果不同 可以先將其整理完再列印，也可以將其分別印出
for i in range(1,10):               #注意，range()包含下界不包含上界!!
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
#最後，注意print()這個function，它會強制在最後列印\n跳行符號，因此可以透過print(end="")，將其化為空格或tab
#接著在j列印完後，在印製一個跳行符號
for i in range(1,10):               #注意，range()包含下界不包含上界!!
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end=" ")
    print("\n")


#for 迴圈可以接受任何可迭代物件 註:只要是有像是list的index順序皆可成為可迭代物件
##使用字串當作for迴圈物件
s="i love python"
for i in s :
    print(i)
##使用list當作for迴圈物件
s=[0,7,1,5,4,9]
for i in s:
    print(i)

#利用檔案作為for迴圈物件，先建立一個測試檔 註:讀檔寫檔有很多方法，這邊使用內建的open()函數  
fopen=open("samplefile",mode='w')
#將其各行逐一寫入一個數字
for i in range(10):
    fopen.write(str(i)+'\n')
#關閉檔案，這時資料夾內會多一個samplefile文字檔
fopen.close
#再次開啟檔案
fopen=open("samplefile")
for i in fopen:
    print(i)
fopen.close

#迴圈控制
##continue 直接進入迴圈下一個round
##break    強制結束迴圈
##pass     不執行動作，通常是為了搭配語法
n=0
#while True 為無窮迴圈
while True:
    n+=1
    if n==10:
        break
    if n==5:
        continue
    print(n)

#def :陳述句
#建立一個功能，將其包裝成一個函式
#i.e將氣泡排序法建立一個函式
#注意!以下5點
#1.不可與變數、函式重複名稱，否則直接覆蓋
#2.def中變數皆為區域(local)變數，若要在該巢狀結構外使用該變數名稱則使用global宣告(強烈不建議使用) 
#3.如果只是要執行功能，不需要回傳值return
#4.print()即可直接列印
#5.def 至於程式碼前後皆可

#注意 如果為不定長度 需要在前方加一個米字號將其轉為類似指標物件傳入，通常使用*arg
#若在函式定義時宣告，該宣告將做為預設值

def bubble_sort(a=[0,7,1,5,4,9]):
    lena=len(a)                         #len()將a取出其長度，這裡為6
    for j in range(lena-1):
        for i in range(lena-j-1):       #因為經過j次交換後，最右邊已是最大值，只需交換lena-j-1次  
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i] 
    return a
this_is_sample_for_def=[0,7,1,5,4,9]
result=bubble_sort(this_is_sample_for_def)
print(result)