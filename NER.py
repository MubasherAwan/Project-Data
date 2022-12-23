# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:13:36 2022

@author: iammu
"""
from camel_tools.ner import NERecognizer

ner = NERecognizer.pretrained()
#sentence='حدثنا الحميدي عبد الله بن الزبير ، قال : حدثنا سفيان ، قال : حدثنا يحيى بن سعيد الانصاري ، قال : اخبرني محمد بن ابراهيم التيمي ، انه سمع علقمة بن وقاص الليثي ، يقول : سمعت عمر بن الخطاب رضي الله عنه على المنبر ، قال : سمعت رسول الله صلى الله عليه وسلم ، يقول :    انما الاعمال بالنيات ، وانما لكل امرئ ما نوى ، فمن كانت هجرته الى دنيا يصيبها او الى امراة ينكحها ، فهجرته الى ما هاجر اليه'.slpit()
test="حدثني يحيى بن أيوب، وقتيبة بن سعيدٍ، جميعًا عن إسماعيل بن جعفرٍ، عن أبي سهيلٍ، عن أبيه، عن طلحة بن عبيد الله، عن النبي صلى الله عليه وسلم بهذا الحديث نحو حديث مالكٍ غير أنه قال فقال رسول الله صلى الله عليه وسلم ‏ أفلح وأبيه إن صدق ‏ ‏.‏ أو ‏ دخل الجنة وأبيه إن صدق"

label=ner.predict_sentence(test)

from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("CAMeL-Lab/bert-base-arabic-camelbert-mix-ner")

model = AutoModelForTokenClassification.from_pretrained("CAMeL-Lab/bert-base-arabic-camelbert-mix-ner")


from camel_tools.ner import NERecognizer
from camel_tools.tokenizers.word import simple_word_tokenize
ner = NERecognizer('CAMeL-Lab/bert-base-arabic-camelbert-mix-ner')

test="حدثني يحيى بن أيوب، وقتيبة بن سعيدٍ، جميعًا عن إسماعيل بن جعفرٍ، عن أبي سهيلٍ، عن أبيه، عن طلحة بن عبيد الله، عن النبي صلى الله عليه وسلم بهذا الحديث نحو حديث مالكٍ غير أنه قال فقال رسول الله صلى الله عليه وسلم ‏ أفلح وأبيه إن صدق ‏ ‏.‏ أو ‏ دخل الجنة وأبيه إن صدق"
#test='حدثنا عبدان، قال أخبرنا عبد الله، قال أخبرنا يونس، عن الزهري، ح وحدثنا بشر بن محمد، قال أخبرنا عبد الله، قال أخبرنا يونس، ومعمر، عن الزهري، نحوه قال أخبرني عبيد الله بن عبد الله، عن ابن عباس، قال كان رسول الله صلى الله عليه وسلم أجود الناس، وكان أجود ما يكون في رمضان حين يلقاه جبريل، وكان يلقاه في كل ليلة من رمضان فيدارسه القرآن، فلرسول الله صلى الله عليه وسلم أجود بالخير من الريح المرسلة‏.‏'

sentence = simple_word_tokenize(test)
dum=ner.predict_sentence(sentence)


test='''حدثنا أبو اليمان، قال أخبرنا شعيب، عن الزهري، قال أخبرني سالم بن عبد الله، أن عبد الله بن عمر، قال أخذ عمر جبة من إستبرق تباع في السوق، فأخذها فأتى رسول الله صلى الله عليه وسلم فقال يا رسول الله ابتع هذه تجمل بها للعيد والوفود‏.‏ فقال له رسول الله صلى الله عليه وسلم ‏"‏ إنما هذه لباس من لا خلاق له ‏"‏‏.‏ فلبث عمر ما شاء الله أن يلبث، ثم أرسل إليه رسول الله صلى الله عليه وسلم بجبة ديباج، فأقبل بها عمر، فأتى بها رسول الله صلى الله عليه وسلم فقال يا رسول الله إنك قلت ‏"‏ إنما هذه لباس من لا خلاق له ‏"‏‏.‏ وأرسلت إلى بهذه الجبة فقال له رسول الله صلى الله عليه وسلم ‏"‏ تبيعها أو تصيب بها حاجتك '''

test="أبو اليمان"

from transformers import pipeline
ner = pipeline('ner', model='CAMeL-Lab/bert-base-arabic-camelbert-mix-ner')
dummy1 = ner(test)


append_name=''
name_list=[]
for i in range(len(dummy1)):
    if(dummy1[i].get('entity')=='B-PERS'):
        if(append_name==''):
            append_name=dummy1[i].get('word')
        else:
            name_list.append(append_name)
            append_name=dummy1[i].get('word')
    
    if(dummy1[i].get('entity')=='I-PERS'):
        append_name=append_name+' '+dummy1[i].get('word')
        if(i==len(dummy1)-1):
            name_list.append(append_name)
        
    if(dummy1[i].get('entity')=='B-MISC'):
        if(append_name!=''):
            name_list.append(append_name)
            append_name=''
            
len(dummy1)


dummy="حدثنا الحميدي عبد الله بن الزبير ، قال : حدثنا سفيان ، قال : حدثنا يحيى بن سعيد الانصاري ، قال : اخبرني محمد بن ابراهيم التيمي ، انه سمع علقمة بن وقاص الليثي ، يقول : سمعت عمر بن الخطاب رضي الله عنه على المنبر ، قال : سمعت رسول الله صلى الله عليه وسلم ، يقول :    انما الاعمال بالنيات ، وانما لكل امرئ ما نوى ، فمن كانت هجرته الى دنيا يصيبها او الى امراة ينكحها ، فهجرته الى ما هاجر اليه"
dummy[6:32]

    
    