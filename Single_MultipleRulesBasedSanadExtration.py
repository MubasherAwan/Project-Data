# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 10:35:45 2022

@author: iammu
"""

def multipleSanads(txt):
    WordReplace=["حدثني","وحدثنا","حدثنا","نحوه","عن","قال","فقال","سمعت","يقول","أنه","سمع","أخبرني","مولى","أن","أخبرنا","اخبرنا","سال","قالت","قالا","جميعا","قلت","وحدثني","في حديثه","تابعه","انه","اخبرني","وأخبرني"]

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
    prophetNamesReplacerList = ["رسول الله صلى الله عليه وسلم","النبي ـ صلى الله عليه وسلم" ,"النبي صلى الله عليه وسلم", "يا رسول الله","محمد صلی اللہ علیہ وآلہ وسلم"]

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
    return sanadList




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
    WordReplace = ["حدثني", "في" , "أنها" , "وحدثنا", "حدثنا", "أنبأنا","ـ", "نحوه", "عن", "قال", "فقال", "سمعت", "يقول", "أنه", "سمع", "أخبرني",
                           "مولى", "أخبرنا", "اخبرنا", "سال", "أن", "قالت", ":", "في حديثه", "تابعه", "أخبره", "ان", "انه",
                           "اخبرني", "وحدثني", "وأخبرني"]


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
    prophetNamesReplacerList = ["رسول الله صلى الله عليه وسلم","النبي ـ صلى الله عليه وسلم" ,"النبي صلى الله عليه وسلم", "يا رسول الله",
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
        narratorsNameList[i] = narratorsNameList[i].replace("ـ رضى الله عنهما ـ", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنها", "")
        narratorsNameList[i] = narratorsNameList[i].replace("رضي الله عنه", "")
        narratorsNameList[i] = narratorsNameList[i].replace("على المنبر", "")
        narratorsNameList[i] = narratorsNameList[i].strip()
    return narratorsNameList




#_______________Main Code___________

finalNarratorsNameList=[]

hadithList = ['''حَدَّثَنَا مُحَمَّدُ بْنُ سِنَانٍ، قَالَ حَدَّثَنَا فُلَيْحٌ، ح وَحَدَّثَنِي إِبْرَاهِيمُ بْنُ الْمُنْذِرِ، قَالَ حَدَّثَنَا مُحَمَّدُ بْنُ فُلَيْحٍ، قَالَ حَدَّثَنِي أَبِي قَالَ، حَدَّثَنِي هِلاَلُ بْنُ عَلِيٍّ، عَنْ عَطَاءِ بْنِ يَسَارٍ، عَنْ أَبِي هُرَيْرَةَ، قَالَ بَيْنَمَا النَّبِيُّ صلى الله عليه وسلم فِي مَجْلِسٍ يُحَدِّثُ الْقَوْمَ جَاءَهُ أَعْرَابِيٌّ فَقَالَ مَتَى السَّاعَةُ فَمَضَى رَسُولُ اللَّهِ صلى الله عليه وسلم يُحَدِّثُ، فَقَالَ بَعْضُ الْقَوْمِ سَمِعَ مَا قَالَ، فَكَرِهَ مَا قَالَ، وَقَالَ بَعْضُهُمْ بَلْ لَمْ يَسْمَعْ، حَتَّى إِذَا قَضَى حَدِيثَهُ قَالَ ‏"‏ أَيْنَ ـ أُرَاهُ ـ السَّائِلُ عَنِ السَّاعَةِ ‏"‏‏.‏ قَالَ هَا أَنَا يَا رَسُولَ اللَّهِ‏.‏ قَالَ ‏"‏ فَإِذَا ضُيِّعَتِ الأَمَانَةُ فَانْتَظِرِ السَّاعَةَ ‏"‏‏.‏ قَالَ كَيْفَ إِضَاعَتُهَا قَالَ ‏"‏ إِذَا وُسِّدَ الأَمْرُ إِلَى غَيْرِ أَهْلِهِ فَانْتَظِرِ السَّاعَةَ ‏"‏‏.‏'''
,'''وَحَدَّثَنِي مُحَمَّدُ بْنُ سَهْلِ بْنِ عَسْكَرٍ التَّمِيمِيُّ، حَدَّثَنَا يَحْيَى بْنُ حَسَّانَ، ح وَحَدَّثَنَا عَبْدُ اللَّهِ بْنُ عَبْدِ الرَّحْمَنِ الدَّارِمِيُّ، أَخْبَرَنَا يَحْيَى، - وَهُوَ ابْنُ حَسَّانَ - حَدَّثَنَا مُعَاوِيَةُ، - يَعْنِي ابْنَ سَلاَّمٍ - حَدَّثَنَا زَيْدُ بْنُ سَلاَّمٍ، عَنْ أَبِي سَلاَّمٍ، قَالَ قَالَ حُذَيْفَةُ بْنُ الْيَمَانِ قُلْتُ يَا رَسُولَ اللَّهِ إِنَّا كُنَّا بِشَرٍّ فَجَاءَ اللَّهُ بِخَيْرٍ فَنَحْنُ فِيهِ فَهَلْ مِنْ وَرَاءِ هَذَا الْخَيْرِ شَرٌّ قَالَ نَعَمْ ‏.‏ قُلْتُ هَلْ وَرَاءَ ذَلِكَ الشَّرِّ خَيْرٌ قَالَ ‏"‏ نَعَمْ ‏"‏ ‏.‏ قُلْتُ فَهَلْ وَرَاءَ ذَلِكَ الْخَيْرِ شَرٌّ قَالَ ‏"‏ نَعَمْ ‏"‏ ‏.‏ قُلْتُ كَيْفَ قَالَ ‏"‏ يَكُونُ بَعْدِي أَئِمَّةٌ لاَ يَهْتَدُونَ بِهُدَاىَ وَلاَ يَسْتَنُّونَ بِسُنَّتِي وَسَيَقُومُ فِيهِمْ رِجَالٌ قُلُوبُهُمْ قُلُوبُ الشَّيَاطِينِ فِي جُثْمَانِ إِنْسٍ ‏"‏ ‏.‏ قَالَ قُلْتُ كَيْفَ أَصْنَعُ يَا رَسُولَ اللَّهِ إِنْ أَدْرَكْتُ ذَلِكَ قَالَ ‏"‏ تَسْمَعُ وَتُطِيعُ لِلأَمِيرِ وَإِنْ ضُرِبَ ظَهْرُكَ وَأُخِذَ مَالُكَ فَاسْمَعْ وَأَطِعْ ‏"‏ ‏.‏'''
,'''حَدَّثَنَا الْحُمَيْدِيُّ عَبْدُ اللَّهِ بْنُ الزُّبَيْرِ ، قَالَ : حَدَّثَنَا سُفْيَانُ ، قَالَ : حَدَّثَنَا يَحْيَى بْنُ سَعِيدٍ الْأَنْصَارِيُّ ، قَالَ : أَخْبَرَنِي مُحَمَّدُ بْنُ إِبْرَاهِيمَ التَّيْمِيُّ ، أَنَّهُ سَمِعَ عَلْقَمَةَ بْنَ وَقَّاصٍ اللَّيْثِيَّ ، يَقُولُ : سَمِعْتُ عُمَرَ بْنَ الْخَطَّابِ رَضِيَ اللَّهُ عَنْهُ عَلَى الْمِنْبَرِ، قَالَ : سَمِعْتُ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ، يَقُولُ : " إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى، فَمَنْ كَانَتْ هِجْرَتُهُ إِلَى دُنْيَا يُصِيبُهَا أَوْ إِلَى امْرَأَةٍ يَنْكِحُهَا، فَهِجْرَتُهُ إِلَى مَا هَاجَرَ إِلَيْهِ "'''

]

for i in range(len(hadithList)):
    if(hadithList[i].__contains__(" ح ")):
        return_M_List= multipleSanads(hadithList[i])
        finalNarratorsNameList.append(return_M_List)
    else:
        return_S_List = singleSanad(hadithList[i])
        finalNarratorsNameList.append(return_S_List)
        
    









