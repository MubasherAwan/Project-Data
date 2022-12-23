# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:27:40 2022

@author: iammu
"""

import pandas as pd

dfc = pd.read_csv('C:/Users/iammu/OneDrive/Desktop/PyhtonProgram/matnnais.csv')
textm=list(dfc['Hadith_Matn'])

dum = []

for i in range(len(textm)):
    if(type(textm[i])==float):
        textm[i] = str(textm[i])
        
for i in range(len(textm)):
    if(textm[i]=="nan"):
        continue
    else:
        dum.append(textm[i])
        
textm = dum
#اخلاقا
# خياركم اسلاما احاسنكم اخلاقا اذا فقهوا
# تم میں سے اسلام کا انتخاب اخلاق کے لحاظ سے تم میں سب سے بہتر ہے اگر وہ سمجھ جائیں۔
# رضى الرب في رضى الوالد وسخط الرب في سخط الوالد
# رب کی رضا والد کی رضا میں ہے، اور رب کی ناراضگی والد کی رضا میں ہے۔ باپ کا غصہ۔


# مسواک
# لولا ان اشق على امتي لامرتهم بالسواك عند كل صلاة
# ”اگر مجھے اپنی قوم پر سختی کرنا نہیں تھا، میں انہیں ہر نماز کے وقت ٹوتھ پک استعمال کرنے کا حکم دیتا۔
# لعائشة باي شيء كان يبدا النبي صلى الله عليه وسلم اذا دخل بيته قالت بالسواك
# عائشہ کے لیے نبی کریم صلی اللہ علیہ وسلم کے گھر میں داخل ہوتے ہی کوئی بھی دعا شروع ہو جاتی تھی، انہوں نے ٹوتھ پک کے ساتھ کہا۔

# text2=[" لولا ان اشق على امتي لامرتهم بالسواك عند كل صلاة"
 #   ,"رضى الرب في رضى الوالد وسخط الرب في سخط الوالد"," لعائشة باي شيء كان يبدا النبي صلى الله عليه وسلم اذا دخل بيته قالت بالسواك"
#     ,"كنا جلوسا عند النبي صلی اللہ علیہ وسلم كانما على رءوسنا الطير ، ما يتكلم منا متكلم اذ جآءه اناس ، فقالوا : من احب عباد الله الى الله ؟ ، قال : احسنهم خلقا"
#       ]

# text2=[" اوصيك ان تستحي من الله عز وجل ، كما تستحي رجلا من صالحي قومك "
     #  ," قال رسول الله صلی اللہ علیہ وسلم الحياء من الايمان والايمان في الجنة والبذاء من الجفاء والجفاء في النار. "  
#    ,  " الراحمون يرحمهم الرحمن تبارك وتعالي ارحموا من في الارض"  
# ,"يرحمكم من في السماء الرحم شجنة من الرحمن فمن وصلها وصله الله ومن قطعها قطعه الله"
# ," اكتنيت وليس لك ولد ،  وانتميت الى العرب وانت من الروم ،  وفيك سرف في الطعام ،  قال اما قولك اكتنيت ولم يولد لك ،  فان رسول الله  صلی اللہ علیہ وسلم كناني ابا يحيى ،  واما قولك انتميت الى العرب ،  ولست منهم ،  وانت رجل من الروم ،  فاني رجل من النمر بن قاسط فسبتني الروم من الموصل ، بعد اذ انا غلام عرفت نسبي ،  واما قولك   :   فيك سرف في الطعام فاني سمعت رسول الله  صلی اللہ علیہ وسلم يقول   :   خياركم من اطعم الطعام . "
# ]
   
# text=["أقسم بمن نفسي بيده لا يقدر أحدكم. كن مؤمنا حتى أكون أعز إليه من أبيه وابنه ، قال سعيد بن يحيى بن منا سعيد القرشي. قال: حدثنا أبي ، فقال: حدثنا أبو بردة بن عبد الله بن أبي بردة ، رواه عن أبي بردة ، رواه عن أبي موسى ، يا رسول الله! والله ما هو الإسلام الأفضل؟ قَالَ: مَنْ دَعَمَ المسلمين بلسانه ويده."
     # ,   " سمعت ابن الزبير ، يخطب ، يقول : قال محمد صلى الله عليه وسلم    من لبس الحرير في الدنيا لم يلبسه في الاخرة    ."   
#   ,"من قال حين يسمع النداء ، اللهم رب هذه الدعوة التامة والصلاة القائمة ات محمدا ۨ الوسيلة والفضيلة وابعثه مقاما محمودا ۨ الذي وعدته ، حلت له شفاعتي يوم القي\امة "
# ,"  حدثنا شيبان ، عن يحيى ، عن ابي سلمة ، عن عائشة    كان النبي صلى الله عليه وسلم يصلي ركعتين خفيفتين بين النداء والاقامة من صلاة الصبح"
# ,"قال : سمعت عمرو بن عامر الانصاري ، عن انس بن مالك ، قال :    كان المؤذن اذا اذن قام ناس من اصحاب النبي صلى الله عليه وسلم يبتدرون السواري حتى يخرج النبي صلى الله عليه وسلم ، وهم كذلك يصلون الركعتين قبل المغرب ، ولم يكن بين الاذان والاقامة شيء    ، قال عثمان بن جبلة : وابو داود ، عن شعبة ، لم يكن بينهما الا قليل"
# ]
#text=["اوصيك ان تستحي من الله عز وجل ، كما تستحي رجلا من صالحي قومك"]
#text2=["الراحمون يرحمهم الرحمن تبارك وتعالي ارحموا من في الارض"]

#text1=["فقالت : ما كنت لافشي سر رسول الله صلى الله عليه وسلم حتى قبض النبي صلى الله عليه وسلم فسالتها ، فقالت : اسر الي ان جبريل كان يعارضني القران كل سنة مرة وانه عارضني العام مرتين ولا اراه الا حضر اجلي وانك اول اهل بيتي لحاقا بي فبكيت ، فقال : اما ترضين ان تكوني سيدة نساء اهل الجنة او نساء المؤمنين فضحكت لذلك    .
# ",
# "حدثني احمد بن اشكاب ، حدثنا محمد بن فضيل عن عمارة بن القعقاع عن ابي زرعة عن ابي هريرة رضي الله عنه ، قال قال النبي صلى الله عليه وسلم :    كلمتان حبيبتان الى الرحمن خفيفتان على اللسان ، ثقيلتان في الميزان ، سبحان الله وبحمده ، سبحان الله العظيم    .
# ",
# "حدثنا ابو النعمان ، حدثنا مهدي بن ميمون سمعت محمد بن سيرين ، يحدث ، عن معبد بن سيرين ، عن ابي سعيد الخدري رضي الله ، عن النبي صلى الله عليه وسلم ، قال :    يخرج ناس من قبل المشرق ويقرءون القران لا يجاوز تراقيهم يمرقون من الدين كما يمرق السهم من الرمية ، ثم لا يعودون فيه حتى يعود السهم الى فوقه قيل ما سيماهم ؟ ، قال : سيماهم التحليق ، او قال التسبيد    .
# ",
# "حدثنا قبيصة ، حدثنا سفيان ، عن منصور ، عن امه ، عن عائشة ، قالت : كان النبي صلى الله عليه وسلم    يقرا القران وراسه في حجري وانا حائض    .
# "

# ]
import nltk
from nltk.corpus import stopwords
arabicStopwords=stopwords.words('Arabic')
#print(arabicStopwords)


#__stopword Code
List=[]
for i in arabicStopwords:
    dummy = i
    dum1 = ""
    dum2 = ""
    outerFlag1=False
    outerFlag2=False
    outerFlag3=False
    if(dummy[0]=="ا"):
        outerFlag1=True
    if(dummy[0]=="إ"):
        outerFlag2=True
    if(dummy[0]=="أ"):
        outerFlag3=True
    if(outerFlag1):
        innerFlag=True
        for j in range(len(dummy)):
            if(dummy[j]=="ا" and innerFlag):
                dum1+="إ"
                dum2+="أ"
                innerFlag=False
            else:
                dum1+=dummy[j]
                dum2+=dummy[j]
    if(outerFlag2):
        innerFlag=True
        for j in range(len(dummy)):
            if(dummy[j]=="إ" and innerFlag):
                dum1+="ا"
                dum2+="أ"
                innerFlag=False
            else:
                dum1+=dummy[j]
                dum2+=dummy[j]
    if(outerFlag3):
        innerFlag=True
        for j in range(len(dummy)):
            if(dummy[j]=="أ" and innerFlag):
                dum1+="إ"
                dum2+="ا"
                innerFlag=False
            else:
                dum1+=dummy[j]
                dum2+=dummy[j]
    if(dum1 != "" and dum2 != ""):
        List.append(dum1)
        List.append(dum2)


arabicStopwords = arabicStopwords + List

arabicStopwords = list(dict.fromkeys(arabicStopwords))

#__



#print(ArabicStopwords)
#text.split()


listRange=[]
for i in range(len(textm)):
    listRange.append(str(i))
    
#...........stopwordremove............
# without_stopwords=[]
# for word in str(spr):
#     if word not in arabicStopwords:
#         without_stopwords.append(word)
# print(without_stopwords)
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
count_vectorizer = CountVectorizer(stop_words=(arabicStopwords))
#count_vectorizer = CountVectorizer()
print(count_vectorizer)
sparse_matrix = count_vectorizer.fit_transform(textm)
doc_term_matrix = sparse_matrix.todense()
dfm = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=listRange)
dfm

# lst = []
# for i in range(1,20):
#     lst.append(i)

# print (lst)
# sparse_matrix2 = count_vectorizer.transform(text2)
# doc_term_matrix2 = sparse_matrix2.todense()
# df1 = pd.DataFrame(doc_term_matrix2, 
#                   columns=count_vectorizer.get_feature_names(), 
#                   index=listRange)
# df1
# Compute Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity
samilarity_matrix_matn=cosine_similarity(dfm, dfm)
print(samilarity_matrix_matn)