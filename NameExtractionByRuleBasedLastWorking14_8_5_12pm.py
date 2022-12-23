# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:43:18 2022

@author: iammu
"""

def multipleSanads(txt):
    WordReplace=["حدثني","وحدثنا","حدثنا","نحوه","عن","قال،","فقال","سمعت","يقول","أنه","سمع","أخبرني","مولى","أن","أخبرنا","اخبرنا","سال","قالت","قالا","جميعا","قلت","أنها","وحدثني","في حديثه","يخطب","أخبره","تابعه","إنه","انه","كثيرا","قال:","قال","أنبأنا","إذا","أحدثكم","قام","فكتب","يحدث","فقلت","وقد","روى","هذا","الحديث","حدثكم","من","ولقد","وعن","كتب","زوج","يذكر","سألني","قالوا","إلى","فكان","لما","قدم","أشياء","رواية","رأيت","أقبلت","قراءة","وأنا","أسمع","إن","حدثه","بهذا","حديثا","بأى","اخبرني","كان",'كنت',"يحدثونه","حدثتني","شىء","وغير","واحد","أسمع","وأخبرني"]

    #Keys=["حدثنا","عن","قال","فقال","سمعت","يقول","أنه","سمع","أخبرني","مولى","أن","أخبرنا",":","في حديثه","تابعه","انه","اخبرني","وأخبرني","وحدثنا"]
    

    #txt='''حَدَّثَنَا مُحَمَّدُ بْنُ سِنَانٍ، قَالَ حَدَّثَنَا فُلَيْحٌ، ح وَحَدَّثَنِي إِبْرَاهِيمُ بْنُ الْمُنْذِرِ، قَالَ حَدَّثَنَا مُحَمَّدُ بْنُ فُلَيْحٍ، قَالَ حَدَّثَنِي أَبِي قَالَ، حَدَّثَنِي هِلاَلُ بْنُ عَلِيٍّ، عَنْ عَطَاءِ بْنِ يَسَارٍ، عَنْ أَبِي هُرَيْرَةَ، قَالَ بَيْنَمَا النَّبِيُّ صلى الله عليه وسلم فِي مَجْلِسٍ يُحَدِّثُ الْقَوْمَ جَاءَهُ أَعْرَابِيٌّ فَقَالَ مَتَى السَّاعَةُ فَمَضَى رَسُولُ اللَّهِ صلى الله عليه وسلم يُحَدِّثُ، فَقَالَ بَعْضُ الْقَوْمِ سَمِعَ مَا قَالَ، فَكَرِهَ مَا قَالَ، وَقَالَ بَعْضُهُمْ بَلْ لَمْ يَسْمَعْ، حَتَّى إِذَا قَضَى حَدِيثَهُ قَالَ ‏"‏ أَيْنَ ـ أُرَاهُ ـ السَّائِلُ عَنِ السَّاعَةِ ‏"‏‏.‏ قَالَ هَا أَنَا يَا رَسُولَ اللَّهِ‏.‏ قَالَ ‏"‏ فَإِذَا ضُيِّعَتِ الأَمَانَةُ فَانْتَظِرِ السَّاعَةَ ‏"‏‏.‏ قَالَ كَيْفَ إِضَاعَتُهَا قَالَ ‏"‏ إِذَا وُسِّدَ الأَمْرُ إِلَى غَيْرِ أَهْلِهِ فَانْتَظِرِ السَّاعَةَ ‏"‏‏.‏'''
    #txt='''حَدَّثَنَا أَبُو النُّعْمَانِ، عَارِمُ بْنُ الْفَضْلِ قَالَ حَدَّثَنَا أَبُو عَوَانَةَ، عَنْ أَبِي بِشْرٍ، عَنْ يُوسُفَ بْنِ مَاهَكَ، عَنْ عَبْدِ اللَّهِ بْنِ عَمْرٍو، قَالَ تَخَلَّفَ عَنَّا النَّبِيُّ صلى الله عليه وسلم فِي سَفْرَةٍ سَافَرْنَاهَا، فَأَدْرَكَنَا وَقَدْ أَرْهَقَتْنَا الصَّلاَةُ وَنَحْنُ نَتَوَضَّأُ، فَجَعَلْنَا نَمْسَحُ عَلَى أَرْجُلِنَا، فَنَادَى بِأَعْلَى صَوْتِهِ ‏ "‏ وَيْلٌ لِلأَعْقَابِ مِنَ النَّارِ ‏"‏‏.‏ مَرَّتَيْنِ أَوْ ثَلاَثًا‏.‏'''

    #___2 sanad________
    #txt='''وَحَدَّثَنِي مُحَمَّدُ بْنُ سَهْلِ بْنِ عَسْكَرٍ التَّمِيمِيُّ، حَدَّثَنَا يَحْيَى بْنُ حَسَّانَ، ح وَحَدَّثَنَا عَبْدُ اللَّهِ بْنُ عَبْدِ الرَّحْمَنِ الدَّارِمِيُّ، أَخْبَرَنَا يَحْيَى، - وَهُوَ ابْنُ حَسَّانَ - حَدَّثَنَا مُعَاوِيَةُ، - يَعْنِي ابْنَ سَلاَّمٍ - حَدَّثَنَا زَيْدُ بْنُ سَلاَّمٍ، عَنْ أَبِي سَلاَّمٍ، قَالَ قَالَ حُذَيْفَةُ بْنُ الْيَمَانِ قُلْتُ يَا رَسُولَ اللَّهِ إِنَّا كُنَّا بِشَرٍّ فَجَاءَ اللَّهُ بِخَيْرٍ فَنَحْنُ فِيهِ فَهَلْ مِنْ وَرَاءِ هَذَا الْخَيْرِ شَرٌّ قَالَ نَعَمْ ‏.‏ قُلْتُ هَلْ وَرَاءَ ذَلِكَ الشَّرِّ خَيْرٌ قَالَ ‏"‏ نَعَمْ ‏"‏ ‏.‏ قُلْتُ فَهَلْ وَرَاءَ ذَلِكَ الْخَيْرِ شَرٌّ قَالَ ‏"‏ نَعَمْ ‏"‏ ‏.‏ قُلْتُ كَيْفَ قَالَ ‏"‏ يَكُونُ بَعْدِي أَئِمَّةٌ لاَ يَهْتَدُونَ بِهُدَاىَ وَلاَ يَسْتَنُّونَ بِسُنَّتِي وَسَيَقُومُ فِيهِمْ رِجَالٌ قُلُوبُهُمْ قُلُوبُ الشَّيَاطِينِ فِي جُثْمَانِ إِنْسٍ ‏"‏ ‏.‏ قَالَ قُلْتُ كَيْفَ أَصْنَعُ يَا رَسُولَ اللَّهِ إِنْ أَدْرَكْتُ ذَلِكَ قَالَ ‏"‏ تَسْمَعُ وَتُطِيعُ لِلأَمِيرِ وَإِنْ ضُرِبَ ظَهْرُكَ وَأُخِذَ مَالُكَ فَاسْمَعْ وَأَطِعْ ‏"‏ ‏.‏'''
    #txt='''حَدَّثَنَا عَمْرُو بْنُ عَلِيٍّ، حَدَّثَنَا ابْنُ مَهْدِيٍّ، ح وَحَدَّثَنَا مُحَمَّدُ بْنُ عَمْرِو بْنِ جَبَلَةَ، حَدَّثَنَا بِشْرُ بْنُ عُمَرَ، قَالاَ جَمِيعًا حَدَّثَنَا هِشَامُ بْنُ سَعْدٍ، عَنْ زَيْدِ بْنِ أَسْلَمَ، عَنْ أَبِيهِ، عَنِ ابْنِ عُمَرَ، عَنِ النَّبِيِّ صلى الله عليه وسلم بِمَعْنَى حَدِيثِ نَافِعٍ عَنِ ابْنِ عُمَرَ ‏.‏'''
    #______3 sanad_____
    #txt='''وَحَدَّثَنَا أَحْمَدُ بْنُ خِرَاشٍ، حَدَّثَنَا حَبَّانُ، حَدَّثَنَا أَبُو عَوَانَةَ، ح وَحَدَّثَنِي الْقَاسِمُ بْنُ زَكَرِيَّاءَ، حَدَّثَنَا عُبَيْدُ اللَّهِ بْنُ مُوسَى، عَنْ شَيْبَانَ، ح وَحَدَّثَنَا إِسْحَاقُ بْنُ إِبْرَاهِيمَ، أَخْبَرَنَا الْمُصْعَبُ بْنُ الْمِقْدَامِ الْخَثْعَمِيُّ، حَدَّثَنَا إِسْرَائِيلُ، ح وَحَدَّثَنِي حَجَّاجٌ، حَدَّثَنَا عَارِمُ بْنُ الْفَضْلِ، حَدَّثَنَا حَمَّادُ بْنُ زَيْدٍ، حَدَّثَنَا عَبْدُ اللَّهِ بْنُ الْمُخْتَارِ، وَرَجُلٌ، سَمَّاهُ كُلُّهُمْ عَنْ زِيَادِ بْنِ عِلاَقَةَ، عَنْ عَرْفَجَةَ، عَنِ النَّبِيِّ صلى الله عليه وسلم بِمِثْلِهِ غَيْرَ أَنَّ فِي حَدِيثِهِمْ جَمِيعًا ‏ "‏ فَاقْتُلُوهُ ‏"‏ ‏.'''

    contextList=[]
    nameList=[]
    finalName=[]

    WithoutAhrabTxt=""
    for  i in range(len(txt)):
        no=ord(txt[i])
        if(no==1614 or no==1615 or no==1616 or no==1618 or no==1617 or no==1612 or no==1613 or no==1611):
            continue
        else:
            WithoutAhrabTxt+=txt[i]
            
    print(WithoutAhrabTxt)

    sanadList =[]
    # txtList=WithoutAhrabTxt.split(" ")
    if(WithoutAhrabTxt.__contains__(" ح، ")):
        txtList=WithoutAhrabTxt.split(" ح، ")
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
    print(sanadList)
    
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
    # while("" in nameList) :
    #     sanadList.remove("")
        
    # #agr remove comma here than malik will be name 
    # sanadList =[name.replace("،","") for name in sanadList]
    
    # FinalList=[]
    # for i in range(len(sanadList)):
    #     if(sanadList[i] == "محمد صلی اللہ علیہ وآلہ وسلم"):
    #         FinalList.append(sanadList[i])
    #         break
    #     else:
    #         FinalList.append(sanadList[i])
    
    # return FinalList




#_________________________________________________________________________

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
    WordReplace=["حدثني","وحدثنا","حدثنا","نحوه","عن","قال","فقال","سمعت","يقول","أنه","سمع","أخبرني","مولى","أن","أخبرنا","اخبرنا","سال","قالت","قالا","جميعا","قلت","أنها","وحدثني","أخبره","في حديثه","يخطب","تابعه","إنه","انه","كثيرا","قال:","أنبأنا","أحدثكم","إذا","قام","فكتب","يحدث","فقلت","قالوا","وقد","روى","هذا","الحديث","حدثكم","من","كتب","وعن","زوج","ولقد","يذكر","سألني","فكان","إلى","لما","قدم","أشياء","بهذا","رأيت","أقبلت","رواية","قال،","قراءة","وأنا","إن","أسمع","حدثه","بأى","حديثا","كان",'كنت',"اخبرني","يحدثونه","حدثتني","شىء","أسمع","وغير","واحد","وأخبرني"]



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
    
    
    return narratorsNameList




#_______________Main Code___________

finalNarratorsNameList=[]


import pandas as pd 
df = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/copied fyp/HadithFromDifferentBooks.xlsx")
df

hadithList = df.HadithText

for i in range(len(hadithList)):
    
    if(hadithList[i].__contains__(" ح ") or hadithList[i].__contains__(" ح، ")):
        return_M_List= multipleSanads(hadithList[i])
        finalNarratorsNameList.append(return_M_List)
    else:
        return_S_List = singleSanad(hadithList[i])
        finalNarratorsNameList.append(return_S_List)
        
        
        

# dfN = pd.DataFrame()
# dfN["NameFromRuleBase"] = finalNarratorsNameList
# dfN.to_excel("NameOfNarrator_FromRuleBased.xlsx")

#####################################################################
#  Comparison 

df_comp_R_with_E = pd.read_excel("C:/Users/iammu/OneDrive/Desktop/copied fyp/Names and Length Comparison btw Rule_Based and Exact.xlsx")

testFinal_E_NameList=[]


eNameList = df_comp_R_with_E['Exact Names']

for i in range(len(eNameList)):
    dum=[]
    if(eNameList[i].count('[') == 1):
        index_S_NameList=[]
        eNameList[i]=eNameList[i].replace("[","")
        eNameList[i]=eNameList[i].replace("]","")
        dum = eNameList[i].split(",")
        for j in range(len(dum)):
            dum[j]= dum[j].strip()
            if((dum[j][0] and dum[j][-1]) =="'"):
                dum[j]= dum[j].replace("'","")
                
                if(dum[j].__contains__("-")):
                    dum[j]= dum[j].replace("-","")
                    dum[j]= dum[j].strip()
                if(dum[j].__contains__("ـ")):
                    dum[j]= dum[j].replace("ـ","")
                    dum[j]= dum[j].strip()
                if(dum[j].__contains__("،")):
                    dum[j]= dum[j].replace("،","")
                    dum[j]= dum[j].strip()
                dum[j]= dum[j].strip()
                index_S_NameList.append(dum[j])
    if(len(index_S_NameList)!=0):
        testFinal_E_NameList.append(index_S_NameList)
        index_S_NameList=[]
    MList=[]
    if(eNameList[i].count('[') == 3):     
        eNameList[i]= eNameList[i].replace("[","")
        if((eNameList[i][-1] and eNameList[i][-2]) == "]"):
            eNameList[i] = eNameList[i][:-3]
            dum = eNameList[i].split("]")
            for ii in range(len(dum)):
                dum1=[]
                index_M_NameList=[]
                dum1 = dum[ii].split(",")
                for j in range(len(dum1)): 
                    dum1[j]= dum1[j].strip()
                    dum1[j]= dum1[j].replace("'","")
                    if(dum1[j].__contains__("-")):
                        dum1[j]= dum1[j].replace("-","")
                        dum1[j]= dum1[j].strip()
                    if(dum1[j].__contains__("ـ")):
                        dum1[j]= dum1[j].replace("ـ","")
                        dum1[j]= dum1[j].strip()
                    if(dum1[j].__contains__("،")):
                        dum1[j]= dum1[j].replace("،","")
                        dum1[j]= dum1[j].strip()
                    dum1[j]= dum1[j].strip()
                    if(dum1[j] !=""):
                        index_M_NameList.append(dum1[j])
            
                MList.append(index_M_NameList)   
    if(len(MList)!=0):
        testFinal_E_NameList.append(MList)




rPresentName_final_E_NameList = []

rAbsentName_final_E_NameList = []

length_rPresentName_final_E_NameList = []

length_rAbsentName_final_E_NameList = []

for i in range(len(finalNarratorsNameList)):
    first_index = finalNarratorsNameList[i]
    if(type(first_index[0])==list):
        presentLength = ""
        absentLength = ""
        dummy_multiplePresentName = []
        dummy_multipleAbsentName = []
        for j in range(len(first_index)):
            dummy_presentName = []
            dummy_absentName = []
            for name1 in first_index[j]:
                if(name1 in testFinal_E_NameList[i][j]):
                    dummy_presentName.append(name1)
                else:
                    dummy_absentName.append(name1)
            if(len(dummy_presentName)!=0):
                dummy_multiplePresentName.append(dummy_presentName)
                if(j!=len(first_index)-1):
                    presentLength = presentLength +str(len(dummy_presentName)) + ", "
                else:
                    presentLength = presentLength +str(len(dummy_presentName))
            else:
                dummy_multiplePresentName.append("No Name Present")
                if(j!=len(first_index)-1):
                    presentLength = presentLength + "0" + ", "
                else:
                    presentLength = presentLength + "0" 
                
            if(len(dummy_absentName)!=0):
                dummy_multipleAbsentName.append(dummy_absentName)
                if(j!=len(first_index)-1):
                    absentLength = absentLength +str(len(dummy_absentName)) + ", "
                else:
                    absentLength = absentLength +str(len(dummy_absentName)) 
            else:
                dummy_multipleAbsentName.append("No Name Absent")
                if(j!=len(first_index)-1):
                    absentLength = absentLength + "0" + ", "
                else:
                    absentLength = absentLength + "0" 
        rPresentName_final_E_NameList.append(dummy_multiplePresentName)
        rAbsentName_final_E_NameList.append(dummy_multipleAbsentName)
        length_rPresentName_final_E_NameList.append(presentLength)
        length_rAbsentName_final_E_NameList.append(absentLength)
    else:
        dummy_presentName = []
        dummy_absentName = []
        for name in first_index:
            if(name in testFinal_E_NameList[i]):
                dummy_presentName.append(name)
            else:
                dummy_absentName.append(name)
        if(len(dummy_presentName)!=0):
            rPresentName_final_E_NameList.append(dummy_presentName)
            length_rPresentName_final_E_NameList.append(len(dummy_presentName))
        else:
            rPresentName_final_E_NameList.append("No Name Present")
            length_rPresentName_final_E_NameList.append(0)
            
        if(len(dummy_absentName)!=0):
            rAbsentName_final_E_NameList.append(dummy_absentName)
            length_rAbsentName_final_E_NameList.append(len(dummy_absentName))
        else:
            rAbsentName_final_E_NameList.append("No Name Absent")
            length_rAbsentName_final_E_NameList.append(0)




# dfDum = pd.DataFrame()
# dfDum["Exact Names"] = testFinal_E_NameList
# dfDum["RuleBased Names"] = finalNarratorsNameList
# dfDum["Name Present in Rule-Based"] = rPresentName_final_E_NameList
# dfDum["Length of Present Names"] = length_rPresentName_final_E_NameList
# dfDum["Name Absent in Rule-Based"] = rAbsentName_final_E_NameList
# dfDum["Length of Absent Names"] = length_rAbsentName_final_E_NameList

# dfDum.to_excel("Compare Exact With Rule Based After removing RA.xlsx")

dfCheck = pd.read_excel("NameCheckWithNER.xlsx")
checkName = dfCheck.Names
checkNameList=[]
for i in range(len(checkName)):
    dum=[]
    if(checkName[i].count('[') == 1):
        index_S_NameList=[]
        checkName[i]=checkName[i].replace("[","")
        checkName[i]=checkName[i].replace("]","")
        dum = checkName[i].split(",")
        for j in range(len(dum)):
            dum[j]= dum[j].strip()
            if((dum[j][0] and dum[j][-1]) =="'"):
                dum[j]= dum[j].replace("'","")
                
                if(dum[j].__contains__("-")):
                    dum[j]= dum[j].replace("-","")
                    dum[j]= dum[j].strip()
                if(dum[j].__contains__("ـ")):
                    dum[j]= dum[j].replace("ـ","")
                    dum[j]= dum[j].strip()
                if(dum[j].__contains__("،")):
                    dum[j]= dum[j].replace("،","")
                    dum[j]= dum[j].strip()
                dum[j]= dum[j].strip()
                index_S_NameList.append(dum[j])
    if(len(index_S_NameList)!=0):
        checkNameList.append(index_S_NameList)
        index_S_NameList=[]
    MList=[]
    if(checkName[i].count('[') == 3):     
        checkName[i]= checkName[i].replace("[","")
        if((checkName[i][-1] and checkName[i][-2]) == "]"):
            checkName[i] = checkName[i][:-3]
            dum = checkName[i].split("]")
            for ii in range(len(dum)):
                dum1=[]
                index_M_NameList=[]
                dum1 = dum[ii].split(",")
                for j in range(len(dum1)): 
                    dum1[j]= dum1[j].strip()
                    dum1[j]= dum1[j].replace("'","")
                    if(dum1[j].__contains__("-")):
                        dum1[j]= dum1[j].replace("-","")
                        dum1[j]= dum1[j].strip()
                    if(dum1[j].__contains__("ـ")):
                        dum1[j]= dum1[j].replace("ـ","")
                        dum1[j]= dum1[j].strip()
                    if(dum1[j].__contains__("،")):
                        dum1[j]= dum1[j].replace("،","")
                        dum1[j]= dum1[j].strip()
                    dum1[j]= dum1[j].strip()
                    if(dum1[j] !=""):
                        index_M_NameList.append(dum1[j])
            
                MList.append(index_M_NameList)   
    if(len(MList)!=0):
        checkNameList.append(MList)



from camel_tools.ner import NERecognizer

ner = NERecognizer('CAMeL-Lab/bert-base-arabic-camelbert-mix-ner')

finalNameCheckFromNER=[]
for i in range(len(checkNameList)):
    sent_split = checkNameList[i]
    # for j in range(len(checkNameList[i])):
        
        
    splitWord=[]
    for i in range(len(sent_split)):
        splitWord.append(sent_split[i].split())
        
    nameList=[]
    for i in range(len(splitWord)):
        label=ner.predict_sentence(splitWord[i])
        print(list(zip(splitWord[i],label)))
        
        #New Code and comment the below RAsool name
        # if(sent_split[i].__contains__('النبي صلى الله عليه وسلم') or sent_split[i].__contains__('رسول الله صلى الله عليه وسلم')):
            
        #     nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
        #     count=1
        #     break
        
        dum=''
        for j in range(len(label)):
            if (label[j]=="B-PERS" or label[j]=="I-PERS"):
                dum =dum+splitWord[i][j]+' '
            else:
                if(dum !=''):
                    nameList.append(dum)
                    dum=''
                #Hear From Father Mother Etc
                
                if(splitWord[i][j]=="أبيه"):
                    nameList.append("أبيه")
                    
                if(splitWord[i][j]=="أبي"):
                    nameList.append("أبي")
                    
                # #Rasool Name Recong From Tokens
                    
                if(sent_split[i] =="محمد صلی اللہ علیہ وآلہ وسلم"):
                    # if(splitWord[i][j+1]=='صلى' and splitWord[i][j+2]=='الله' and splitWord[i][j+3]=='علیہ' and splitWord[i][j+4]=='وآلہ' and splitWord[i][j+5]=='وسلم'):
                    nameList.append("محمد صلی اللہ علیہ وآلہ وسلم")
                        # count=1
                    break
                    
                    print(dum)
        # if(count==1):
        #     break
        
        nameList.append(dum)
        dum=''
        
        while("" in nameList) :
            nameList.remove("")
            
    finalNameCheckFromNER.append(nameList)
        
dfCheck["NameFromNER"] = finalNameCheckFromNER
