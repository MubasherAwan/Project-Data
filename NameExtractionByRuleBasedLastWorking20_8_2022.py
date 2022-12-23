# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:43:18 2022

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
# for i in range(len(result2)):
#     result2[i] = result2[i][0]    

# result.append("أبي")
# result.append("أبيه")
# 



# d="رضي الله تعالى عنهما"
# print(d.replace("رضي الله تعالى عنهما","hh"))

# dum = 'العمري'
# dum [0:2]


notMatchList=[]
matchList=[]
match=0
noMatch = 0
for i in range(len(finalNarratorsNameList)):
    nameList = finalNarratorsNameList[i]
    print(i)
    if(len(nameList)==0):
        continue
    if(type(nameList[0])==str):
        for name in range(len(nameList)): 
            if(nameList[name] in result):
                match= match +1
                matchList.append(nameList[name])
                continue
            elif(nameList[name] in result2):
                 match= match +1
                 matchList.append(nameList[name])
                 continue
            elif(nameList[name][0:1] == 'ل'):
                d = nameList[name][1:]
                if(d in result) or (d in result2):
                    match = match + 1
                    matchList.append(d)
                    continue
                else:
                    noMatch = noMatch + 1
                    notMatchList.append(nameList[name])
                    continue
            elif(nameList[name][0:2] == 'ال'):
                d = nameList[name][2:]
                if(d in result) or (d in result2):
                    match = match + 1
                    matchList.append(d)
                    continue
                else:
                    noMatch = noMatch + 1
                    notMatchList.append(nameList[name])
                    continue
                    
                
            elif(nameList[name].__contains__("و")):
                dum = nameList[name].split("و")
                for j in dum:
                    if(j in result):
                        match= match +1
                        matchList.append(j)
                        continue
                    elif(j in result2):
                        match= match +1
                        matchList.append(j)
                        continue
                    else:
                        noMatch = noMatch + 1
                        notMatchList.append(j)
                        continue
            else:
                noMatch = noMatch + 1
                notMatchList.append(nameList[name])
                print(nameList[name])
                continue
                
    else:
        for row in range(len(nameList)):
            for col in range(len(nameList[row])):
                if(nameList[row][col] in result):
                    match= match +1
                    matchList.append(nameList[row][col])
                    continue
                elif(nameList[row][col] in result2):
                    match= match +1
                    matchList.append(nameList[row][col])
                    continue
                elif(nameList[row][col][0:1] == 'ل'):
                    d = nameList[row][col][1:]
                    if(d in result) or (d in result2):
                        match = match + 1
                        matchList.append(d)
                        continue
                    else:
                        noMatch = noMatch + 1
                        notMatchList.append(nameList[row][col])
                        continue
                elif(nameList[row][col][0:2] == 'ال'):
                    d = nameList[row][col][2:]
                    if(d in result) or (d in result2):
                        match = match + 1
                        matchList.append(d)
                        continue
                    else:
                        noMatch = noMatch + 1
                        notMatchList.append(nameList[row][col])
                        continue
                elif(nameList[row][col].__contains__("و")):
                    dum = nameList[row][col].split("و")
                    for j in dum:
                        if(j in result):
                            match= match +1
                            matchList.append(j)
                            continue
                        elif(j in result2):
                            match= match +1
                            matchList.append(j)
                            continue
                        else:
                            noMatch = noMatch + 1
                            notMatchList.append(j)
                            continue
                else:
                    noMatch = noMatch + 1
                    notMatchList.append(nameList[row][col])
                    continue
                    
    
## remove Duplicate    
# matchList = list(dict.fromkeys(matchList))



dfNot = pd.DataFrame()
dfNot['notMatch'] = notMatchList

dfNot.to_excel("C:/Users/iammu/OneDrive/Desktop/NotMatchAfterRuleBased.xlsx")










































































List=[]

from camel_tools.ner import NERecognizer
from camel_tools.tokenizers.word import simple_word_tokenize
ner = NERecognizer('CAMeL-Lab/bert-base-arabic-camelbert-msa-ner')

for i in notMatchList:
    i = i.strip()
    if(len(i)==0 or len(i)==1 or len(i)==2):
        continue
    else:    
        sentence = simple_word_tokenize(i)
        dummy = ner.predict_sentence(sentence)
    
        
    
        name = ""
        pre_end = 0
        for j in range(len(dummy)):
            if(dummy[j]=="B-PERS" or dummy[j]=="I-PERS"):
                name =name + sentence[j]+' '
        print(name)           
        List.append(name.strip())
        name = ""



# #remove empty index from List
List = [i for i in List if i]

for i in range(len(List)):
    nameList =List[i]
    print(i)
        
    if(nameList in result):
        match= match +1
        matchList.append(nameList)
        continue
    elif(nameList in result2):
         match= match +1
         matchList.append(nameList)
         continue
    elif(nameList[0:1] == 'ل'):
        d = nameList[1:]
        if(d in result) or (d in result2):
            match = match + 1
            matchList.append(d)
            continue
        else:
            noMatch = noMatch + 1
            notMatchList.append(nameList)
            continue
    elif(nameList[0:2] == 'ال'):
        d = nameList[2:]
        if(d in result) or (d in result2):
            match = match + 1
            matchList.append(d)
            continue
        else:
            noMatch = noMatch + 1
            notMatchList.append(nameList)
            continue
            
        
    elif(nameList.__contains__("و")):
        dum = nameList.split("و")
        for j in dum:
            if(j in result):
                match= match +1
                matchList.append(j)
                continue
            elif(j in result2):
                match= match +1
                matchList.append(j)
                continue
            else:
                noMatch = noMatch + 1
                notMatchList.append(j)
                continue
    else:
        noMatch = noMatch + 1
        notMatchList.append(nameList)
        print(nameList)
        continue
        








dfMatch = pd.DataFrame()
dfMatch["Match_Name"]= matchList


dfMatch.to_excel("C:/Users/iammu/OneDrive/Desktop/MatchNameFromAllTrainTestHadith.xlsx")





# df["RuleBasedNames"] = finalNarratorsNameList

# df.to_excel("C:/Users/iammu/OneDrive/Desktop/comparison/Overall Comparison (error in rule-based)/ExactAndRuleBasedNames.xlsx")
##################### Removing extra spaces from HadithText column and store it in a new File ####################


# df1 = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/comparison/Overall Comparison (error in rule-based)/exact_NewNER_RuleBased_andOldNERNamesFrom480Hadith.xlsx")

# hadithNumber = list(df1["HadithNumber"])

# hadithText = list(df1["HadithText"])

# hadithText = [item.replace("\\u200f","") for item in hadithText]

# hadithText = [item.replace("\u200f","") for item in hadithText]

# df1["HadithText"] = hadithText

# exactNames = list(df1["Exact_Names"])

# exactNames = [item.replace("\\u200f","") for item in exactNames]

# exactNames = [item.replace("\u200f","") for item in exactNames]

# df1["Exact_Names"] = exactNames

# df2 = pd.DataFrame()

# df2["HadithNumber"] = hadithNumber

# df2["HadithText"] = hadithText

# df2["Exact_Names"] = exactNames

# df2.to_excel("C:/Users/iammu/OneDrive/Desktop/comparison/Overall Comparison (error in rule-based)/hadithAndExactNames.xlsx")


###########################################################################################################













# dfN = pd.DataFrame()
# dfN["NameFromRuleBase"] = finalNarratorsNameList
# # dfN.to_excel("NameOfNarrator_FromRuleBased.xlsx")
# df["RuleBasedNames"] = finalNarratorsNameList
# df.to_excel("C:/Users/iammu/OneDrive/Desktop/newNERNamesFrom480Hadith.xlsx")
#####################################################################
#  Comparison 

# df_comp_R_with_E = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/copied fyp/Names and Length Comparison btw Rule_Based and Exact.xlsx")

# testFinal_E_NameList=[]


# eNameList = df_comp_R_with_E['Exact Names']

# for i in range(len(eNameList)):
#     dum=[]
#     if(eNameList[i].count('[') == 1):
#         index_S_NameList=[]
#         eNameList[i]=eNameList[i].replace("[","")
#         eNameList[i]=eNameList[i].replace("]","")
#         dum = eNameList[i].split(",")
#         for j in range(len(dum)):
#             dum[j]= dum[j].strip()
#             if((dum[j][0] and dum[j][-1]) =="'"):
#                 dum[j]= dum[j].replace("'","")
                
#                 if(dum[j].__contains__("-")):
#                     dum[j]= dum[j].replace("-","")
#                     dum[j]= dum[j].strip()
#                 if(dum[j].__contains__("ـ")):
#                     dum[j]= dum[j].replace("ـ","")
#                     dum[j]= dum[j].strip()
#                 if(dum[j].__contains__("،")):
#                     dum[j]= dum[j].replace("،","")
#                     dum[j]= dum[j].strip()
#                 dum[j]= dum[j].strip()
#                 index_S_NameList.append(dum[j])
#     if(len(index_S_NameList)!=0):
#         testFinal_E_NameList.append(index_S_NameList)
#         index_S_NameList=[]
#     MList=[]
#     if(eNameList[i].count('[') == 3):     
#         eNameList[i]= eNameList[i].replace("[","")
#         if((eNameList[i][-1] and eNameList[i][-2]) == "]"):
#             eNameList[i] = eNameList[i][:-3]
#             dum = eNameList[i].split("]")
#             for ii in range(len(dum)):
#                 dum1=[]
#                 index_M_NameList=[]
#                 dum1 = dum[ii].split(",")
#                 for j in range(len(dum1)): 
#                     dum1[j]= dum1[j].strip()
#                     dum1[j]= dum1[j].replace("'","")
#                     if(dum1[j].__contains__("-")):
#                         dum1[j]= dum1[j].replace("-","")
#                         dum1[j]= dum1[j].strip()
#                     if(dum1[j].__contains__("ـ")):
#                         dum1[j]= dum1[j].replace("ـ","")
#                         dum1[j]= dum1[j].strip()
#                     if(dum1[j].__contains__("،")):
#                         dum1[j]= dum1[j].replace("،","")
#                         dum1[j]= dum1[j].strip()
#                     dum1[j]= dum1[j].strip()
#                     if(dum1[j] !=""):
#                         index_M_NameList.append(dum1[j])
            
#                 MList.append(index_M_NameList)   
#     if(len(MList)!=0):
#         testFinal_E_NameList.append(MList)



# dfCheck = pd.read_excel("NameCheckWithNER.xlsx")
# checkName = dfCheck.Names
# checkNameList=[]
# for i in range(len(checkName)):
#     dum=[]
#     if(checkName[i].count('[') == 1):
#         index_S_NameList=[]
#         checkName[i]=checkName[i].replace("[","")
#         checkName[i]=checkName[i].replace("]","")
#         dum = checkName[i].split(",")
#         for j in range(len(dum)):
#             dum[j]= dum[j].strip()
#             if((dum[j][0] and dum[j][-1]) =="'"):
#                 dum[j]= dum[j].replace("'","")
                
#                 if(dum[j].__contains__("-")):
#                     dum[j]= dum[j].replace("-","")
#                     dum[j]= dum[j].strip()
#                 if(dum[j].__contains__("ـ")):
#                     dum[j]= dum[j].replace("ـ","")
#                     dum[j]= dum[j].strip()
#                 if(dum[j].__contains__("،")):
#                     dum[j]= dum[j].replace("،","")
#                     dum[j]= dum[j].strip()
#                 dum[j]= dum[j].strip()
#                 index_S_NameList.append(dum[j])
#     if(len(index_S_NameList)!=0):
#         checkNameList.append(index_S_NameList)
#         index_S_NameList=[]
#     MList=[]
#     if(checkName[i].count('[') == 3):     
#         checkName[i]= checkName[i].replace("[","")
#         if((checkName[i][-1] and checkName[i][-2]) == "]"):
#             checkName[i] = checkName[i][:-3]
#             dum = checkName[i].split("]")
#             for ii in range(len(dum)):
#                 dum1=[]
#                 index_M_NameList=[]
#                 dum1 = dum[ii].split(",")
#                 for j in range(len(dum1)): 
#                     dum1[j]= dum1[j].strip()
#                     dum1[j]= dum1[j].replace("'","")
#                     if(dum1[j].__contains__("-")):
#                         dum1[j]= dum1[j].replace("-","")
#                         dum1[j]= dum1[j].strip()
#                     if(dum1[j].__contains__("ـ")):
#                         dum1[j]= dum1[j].replace("ـ","")
#                         dum1[j]= dum1[j].strip()
#                     if(dum1[j].__contains__("،")):
#                         dum1[j]= dum1[j].replace("،","")
#                         dum1[j]= dum1[j].strip()
#                     dum1[j]= dum1[j].strip()
#                     if(dum1[j] !=""):
#                         index_M_NameList.append(dum1[j])
            
#                 MList.append(index_M_NameList)   
#     if(len(MList)!=0):
#         checkNameList.append(MList)



# from camel_tools.ner import NERecognizer

# ner = NERecognizer('CAMeL-Lab/bert-base-arabic-camelbert-mix-ner')

# finalNameCheckFromNER=[]
# for i in range(len(checkNameList)):
#     sent_split = checkNameList[i]
#     # for j in range(len(checkNameList[i])):
        
        
#     splitWord=[]
#     for i in range(len(sent_split)):
#         splitWord.append(sent_split[i].split())
        
#     nameList=[]
#     for i in range(len(splitWord)):
#         label=ner.predict_sentence(splitWord[i])
#         print(list(zip(splitWord[i],label)))
        
#         #New Code and comment the below RAsool name
#         # if(sent_split[i].__contains__('النبي صلى الله عليه وسلم') or sent_split[i].__contains__('رسول الله صلى الله عليه وسلم')):
            
#         #     nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
#         #     count=1
#         #     break
        
#         dum=''
#         for j in range(len(label)):
#             if (label[j]=="B-PERS" or label[j]=="I-PERS"):
#                 dum =dum+splitWord[i][j]+' '
#             else:
#                 if(dum !=''):
#                     nameList.append(dum)
#                     dum=''
#                 #Hear From Father Mother Etc
                
#                 if(splitWord[i][j]=="أبيه"):
#                     nameList.append("أبيه")
                    
#                 if(splitWord[i][j]=="أبي"):
#                     nameList.append("أبي")
                    
#                 # #Rasool Name Recong From Tokens
                    
#                 if(sent_split[i] =="محمد صلی اللہ علیہ وآلہ وسلم"):
#                     # if(splitWord[i][j+1]=='صلى' and splitWord[i][j+2]=='الله' and splitWord[i][j+3]=='علیہ' and splitWord[i][j+4]=='وآلہ' and splitWord[i][j+5]=='وسلم'):
#                     nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
#                         # count=1
#                     break
                    
#                     print(dum)
#         # if(count==1):
#         #     break
        
#         nameList.append(dum)
#         dum=''
        
#         while("" in nameList) :
#             nameList.remove("")
            
#     finalNameCheckFromNER.append(nameList)
        
# dfCheck["NameFromNER"] = finalNameCheckFromNER
