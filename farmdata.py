import urllib
import  gzip
import json
import urllib.request
url='https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'
with urllib.request.urlopen(url) as response:
    jdata=response.read()
    data1=json.loads(jdata)
    data=sorted(data1,key=lambda k:k["作物名稱"])
    for i in range(0,(len(data)),1):
        s1=data[i]["交易日期"]
        s2=data[i]["作物名稱"]
        s3=data[i]["市場名稱"]
        s4=data[i]["平均價"]
        s5=data[i]["交易量"]
        print(s1+" "+s2+" "+s3+"  平均價"+str(s4)+" "+str(s5))
