# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 09:48:58 2022

@author: iammu
"""
import pandas as pd
# import mysql.connector



# myDb=mysql.connector.connect(host="localhost",user="root",passwd="fb834946220403",database="scholar_database")
# myCursor=myDb.cursor()

# query='''select id,name from scholars ;'''
# myCursor.execute(query)
# result=myCursor.fetchall()

# for i in range(len(result)):
#     if(i==15):
#         break
#     else:
#         print(result[i])
#         print("\n"+result[i][1])
                
data=pd.read_excel("C:/Users/iammu/OneDrive/Desktop/distinctAreaOfIntrest.xlsx")
Statuslist=list(data.area_of_intrest)
gradeList=[]


for i in range(len(Statuslist)):
    count=0;
    if(type(Statuslist))==float:
        gradeList.append(" ")
    if(str(Statuslist[i]).__contains__("Narrator"))==False:
        gradeList.append(" ")
        
    if(str(Statuslist[i]).__contains__("Narrator")):
        splitList=Statuslist[i].split(",")
        for j in range(len(splitList)):
            dum=splitList[j].strip()
            if(dum[0:8].strip()=="Narrator"):
                gradeList.append(splitList[j])
                break
            
#_Testing_
areaOfIntrest=list(data.area_of_intrest)

gradesWord=['صحبة','ثقة','لا بأس به','ثقة حافظ','صدوق','ثقة ثبت','صدوق يخطئ','مقبول','الحافظ','لين الحديث','صدوق له أوهام','صدوق يخطئ','صحابي','صحابة', 'أوثق الناس','مخضرم','تمييز','ليس به بأس','ضعيف','مستور', 'مجهول الحال','كذب','مجهول','منكر الحديث','متروك','تهم بالكذب']


refinedGrade=[]

    
    
length=[]
# for i in range(len(gradeList)):
#     x=gradeList[i].split("[")
#     length.append(len(x))
#     if(len(x)==0 or len(x)==1):
#         refinedGrade.append(" ")
#     if(len(x)==2 or len(x)==3 or len(x)==4 or len(x)==5):
#         refinedGrade.append(x[1])
refineList=[]   
for i in range(len(refinedGrade)):
    if(len(refinedGrade[i])!=0):
        if(refinedGrade[i][-1]=="]"):
            refineList.append(refinedGrade[i][:-1].strip())
        else:
            refineList.append(refinedGrade[i])
    else:
        refineList.append(refinedGrade[i])
    
    
for i in range(len(refineList)):
    x=refineList[i].strip()
    refinedGrade.append(x)


dumList=[]
for i in range(len(refineList)):
    count=0
    if(refineList[i].__contains__("-") and refineList[i][0]!="G"):
        y=refineList[i].split("-")
        for j in range(len(y)):
            
            if(y[j].strip() in gradesWord):
                dumList.append(y[j].strip())
                break
            else:
                count+=1
                if(count==len(y)):
                    dumList.append("Narrator")
                    
    else:
        
        dumList.append(refineList[i].strip())   
    
count=0  
for i in range(len(dumList)):
    if(refineList[i]==""):
        dumList[i]=(refineList[i])
        count+=1


zaeefKeywords=['Grade:Weak','Grade:Not Thiqah','Grade:Liar','Grade:Abandoned','Grade:Unknown-Majhool','Grade:Undefined','ضعيف','مستور',' مجهول الحال','كذب','مجهول','منكر الحديث','متروك','تهم بالكذب']
sahihKeywords=['Grade:Thiqah Thiqah','Grade:Sadooq','Grade:Thiqah',"Grade:Accused Liar",'Grade:Maqbool','Grade:Sadooq/Delusion','Grade:No Doubt','صحبة','ثقة','لا بأس به', 'ثقة حافظ', 'صدوق', 'ثقة ثبت','صدوق يخطئ','مقبول','الحافظ','لين الحديث','صدوق له أوهام','صدوق يخطئ','صحابي','صحابة', 'أوثق الناس','مخضرم','تمييز', 'ليس به بأس']
narratorStatusList=[]

for i in range(len(dumList)):
    if(dumList[i] in sahihKeywords):
        narratorStatusList.append("Sahih")
    elif(dumList[i] in zaeefKeywords):
        narratorStatusList.append("Zaeef")
        #count+=1
    elif(dumList[i]=="" or dumList[i]=="Narrator"):
        narratorStatusList.append("")
        #count+=1
    else:
        narratorStatusList.append(dumList[i])
        count+=1
        print(dumList[i], end="\t")
        
for i in range(len(narratorStatusList)):
    if(narratorStatusList[i]==""):
        count+=1
        
data=pd.DataFrame()
data["Status"]=narratorStatusList        

data.to_excel("NarratorStatusList.xlsx")
