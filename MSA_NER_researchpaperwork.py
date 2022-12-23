# -*- coding: utf-8 -*-
"""ResearchPaperWork.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x6j0oPN3kkQ3zTK2G3kY7kUZC_TTrDGc
"""

pip install transformers

# import pandas as pd
# df = pd.read_excel("/content/Exact_RuleBased_OldNER_NewNERNamesFrom480Hadith.xlsx")

# HadithList = df.HadithText
# WithoutAhrabList=[]
# #sentence="وَحَدَّثَنَا مُحَمَّدُ بْنُ عَبْدِ اللَّهِ بْنِ نُمَيْرٍ، حَدَّثَنَا أَبِي، حَدَّثَنَا سَعِيدُ بْنُ عُبَيْدٍ، حَدَّثَنَا عَلِيُّ بْنُ رَبِيعَةَ، قَالَ أَتَيْتُ الْمَسْجِدَ وَالْمُغِيرَةُ أَمِيرُ الْكُوفَةِ قَالَ فَقَالَ الْمُغِيرَةُ سَمِعْتُ رَسُولَ اللَّهِ صلى الله عليه وسلم يَقُولُ ‏ ‏ إِنَّ كَذِبًا عَلَىَّ لَيْسَ كَكَذِبٍ عَلَى أَحَدٍ فَمَنْ كَذَبَ عَلَىَّ مُتَعَمِّدًا فَلْيَتَبَوَّأْ مَقْعَدَهُ مِنَ النَّارِ ‏‏ ‏.‏ ‏"
# for hadith in HadithList:
#     dum123 = ""
    
#     # Aeraab Remover Code
#     for i in range(len(hadith)):
#         no = ord(hadith[i])
#         if (no == 1614 or no == 1615 or no == 1616 or no == 1618 or no == 1617 or no == 1612 or no == 1613 or no == 1611):
#             continue
#         else:
#             dum123 += hadith[i]
        
    
#     dum123 = dum123.strip()
#     WithoutAhrabList.append(dum123)

#Extracting name fo Narrators From Hadith(WithoutAhrab)

def extractingNames(notMatchName):
  # finalNameList =[]
  # # List of Prophet's صلی اللہ علیہ وآلہ وسلم name that are used in Ahadith
    # prophetNamesReplacerList = ["النبي ـ صلى الله عليه وسلم" ,"النبي صلى الله عليه وسلم","رسول الله صلى الله عليه وسلم","النبي ‌صلی ‌اللہ ‌علیہ ‌وآلہ ‌وسلم","محمد صلی اللہ علیہ وآلہ وسلم","للنبي صلی اللہ علیہ وسلم","يا رسول الله","رسول الله", "صلى الله عليه وسلم",]
    # extraWords = ["رضي الله تعالى عنه","رضي الله عنه -","- رضي الله عنه -","رضي الله عنه","رضي الله عنها","رضي الله عنهما","رضي الله عنهما ","ـ رضي الله عنها ـ","رضى الله تعالى عنه","رضى الله عنه -","رضى الله عنه","رضى الله عنها","رضى الله عنهما ","ـ","- رضى الله عنه -","رضى الله عنه","ـ رضى الله عنها ـ"]
    # for i in extraWords:
    #     HadithText = HadithText.replace(i,"")
    # isPresentProphetName = False
    # modifiedHadithText =[]
    # for j in prophetNamesReplacerList:
    #     if(HadithText.__contains__(j)):
    #         isPresentProphetName=True
    #         dum = []
    #         dum = HadithText.split(j)
    #         HadithText = dum[0]
    #         modifiedHadithText=dum[0]
            
    # if(isPresentProphetName==False):
    #     modifiedHadithText = HadithText
    
    from transformers import pipeline
    pos = pipeline('token-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-mix-pos-msa')
    #text = 'إمارة أبوظبي هي إحدى إمارات دولة الإمارات العربية المتحدة السبع'
    dummy = pos(notMatchName)
    print(dummy)

    nameList = []
    name = ""
    pre_end = 0
    for j in range(len(dummy)):
        
        dic = dummy[j]
        
        if(dic.get("entity")=="noun_prop"):
            if(name=="" and pre_end==0):
                name = name +dic.get("word")
                pre_end = dic.get("end")
            else:
                if(dic.get("start")==pre_end):
                    name = name + dic.get("word")
                    pre_end = dic.get("end")
                else:
                    name = name  + " " + dic.get("word")
                    pre_end = dic.get("end")
        
    if(name!=""):  
        if(name.__contains__("#")):
            name = name.replace("#","")
                
                
    nameList.append(name.strip())
    name = ""
    pre_end=0

    # finalNameList.append(nameList)

    # if(isPresentProphetName):
    #     nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")

    return nameList

  # lastNameLists =[]

  # for i in range(len(finalNameList)):
  #   nameLists =[]
  #   count=0
  #   for j in range(len(finalNameList[i])):
  #     # if(finalNameList[i][j]== 'محمد' and finalNameList[i][j+1]=='ی اللہ') or (finalNameList[i][j]== 'محمد' and finalNameList[i][j+1]=='ی الل') or (finalNameList[i][j]== 'محمد' and finalNameList[i][j+1]=='الل'):
  #     #   nameLists.append('محمد صلی اللہ علیہ وآلہ وسلم')
  #     #   count=1
  #     else:
  #       if(count==1):
  #         break
  #       else:
  #         nameLists.append(finalNameList[i][j])
  #   lastNameLists.append(nameLists)





# for i in range(len(WithoutAhrabList)):
  #Check For OnlyNameList
  # if(df.Absent_Names[i].count('[')==1):

  # # df.Names[i] = df.Names[i].replace("]","")
  # # df.Names[i] = df.Names[i].replace("'","")
  # # df.Names[i] = df.Names[i].replace("[","")
  # # df.Names[i]

# print(extractingNames())

#for training in nNetwork

import pandas as pd
df = pd.read_excel("/content/NotMatchAfterRuleBased.xlsx")
df.head()

len(df)

df = df.dropna()

len(df)

names = []
for i in df.notMatch:
  names.append(extractingNames(i))

names









# finalResultList=[]
# for i in range(len(WithoutAhrabList)):
#     print(i)
#     if(WithoutAhrabList[i].__contains__(" ح ") or WithoutAhrabList[i].__contains__(" ح، ") or WithoutAhrabList[i].__contains__("ح‏.") or WithoutAhrabList[i].__contains__(" ح. ")):
#         splittedList=[]
#         if(WithoutAhrabList[i].__contains__("ح‏.")):
#             splittedList=WithoutAhrabList[i].split("ح‏.")
#         elif(WithoutAhrabList[i].__contains__(" ح، ")):
#             splittedList=WithoutAhrabList[i].split(" ح، ")
#         elif(WithoutAhrabList[i].__contains__(" ح. ")):
#             splittedList=WithoutAhrabList[i].split(" ح. ")
#         else:
#             splittedList=WithoutAhrabList[i].split(" ح ") 
#         mul_sanadList=[]
#         for j in splittedList:
#             mul_sanadList.append(extractingNames(j))
#         finalResultList.append(mul_sanadList)
#     else:
#         finalResultList.append(extractingNames(WithoutAhrabList[i]))

dum = extractingNames("أبا مرة مولى عقيل بن أبي طالب")

dum

df["NewNERNames"] = finalResultList
df.to_excel("/content/latestExact_RuleBased_OldNER_NewNERNames.xlsx")

# For Testing Purpose (Only For One Hadith)

import pandas as pd
df1 = pd.read_excel("/content/Exact_RuleBased_OldNER_NewNERNamesFrom480Hadith.xlsx")
WithoutAhrabList = df1["HadithText"][388]

finalResultList=[]

if(WithoutAhrabList.__contains__(" ح ") or WithoutAhrabList.__contains__(" ح، ") or WithoutAhrabList.__contains__("ح‏.") or WithoutAhrabList.__contains__(" ح. ")):
    splittedList=[]
    if(WithoutAhrabList.__contains__("ح‏.")):
        splittedList=WithoutAhrabList.split("ح‏.")
    elif(WithoutAhrabList.__contains__(" ح، ")):
        splittedList=WithoutAhrabList.split(" ح، ")
    elif(WithoutAhrabList.__contains__(" ح. ")):
        splittedList=WithoutAhrabList.split(" ح. ")
    else:
        splittedList=WithoutAhrabList.split(" ح ") 
    mul_sanadList=[]
    for j in splittedList:
        mul_sanadList.append(extractingNames(j))
    finalResultList.append(mul_sanadList)
else:
    finalResultList.append(extractingNames(WithoutAhrabList))

finalResultList

# For Testing Purpose (Only For One Hadith)

df2 = pd.DataFrame()
df2["single"] = finalResultList
df2.to_excel("/content/singleHadith.xlsx")

#Function for extracting Lists from 'List Formatted Strings'
def extractListsFrom_ListFormattedStrings(dummy):
    finalNamesList = []
    for i in range(len(dummy)):
        dum = dummy[i]
        if(dum.count("[")==1):
            dum=dum.replace("[","")
            dum=dum.replace("]","")
            dum=dum.replace("'","")
            dumList = dum.split(",")
            dumList = [item.strip() for item in dumList]
            finalNamesList.append(dumList)
        else:
            separateList = dum.split("],")
            multipleLists = []
            for i in range(len(separateList)):
                index = separateList[i]
                index=index.replace("[","")
                index=index.replace("]","")
                index=index.replace("'","")
                indList = index.split(",")
                indList = [item.strip() for item in indList]
                multipleLists.append(indList)
            finalNamesList.append(multipleLists)
    return finalNamesList
#***********************************************************

import pandas as pd
df5 = pd.read_excel("/content/NamesAndLengthComparison_RuleBased_andExactNamesFrom480Hadith.xlsx")
ruleBasedAbsentNamesList = extractListsFrom_ListFormattedStrings(list(df5["NameAbsentInRuleBased"]))
finalNameList =[]
for i in range(len(ruleBasedAbsentNamesList)):
    print(i)
    if(type(ruleBasedAbsentNamesList[i][0])==str):
        namesList = []
        for j in range(len(ruleBasedAbsentNamesList[i])):
            if(ruleBasedAbsentNamesList[i][j]=="No Name Absent"):
                continue
            else:
                dum = extractingNames(ruleBasedAbsentNamesList[i][j])
                if(len(dum)==0):
                    continue
                else:
                    for k in dum:
                        namesList.append(k)
        finalNameList.append(namesList)
                
    else:
        multipleNamesList = []
        for j in ruleBasedAbsentNamesList[i]:
            namesList = []
            for k in j:
                if(k=="No Name Absent"):
                    continue
                else:
                    dum = extractingNames(k)
                    if(len(dum)==0):
                        continue
                    else:
                        for l in dum:
                            namesList.append(l)
            multipleNamesList.append(namesList)
        
        finalNameList.append(multipleNamesList)

df5["CheckAbsentNamesWithNewNER"] = finalNameList

df5.to_excel("/content/NamesAndLengthComparison_RuleBased_afterApplingNewNER_withExactNamesFrom480Hadith.xlsx")

# Testing purpose for only one index

df5 = pd.read_excel("/content/NamesAndLengthComparison_RuleBased_andExactNamesFrom480Hadith.xlsx")
ruleBasedAbsentNamesList = extractListsFrom_ListFormattedStrings(list(df5["NameAbsentInRuleBased"]))
index = ruleBasedAbsentNamesList[27] # Give index here for checking purpose
finalNameList =[]

if(type(index[0])==str):
    namesList = []
    for j in range(len(index)):
        if(index[j]=="No Name Absent"):
            continue
        else:
            dum = extractingNames(index[j])
            if(len(dum)==0):
                continue
            else:
                for k in dum:
                    namesList.append(k)
    finalNameList.append(namesList)
            
else:
    multipleNamesList = []
    for j in index:
        namesList = []
        for k in j:
            if(k=="No Name Absent"):
                continue
            else:
                dum = extractingNames(k)
                if(len(dum)==0):
                    continue
                else:
                    for l in dum:
                        namesList.append(l)
        multipleNamesList.append(namesList)
    
    finalNameList.append(multipleNamesList)

finalNameList

finalResultList=[]
for i in range(len(WithoutAhrabList)):
    if(WithoutAhrabList[i].__contains__(" ح ") or WithoutAhrabList[i].__contains__(" ح، ") or WithoutAhrabList[i].__contains__("ح‏.") or WithoutAhrabList[i].__contains__(" ح. ")):
        splittedList=[]
        if(WithoutAhrabList[i].__contains__("ح‏.")):
            splittedList=WithoutAhrabList[i].split("ح‏.")
        elif(WithoutAhrabList[i].__contains__(" ح، ")):
            splittedList=WithoutAhrabList[i].split(" ح، ")
        elif(WithoutAhrabList[i].__contains__(" ح. ")):
            splittedList=WithoutAhrabList[i].split(" ح. ")
        else:
            splittedList=WithoutAhrabList[i].split(" ح ") 
        mul_sanadList=[]
        for i in splittedList:
            mul_sanadList.append(extractingNames(i))
        finalResultList.append(mul_sanadList)
    else:
        finalResultList.append(extractingNames(WithoutAhrabList[i]))

# import pandas as pd
# dfNERName = pd.DataFrame()
# dfNERName["Names"] = finalResultList
# dfNERName.to_excel("/home/NameFromNER.xlsx")
# df["new_NERNames"]=finalResultList
df.to_excel("/home/newNERNamesFrom480Hadith.xlsx")

lastNameLists =[]

for i in range(len(finalNameList)):
  nameLists =[]
  count=0
  for j in range(len(finalNameList[i])):
    if(finalNameList[i][j]== 'محمد' and finalNameList[i][j+1]=='ی اللہ') or (finalNameList[i][j]== 'محمد' and finalNameList[i][j+1]=='ی الل') or (finalNameList[i][j]== 'محمد' and finalNameList[i][j+1]=='الل'):
      nameLists.append('محمد صلی اللہ علیہ وآلہ وسلم')
      count=1
    else:
      if(count==1):
        break
      else:
        nameLists.append(finalNameList[i][j])
  lastNameLists.append(nameLists)

# df["New_NERNames"] =

dum = ['عبد الله بن نمير', 'إسماعيل', 'ابن أبي خالد', 'قيس', 'أبو بكر', 'الله', 'u', 'u', 'f', 'محمد', 'ی اللہ علی']
new = []
for i in dum:
  print(i)
  if((i>='a' and i<='z') or (i>='A' and i<='Z')):
    continue
  else:
    new.append(i)
dum = new
# dum321 = [item for item in dum321 if (not item.isalpha())]
# print(dum321)

prophetNamesReplacerList = ["النبي ـ صلى الله عليه وسلم" ,"النبي صلى الله عليه وسلم","رسول الله صلى الله عليه وسلم","النبي ‌صلی ‌اللہ ‌علیہ ‌وآلہ ‌وسلم","محمد صلی اللہ علیہ وآلہ وسلم","للنبي صلی اللہ علیہ وسلم","يا رسول الله","رسول الله", "صلى الله عليه وسلم",]
isPresentProphetName = False
modifiedHadithText =[]
for i in range(5):
    for j in prophetNamesReplacerList:
        if(WithoutAhrabList[i].__contains__(j)):
            dum = []
            dum = WithoutAhrabList[i].split(j)
            WithoutAhrabList[i] = dum[0]
            modifiedHadithText=dum[0]
            isPresentProphetName=True
    if(isPresentProphetName==False):
        modifiedHadithText = WithoutAhrabList[i]

df.head()

#Old NER Model
from re import split
def split_string(string, delimiters):
    """Splits a string by a list of delimiters.
    Args:
        string (str): string to be split
        delimiters (list): list of delimiters
    Returns:
        list: list of split strings
    """
    pattern = r'|'.join(delimiters)
    return split(pattern, string)

def nameArrangeFunction(sent_split2):
    sent_split2=sent_split
    for i in range(len(sent_split2)):
        if(sent_split2[i].__contains__('-')):
            firstDash=sent_split2[i].index('-')
            lastDash= sent_split2[i].rfind('-')
            
            nameCut = sent_split2[i][firstDash+1:lastDash]
            sent_split2[i-1]=sent_split2[i-1]+" "+nameCut
            sent_split2[i]=sent_split2[i][lastDash+1:]
        else:
            sent_split2[i]=sent_split2[i]
                     
    return sent_split2

pip install camel_tools

def singleSanad(sentence):
    from camel_tools.utils.dediac import dediac_ar
    without_ahraab = dediac_ar(sentence)

    sent_split= split_string(without_ahraab,["حدثني","وحدثنا","حدثنا","نحوه","عن","قال،","فقال","سمعت","يقول","أنه","سمع","أخبرني","أن","أخبرنا","أنه","اخبرنا","سال","وقال","قالت","قالا","جميعا","قلت","أنها","وحدثني","في حديثه","يخطب","أخبره","تابعه","إنه","انه","كثيرا","قال:","قال","أنبأنا","إذا","أحدثكم","قام","فكتب","حديث","حديثه","أخبرهم","وكانت","يحدث","يخبر","فقلت","حدث","وكان","يخبر","لحديث","حدثها","حدثتنيه","ثقة","عقلت","أخبروني","حدث","وقد","روى","صحبت","حدثناه","سألت","هرقل","لي","هذا","الحديث","وأنبأنا","حدثكم","من","ولقد","وعن","شهدت","كتب","زوج","يذكر","سألني","قالوا","إلى","فكان","لما","قدم","أشياء","رواية","رأيت","أقبلت","قراءة","وأنا","أسمع","إن","حدثه","بهذا","حديثا","بأى","اخبرني","كان",'كنت',"يحدثونه","حدثتني","شىء","وغير","واحد","أسمع","وأخبرني"])
    
    #NER
    from camel_tools.ner import NERecognizer

    ner = NERecognizer('CAMeL-Lab/bert-base-arabic-camelbert-mix-ner')

    splitWord=[]
    for i in range(len(sent_split)):
        splitWord.append(sent_split[i].split())
    

    #Removing '-' from name if come
    for i in range(len(splitWord)):
        splitWord[i]  = [word for word in splitWord[i] if word!='-']
    

    nameList=[]
    count=0


    WordReplaceV1=["حدثني","وحدثنا","حدثنا","أخبرني","أخبرنا","اخبرنا","حديثه","أخبره","اخبرني","وحدثني","وأخبرني"]


    for i in range(len(splitWord)):
        label=ner.predict_sentence(splitWord[i])

        dum=''
        for j in range(len(label)):
            if(splitWord[i][j] in WordReplaceV1):
                continue
            if (label[j]=="B-PERS" or label[j]=="I-PERS"):
                dum =dum+splitWord[i][j]+' '
            else:
                if(dum !=''):
                    nameList.append(dum)
                    dum=''
                
                if(splitWord[i][j].strip() =="النبي" or splitWord[i][j].strip()=="النبي ـ"):
                    if(splitWord[i][j+1]=='صلى' and splitWord[i][j+2]=='الله'):
                        nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
                        count=1
                        break
                if(splitWord[i][j] =="للنبي"):
                    if(splitWord[i][j+1]=='صلی' and splitWord[i][j+2]=='اللہ'):
                        nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
                        count=1
                        break
                if(splitWord[i][j] =="رسول"):
                    if(splitWord[i][j+1]=='الله' and splitWord[i][j+2]=='صلى' and splitWord[i][j+3]=='الله'):
                        nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
                        count=1
                        break
                if(splitWord[i][j] =="صلى"):
                    if(splitWord[i][j+1]=='الله'):
                        nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
                        count=1
                        break
                if(splitWord[i][j] =="رسول"):
                    if(splitWord[i][j+1]=='الله'):
                        nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
                        count=1
                        break
                if(splitWord[i][j] =="يا"):
                    if(splitWord[i][j+1]=='رسول' and splitWord[i][j+2]=='الله'):
                        nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
                        count=1
                        break
                if(splitWord[i][j] =="النبي"): 
                    if(splitWord[i][j+1]=='صلی' and splitWord[i][j+2]=='‌اللہ'):
                        nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
                        count=1
                        break
                    
        if(count==1):
            break
        
        nameList.append(dum)
        dum=''

    
    while("" in nameList) :
        nameList.remove("")
        
    #agr remove comma here than malik will be name 
    nameList =[name.replace("،","") for name in nameList]
    return nameList

dum = singleSanad('حدثنا أبو اليمان، أخبرنا شعيب، عن الزهري،')
print(dum)

def multipleSanad(sentenceList):
    finalNameList=[]
    for sentence in sentenceList:
        finalNameList.append(singleSanad(sentence))
    return finalNameList

finalNarratorsNameList=[]


import pandas as pd 
df = pd.read_excel("/content/ExactAndRuleBasedNames.xlsx")
# df
hadithList = df.HadithText

for i in range(len(hadithList)):  
    print(i)
    if(hadithList[i].__contains__(" ح ") or hadithList[i].__contains__(" ح، ") or hadithList[i].__contains__("ح‏.") or hadithList[i].__contains__(" ح. ")):
        if(hadithList[i].__contains__("ح‏.")):
            txtList=hadithList[i].split("ح‏.")
        elif(hadithList[i].__contains__(" ح، ")):
            txtList=hadithList[i].split(" ح، ")
        elif(hadithList[i].__contains__(" ح. ")):
            txtList=hadithList[i].split(" ح. ")
        else:
            txtList=hadithList[i].split(" ح ")
            
        return_M_List= multipleSanad(txtList)
        finalNarratorsNameList.append(return_M_List)
    else:
        return_S_List = singleSanad(hadithList[i])
        finalNarratorsNameList.append(return_S_List)

# For Testing Purpose (Only For One Hadith)

finalNarratorsNameList=[]

import pandas as pd 
df = pd.read_excel("/content/Exact_RuleBased_OldNER_NewNERNamesFrom480Hadith.xlsx")

hadithList = df1["HadithText"][65]


if(hadithList.__contains__(" ح ") or hadithList.__contains__(" ح، ") or hadithList.__contains__("ح‏.") or hadithList.__contains__(" ح. ")):
    if(hadithList.__contains__("ح‏.")):
        txtList=hadithList.split("ح‏.")
    elif(hadithList.__contains__(" ح، ")):
        txtList=hadithList.split(" ح، ")
    elif(hadithList.__contains__(" ح. ")):
        txtList=hadithList.split(" ح. ")
    else:
        txtList=hadithList.split(" ح ")
        
    return_M_List= multipleSanad(txtList)
    finalNarratorsNameList.append(return_M_List)
else:
    return_S_List = singleSanad(hadithList)
    finalNarratorsNameList.append(return_S_List)

finalNarratorsNameList

df2 = pd.DataFrame()
df2["single"] = finalNarratorsNameList
df2.to_excel("/content/singleHadith.xlsx")

df.to_excel("/content/Exact_RuleBased_OldNERNames.xlsx")