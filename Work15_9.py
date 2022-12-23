# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:18:54 2022

@author: iammu
"""


def multipleSanads(txt):
    WordReplace=["حدثني","وحدثنا","حدثنا","نحوه","عن","قال،","فقال","سمعت","يقول","أنه","سمع","أخبرني","أن","أخبرنا","أنه","اخبرنا","سال","وقال","قالت","قالا","جميعا","قلت","أنها","وحدثني","في حديثه","يخطب","أخبره","تابعه","إنه","انه","كثيرا","قال:","قال","أنبأنا","إذا","أحدثكم","قام","فكتب","حديث","حديثه","أخبرهم","وكانت","يحدث","يخبر","فقلت","حدث","وكان","يخبر","لحديث","حدثها","حدثتنيه","ثقة","عقلت","أخبروني","حدث","وقد","روى","صحبت","حدثناه","سألت","هرقل","لي","هذا","الحديث","وأنبأنا","حدثكم","من","ولقد","وعن","شهدت","كتب","زوج","يذكر","سألني","قالوا","إلى","فكان","لما","قدم","أشياء","رواية","رأيت","أقبلت","قراءة","وأنا","أسمع","إن","حدثه","بهذا","حديثا","بأى","اخبرني","كان",'كنت',"يحدثونه","حدثتني","شىء","وغير","واحد","أسمع","وأخبرني"]
    WithoutAhrabTxt=""
    for  i in range(len(txt)):
        no=ord(txt[i])
        if(no==1614 or no==1615 or no==1616 or no==1618 or no==1617 or no==1612 or no==1613 or no==1611):
            continue
        else:
            WithoutAhrabTxt+=txt[i]
            
    # print(WithoutAhrabTxt)
    
    sanadList =[]
    txtList = []
    # txtList=WithoutAhrabTxt.split(" ")
    if(WithoutAhrabTxt.__contains__("ح‏.")):
        txtList=WithoutAhrabTxt.split("ح‏.")
    elif(WithoutAhrabTxt.__contains__(" ح، ")):
        txtList=WithoutAhrabTxt.split(" ح، ")
    elif(WithoutAhrabTxt.__contains__(" ح. ")):
        txtList=WithoutAhrabTxt.split(" ح. ")
    else:
        txtList=WithoutAhrabTxt.split(" ح ") 
    for sanad in range(len(txtList)):
        # Extract all words from hadithText Like "حدثني","وحدثنا","حدثنا"
        wordReplaceList_givenHadith = []

        # Extract all Narrator's Names from given hadith
        narratorsNameList = []

        # Variable for extracting WordReplace's element from hadithText  Like "حدثني","وحدثنا","حدثنا"
        get_WordReplace_Element = ""
        # Variable for extracting Name of Narrator from hadithText and at the end Matn of hadith
        narratorName = ""
        
        tokens_WithoutAerabText = txtList[sanad].split()
        for i in range(len(tokens_WithoutAerabText)):

            if (tokens_WithoutAerabText[i] in WordReplace) == True:
                get_WordReplace_Element += (tokens_WithoutAerabText[i] + " ")
                if (narratorName != ""):
                    narratorsNameList.append(narratorName)
                    narratorName = ""
            if (tokens_WithoutAerabText[i] in WordReplace) == False:
                narratorName += (tokens_WithoutAerabText[i] + " ")
                if (get_WordReplace_Element != ""):
                    wordReplaceList_givenHadith.append(get_WordReplace_Element)
                    get_WordReplace_Element = ""
        if(narratorName!="" and tokens_WithoutAerabText[i]):
            narratorsNameList.append(narratorName)
        sanadList.append(narratorsNameList)

    # # List of Prophet's صلی اللہ علیہ وآلہ وسلم name that are used in Ahadith
    prophetNamesReplacerList = ["رسول الله صلى الله عليه وسلم","النبي ـ صلى الله عليه وسلم" ,"النبي صلى الله عليه وسلم", "يا رسول الله","رسول الله","النبي ‌صلی ‌اللہ ‌علیہ ‌وآلہ ‌وسلم","صلى الله عليه وسلم","للنبي صلی اللہ علیہ وسلم","محمد صلی اللہ علیہ وآلہ وسلم"]

    for i in range(len(sanadList)):
        dum=[]
        for j in range(len(sanadList[i])):
            for name in range(len(prophetNamesReplacerList)):
                if(sanadList[i][j].__contains__(prophetNamesReplacerList[name])):
                    sanadList[i][j] = "محمد صلی اللہ علیہ وآلہ وسلم"
                    break
                
            if(sanadList[i][j].__contains__("محمد صلی اللہ علیہ وآلہ وسلم")):
                 dum.append(sanadList[i][j])
                 break
            else:
                 dum.append(sanadList[i][j])
        sanadList[i]=dum
    # print(sanadList)
    
    for i in range(len(sanadList)):
        for j in range(len(sanadList[i])):
            sanadList[i][j] = sanadList[i][j].strip()
            if (len(sanadList[i][j]) != 0):
                sanadList[i][j] = sanadList[i][j].replace('''"''', '')
                sanadList[i][j] = sanadList[i][j].replace("ـ رضى الله عنها ـ", "")
                sanadList[i][j] = sanadList[i][j].replace("رضى الله عنه", "")
                sanadList[i][j] = sanadList[i][j].replace("- رضى الله عنه -", "")
                sanadList[i][j] = sanadList[i][j].replace("رضى الله عنهما ", "")
                sanadList[i][j] = sanadList[i][j].replace("رضى الله عنها", "")
                sanadList[i][j] = sanadList[i][j].replace("رضى الله عنه", "")   
                sanadList[i][j] = sanadList[i][j].replace("رضى الله عنه -", "")
                sanadList[i][j] = sanadList[i][j].replace("رضى الله تعالى عنه", "")
                sanadList[i][j] = sanadList[i][j].replace("ـ رضي الله عنها ـ", "")
                sanadList[i][j] = sanadList[i][j].replace("رضي الله عنهما ", "")
                sanadList[i][j] = sanadList[i][j].replace("رضي الله عنهما", "")
                sanadList[i][j] = sanadList[i][j].replace("رضي الله عنها", "")
                sanadList[i][j] = sanadList[i][j].replace("رضي الله عنه", "")
                sanadList[i][j] = sanadList[i][j].replace("- رضي الله عنه -", "")
                sanadList[i][j] = sanadList[i][j].replace("رضي الله عنه", "")
                sanadList[i][j] = sanadList[i][j].replace("رضي الله عنه -", "")
                sanadList[i][j] = sanadList[i][j].replace("رضي الله تعالى عنه", "")
                sanadList[i][j] = sanadList[i][j].replace("على المنبر", "")
                sanadList[i][j] = sanadList[i][j].replace("-","")
                sanadList[i][j] = sanadList[i][j].replace("ـ","")
                sanadList[i][j] = sanadList[i][j].replace("،","")        
                sanadList[i][j] = sanadList[i][j].strip()
                
        while("" in sanadList[i]) :
            sanadList[i].remove("")
            
            
    return sanadList
# _____________________________________________________________________

def singleSanad(HadithText):
    hadithText = HadithText.strip()

    # Variable that contains without_Aeraab hadithText
    withoutAerabText = ""

    # Aeraab Remover Code
    for i in range(len(hadithText)):
        no = ord(hadithText[i])
        if (no == 1614 or no == 1615 or no == 1616 or no == 1618 or no == 1617 or no == 1612 or no == 1613 or no == 1611):
            continue
        else:
            withoutAerabText += hadithText[i]
            
    tokens_WithoutAerabText = withoutAerabText.split(" ")
 
    # Words that replace from hadithText  
    WordReplace=["حدثني","وحدثنا","حدثنا","نحوه","عن","قال","فقال","سمعت","يقول","أنه","سمع","أخبرني","أن","أخبرنا","اخبرنا","حدث","أنه","سال","قالت","قالا","جميعا","قلت","أنها","وحدثني","أخبره","في حديثه","يخطب","تابعه","إنه","انه","كثيرا","قال:","أنبأنا","أحدثكم","إذا","قام","فكتب","يحدث","فقلت","قالوا","حديثه","يخبر","أخبرهم","وكانت","حديث","وقد","عقلت","وكان","لحديث","ثقة","حدثتنيه","حدثها","يخبر","أخبروني","وقال","حدث","روى","هذا","سألت","حدثناه","هرقل","لي","صحبت","الحديث","حدثكم","وأنبأنا","من","كتب","شهدت","وعن","زوج","ولقد","يذكر","سألني","فكان","إلى","لما","قدم","أشياء","بهذا","رأيت","أقبلت","رواية","قال،","قراءة","وأنا","إن","أسمع","حدثه","بأى","حديثا","كان",'كنت',"اخبرني","يحدثونه","حدثتني","شىء","أسمع","وغير","واحد","وأخبرني"]



    # Extract all words from hadithText Like "حدثني","وحدثنا","حدثنا"
    wordReplaceList_givenHadith = []

    # Extract all Narrator's Names from given hadith
    narratorsNameList = []

    # Variable for extracting WordReplace's element from hadithText  Like "حدثني","وحدثنا","حدثنا"
    get_WordReplace_Element = ""

    # Variable for extracting Name of Narrator from hadithText and at the end Matn of hadith
    narratorName = ""

    for i in range(len(tokens_WithoutAerabText)):

        if (tokens_WithoutAerabText[i] in WordReplace) == True:
            get_WordReplace_Element += (tokens_WithoutAerabText[i] + " ")
            if (narratorName != ""):
                narratorsNameList.append(narratorName)
                narratorName = ""
        if (tokens_WithoutAerabText[i] in WordReplace) == False:
            narratorName += (tokens_WithoutAerabText[i] + " ")
            if (get_WordReplace_Element != ""):
                wordReplaceList_givenHadith.append(get_WordReplace_Element)
                get_WordReplace_Element = ""


    # List of Prophet's صلی اللہ علیہ وآلہ وسلم name that are used in Ahadith
    prophetNamesReplacerList = ["رسول الله صلى الله عليه وسلم","النبي ـ صلى الله عليه وسلم" ,"النبي صلى الله عليه وسلم","النبي ‌صلی ‌اللہ ‌علیہ ‌وآلہ ‌وسلم","رسول الله","للنبي صلی اللہ علیہ وسلم","صلى الله عليه وسلم", "يا رسول الله",
                                        "محمد صلی اللہ علیہ وآلہ وسلم"]


    # Script for Qauli and Faeli Hadith in which Prophet's(صلی اللہ علیہ وآلہ وسلم) name used in Matn only
    for i in range(len(prophetNamesReplacerList)):
        if (prophetNamesReplacerList[i] not in narratorsNameList and narratorName.__contains__(prophetNamesReplacerList[i])):
            narratorsNameList.append("محمد صلی اللہ علیہ وآلہ وسلم")

    # Script also used for same work as mentioned in above comment
    for i in range(len(narratorsNameList)):
        for j in range(len(prophetNamesReplacerList)):
            if (narratorsNameList[i].__contains__(prophetNamesReplacerList[j]) and narratorsNameList[i] !=prophetNamesReplacerList[j]):
                narratorsNameList[i] = "محمد صلی اللہ علیہ وآلہ وسلم"

    for i in range(len(prophetNamesReplacerList)):
        if(withoutAerabText.__contains__(prophetNamesReplacerList[i])):
            narratorsNameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
    # Removing duplicate values
    narratorsNameList = list(dict.fromkeys(narratorsNameList))


    #   ****************New Search Algorithm asked by Sir****************

    # narratorsNameList[0] = "الحميدي عبد الله بن أبي الزبير"
    # Filtering Names of narrators
    for i in range(len(narratorsNameList)):
        narratorsNameList[i] = narratorsNameList[i].strip()
        if (len(narratorsNameList[i]) != 0):
            if (narratorsNameList[i][-1] == "،"):
                narratorsNameList[i] = narratorsNameList[i].replace("،", "")
     
        narratorsNameList[i] = narratorsNameList[i].replace('''"''', '')
        narratorsNameList[i] = narratorsNameList[i].replace("ـ رضى الله عنها ـ", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضى الله عنهما ", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضى الله عنهما", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضى الله عنها", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضى الله عنه", "")
        narratorsNameList[i] = narratorsNameList[i].replace("- رضى الله عنه -", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضى الله عنه", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضى الله عنه -", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضى الله تعالى عنه", "")
        
        narratorsNameList[i] = narratorsNameList[i].replace("ـ رضي الله عنها ـ", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنهما ", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنهما", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنها", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنه", "")
        narratorsNameList[i] = narratorsNameList[i].replace("- رضي الله عنه -", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنه", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنه -", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله تعالى عنه", "")
        
        narratorsNameList[i] = narratorsNameList[i].replace("على المنبر", "")
        narratorsNameList[i] = narratorsNameList[i].replace("المنبر", "")
        narratorsNameList[i] = narratorsNameList[i].replace("-","")
        narratorsNameList[i] = narratorsNameList[i].replace("ـ","")
        narratorsNameList[i] = narratorsNameList[i].replace("،","")        
        narratorsNameList[i] = narratorsNameList[i].strip()

    
    while("" in narratorsNameList) :
        narratorsNameList.remove("")
        
    #agr remove comma here than malik will be name 
    narratorsNameList =[name.replace("،","") for name in narratorsNameList]
    
    FinalList=[]
    for i in range(len(narratorsNameList)):
        if(narratorsNameList[i] == "محمد صلی اللہ علیہ وآلہ وسلم"):
            FinalList.append(narratorsNameList[i])
            break
        else:
            FinalList.append(narratorsNameList[i])
    
    return FinalList
    
    
    # return narratorsNameList




#_______________Main Code___________

finalNarratorsNameList=[]


import pandas as pd 
# df = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/SahihAhadith2400.xlsx")


df2 = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/Testing600Hadith.xlsx")


df2 = df2.dropna()
hadithList = df2.isnad

for i in hadithList:
    
    if(i.__contains__(" ح ") or i.__contains__(" ح، ") or i.__contains__("ح‏.") or i.__contains__(" ح. ")):
        return_M_List= multipleSanads(i)
        finalNarratorsNameList.append(return_M_List)
    else:
        return_S_List = singleSanad(i)
        finalNarratorsNameList.append(return_S_List)

# fullIsnad = list(df.isnad)+list(df2.isnad)
# fullStatus = list(df.status)+list(df2.status)

#Data frame for list of names after rules based name extract

# df3 = pd.DataFrame()
# df3['isnad'] =fullIsnad
# df3['status'] = fullStatus
# df3['NarratorListAfterRuleBased'] = finalNarratorsNameList
# df3.to_excel("C:/Users/iammu/OneDrive/Desktop/AfterRuleBasedFullHadith.xlsx")      
# ###########################################

from camel_tools.ner import NERecognizer
from camel_tools.tokenizers.word import simple_word_tokenize
ner = NERecognizer('CAMeL-Lab/bert-base-arabic-camelbert-msa-ner')


import mysql.connector
myDb = mysql.connector.connect(host='localhost',user='root',passwd='fb834946220403',database='scholar_database')
myCursor = myDb.cursor()

#Get names from Scholars table
query='''select name from scholars;'''
myCursor.execute(query)
result = myCursor.fetchall()

#get Name from Scholar Other Names table
query='''select name from scholar_other_names;'''
myCursor.execute(query)
result2 = myCursor.fetchall()

# #convert tuple into String
for i in range(len(result)):
    result[i] = result[i][0]    

# result.append("أبي")
# result.append("أبيه")
# # 



# d="رضي الله تعالى عنهما"
# print(d.replace("رضي الله تعالى عنهما","hh"))

# dum = 'العمري'
# dum [0:2]

for i in range(len(finalNarratorsNameList)):
    if(len(finalNarratorsNameList[i])==0):
        print(i)



finalMatchList=[]
for i in range(len(finalNarratorsNameList)):
    if(len(finalNarratorsNameList[i])==0):
        continue
    index = finalNarratorsNameList[i][0]
    #print(finalNarratorsNameList[i],end="\n"
    matchList=[]
    if(type(index)==str):
        for j in range(len(finalNarratorsNameList[i])):
            if(finalNarratorsNameList[i][j] in result) or (finalNarratorsNameList[i][j] in result2):
                matchList.append(finalNarratorsNameList[i][j])
                continue
            elif(finalNarratorsNameList[i][j][0:1] == 'ل'):
                d = finalNarratorsNameList[i][j][1:]
                if(d in result) or (d in result2):
                    matchList.append(d)
                    continue
            elif(finalNarratorsNameList[i][j][0:2] == 'ال'):
                d = finalNarratorsNameList[i][j][2:]
                if(d in result) or (d in result2):
                    matchList.append(d)
                    continue
            elif(finalNarratorsNameList[i][j].__contains__("و")):
                dum = finalNarratorsNameList[i][j].split("و")
                for du in dum:
                    if(du in result) or (du in result2):
                        matchList.append(du)
                        continue
            else:
                sentence = simple_word_tokenize(finalNarratorsNameList[i][j])
                dummy = ner.predict_sentence(sentence)
                name = ""
                pre_end = 0
                for jj in range(len(dummy)):
                    if(dummy[jj]=="B-PERS" or dummy[jj]=="I-PERS"):
                        name =name + sentence[jj]+' '
                        
                print(name)
                if(name in result) or (name in result2): 
                    matchList.append(name.strip())
                    continue
            
        finalMatchList.append(matchList)
        print(finalMatchList)
    else:
        singleMatchList=[]
        for j in range(len(finalNarratorsNameList[i])):
            matchList=[]
            for k in range(len(finalNarratorsNameList[i][j])):
                if(finalNarratorsNameList[i][j][k] in result) or (finalNarratorsNameList[i][j][k] in result2):
                    matchList.append(finalNarratorsNameList[i][j][k])
                    continue
                elif(finalNarratorsNameList[i][j][k][0:1] == 'ل'):
                    d = finalNarratorsNameList[i][j][k][1:]
                    if(d in result) or (d in result2):
                        matchList.append(d)
                        continue
                elif(finalNarratorsNameList[i][j][k][0:2] == 'ال'):
                    d = finalNarratorsNameList[i][j][k][2:]
                    if(d in result) or (d in result2):
                        matchList.append(d)
                        continue
                elif(finalNarratorsNameList[i][j][k].__contains__("و")):
                    dum = finalNarratorsNameList[i][j][k].split("و")
                    for du in dum:
                        if(du in result) or (du in result2):
                            matchList.append(du)
                            continue
                else:
                    sentence = simple_word_tokenize(finalNarratorsNameList[i][j][k])
                    dummy = ner.predict_sentence(sentence)
                    name = ""
                    pre_end = 0
                    for jj in range(len(dummy)):
                        if(dummy[jj]=="B-PERS" or dummy[jj]=="I-PERS"):
                            name =name + sentence[jj]+' '
                            
                    print(name)
                    if(name in result) or (name in result2): 
                        matchList.append(name.strip())
                        continue
                
            singleMatchList.append(matchList)
        finalMatchList.append(singleMatchList)





#Create File of Isnad, Status And Match Name List
        
FinalIsnad_test=[]
FinalStatus_test=[]
indexx=[48,384]
for i in range(len(finalNarratorsNameList)):
    if(i in indexx):
        continue
    else:
        FinalIsnad_test.append(finalNarratorsNameList[i])
        FinalStatus_test.append(dfTest.status[i])
            
dfTestMatchList = pd.DataFrame()
dfTestMatchList['Isnad']=FinalIsnad_test 
dfTestMatchList['Status']=FinalStatus_test  
dfTestMatchList['MatchName']=finalMatchList  

dfTestMatchList.to_excel("C:/Users/iammu/OneDrive/Desktop/600MatchNameWithDataBase.xlsx")

     
    
## remove Duplicate    
# notMatchList = list(dict.fromkeys(notMatchList))

