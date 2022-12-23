# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 00:06:33 2022

@author: iammu
"""

import pandas as pd

# data = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/Data/Taqreeb ul Thazeeb.xlsx")
data=pd.read_excel("C:/Users/iammu/OneDrive/Desktop/Book_96955.xlsx")
ab=str(data.book96955[0])
for i in range(len(data)):
        ab=ab+"\n"+str(data.book96955[i])

file=open("C:/Users/iammu/OneDrive/Desktop/Deewan_ul_Zuhafa.txt","w",encoding='utf-8')
file.write(ab)
file.close()
indexList=[]
dataList=[]


#tabqa=["العاشرة","الحادية عشرة","","التاسعة","كبار العاشرة","الثانية عشرة"]

ListScrap=list(data["Data"])
dum=ListScrap[761]
index = dum.find('-') 
print(dum[0:index].strip())
print(dum[index+1:-1].strip())



#__________________________Seprate the index and text from each other________________

for i in range(len(ListScrap)):
    dum=ListScrap[i]
    index =dum.find('-') 
   # print(ListScrap[i])
    if(index==int(-1)):
        indexList.append("nan")
        dataList.append(ListScrap[i])
    else:
        
        indexList.append(dum[0:index].strip())
        dataList.append(dum[index+1:])



#______Adding these List into Data Frame_______

data["IndexNumber"]=indexList
data["Data"]=dataList





newList=[]
for i in range(len(ListScrap)):
        dumList=ListScrap[i].split(" ")
        if(dumList[0]=="[]" or dumList[0].__contains__("-")):
            newList.append(ListScrap[i])
        else:
            newList.append("nan")
            
        
#data['IndexData']=newList   


data.to_excel("TaqreebUlThzeeb_Status.xlsx")


#____________Extracting jhara o tadheeel
# word2=["صحيح وخلط","متروك الحديث","لا يعرف","فيه ضعف","ليس بالقوي","مجهول الحال","لين الحديث","صدوق تغير بآخرة","صدوق له أوهام","صدوق يهم","ليس به بأس","لا بأس به"]
# word=["الصحابة" ,"ثقة","ثبت","حافظ","متقن","حجة","ثبت","عدل","صدوق","البدعة","مقبول","بالبدعة","مستور","ضعيف","مجهول","الحافظ","ساقط","الكذب","منكرالحديث","كذاب"]


word=["لا","ليس","به","بأس","متروك","الصحابة","صحابي" ,"ثقة","ثبت","حافظ","متقن","ثبت","عدل","صدوق","البدعة","مقبول","بالبدعة","مستور","ضعيف","مجهول","الحافظ","ساقط","الكذب","منكرالحديث","تغير","الحديث","ضعف","يعرف","صحيح","وخلط","فيه","لين","بالقوي","الحال","بآخرة","له","أوهام","يهم","كذاب"]


adlat=[]
for i in range(len(data.Data)): 
    prev=""
    if(type(data.Data[i])!=float):
        dum=(data.Data[i].strip()).split(" ")
        flag=False
        print(i)
        print(dum)
        for j in range(len(word)):
            if(word[j] in dum):
                if(flag==False):
                    flag=True
                    prev=word[j]
                    print(prev)
                    # for k in range(len(dum)):
                    #     if(dum[k]==prev):
                            
                else:
                        prev=prev+" "+str(word[j])
                        print(prev)
        adlat.append(prev)
                    
    else:
        adlat.append("")
        
        
data["Status"]=adlat 
            





