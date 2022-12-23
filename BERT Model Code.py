# -*- coding: utf-8 -*-
"""test (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iW8ea7mZpST2njA5MAacSrMz3Gz36yMF
"""

import pandas as pd
df = pd.read_excel('/content/SahihAhadith2400.xlsx')
df.dropna(inplace=True)

df.head()

from google.colab import drive
drive.mount("/content/drive")

a = df['status'].sort_values().unique()
a

df.shape

df['status'].sort_values().value_counts().plot(kind='bar')

import numpy as np
seq_len =110
num_samles = len (df)
num_samles

!pip install transformers
from transformers import BertTokenizer

lst = df['isnad'].tolist()

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

#toks = tokenizer(df['Review'].tolist(),max_length=seq_len,truncation=True, padding='max_length',add_special_tokens=True, return_tensors='np')
tokens = tokenizer(lst, max_length=seq_len, truncation=True,padding='max_length', add_special_tokens=True,return_tensors='np')

tokens.keys()

tokens['input_ids'].shape

arr = df['status'].values
#print (arr[:50])

a = pd.get_dummies(df['status'])

arr.shape

arr = a.values

type(arr)
#arr[11:15]

import tensorflow as tf
dataset = tf.data.Dataset.from_tensor_slices((tokens['input_ids'], tokens['attention_mask'], arr))
dataset.take(1)

def map_func(input_ids, masks, labels):
    # we convert our three-item tuple into a two-item tuple where the input item is a dictionary
    return {'input_ids': input_ids, 'attention_mask': masks}, labels

# then we use the dataset map method to apply this transformation
dataset = dataset.map(map_func)

dataset.take(1)

batch_size = 32

dataset = dataset.shuffle(10000).batch(batch_size, drop_remainder=True)

dataset.take(1)

split = 0.95

# we need to calculate how many batches must be taken to create 90% training set
size = int((tokens['input_ids'].shape[0] / batch_size) * split)

size

train_ds = dataset.take(size)
val_ds = dataset.skip(size)

# free up memory
# del dataset

tf.data.experimental.save(train_ds, 'train')
tf.data.experimental.save(val_ds, 'val')
val_ds.element_spec == train_ds.element_spec

import tensorflow as tf
ds = tf.data.experimental.load('train', element_spec=train_ds.element_spec)

from transformers import TFAutoModel

bert = TFAutoModel.from_pretrained('bert-base-cased')

import tensorflow as tf

# two input layers, we ensure layer name variables match to dictionary keys in TF dataset
input_ids = tf.keras.layers.Input(shape=(110,), name='input_ids', dtype='int32')
mask = tf.keras.layers.Input(shape=(110,), name='attention_mask', dtype='int32')

df.shape

# we access the transformer model within our bert object using the bert attribute (eg bert.bert instead of bert)
embeddings = bert.bert(input_ids, attention_mask=mask)[1]  # access final activations (alread max-pooled) [1]
# convert bert embeddings into 5 output classes
x = tf.keras.layers.Dense(300, activation='relu')(embeddings)
y = tf.keras.layers.Dense(2, activation='softmax', name='outputs')(x)

# initialize model
model = tf.keras.Model(inputs=[input_ids, mask], outputs=y)

# (optional) freeze bert layer
model.layers[2].trainable = True

# print out model summary
model.summary()

optimizer = tf.keras.optimizers.Adam(learning_rate=1e-5, decay=1e-6)
loss = tf.keras.losses.CategoricalCrossentropy()
acc = tf.keras.metrics.CategoricalAccuracy('accuracy')

model.compile(optimizer=optimizer, loss=loss, metrics=[acc])

element_spec = ({'input_ids': tf.TensorSpec(shape=(32, 110), dtype=tf.int64, name=None),
                 'attention_mask': tf.TensorSpec(shape=(32, 110), dtype=tf.int64, name=None)},
                tf.TensorSpec(shape=(32, 2), dtype=tf.uint8, name=None))

# load the training and validation sets
train_ds = tf.data.experimental.load('train', element_spec=element_spec)
val_ds = tf.data.experimental.load('val', element_spec=element_spec)

# view the input format
train_ds.take(1)

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=20
)

model.save('Hadithsentiment2400_model')

!zip -r /content/model2400.zip /content/Hadithsentiment2400_model

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/content/gdrive')
# %cp /content/model2400.zip /content/gdrive/My\ Drive

import tensorflow as tf

model = tf.keras.models.load_model('/content/Hadithsentiment2400_model')

# view model architecture to confirm we have save and loaded correctly
#model.summary()

!pip install transformers
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

def prep_data(text):
    tokens = tokenizer.encode_plus(text, max_length=110,
                                   truncation=True, padding='max_length',
                                   add_special_tokens=True, return_token_type_ids=False,
                                   return_tensors='tf')
    # tokenizer returns int32 tensors, we need to return float64, so we use tf.cast
    return {'input_ids': tf.cast(tokens['input_ids'], tf.int64),
            'attention_mask': tf.cast(tokens['attention_mask'], tf.int64)}

# probs = model.predict(prep_data(" clicking on next crahses the app"))[0]
# import numpy as np
# print (probs)
# i = np.argmax(probs)
# classes = ['صحيح', 'ضعيف']
# print (i, classes[i], probs[i])

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

# so we can see full phrase

df = pd.read_excel ('/content/Testing600Hadith.xlsx')
df = df.dropna()
df.head()

#classes = ['Angry', 'Bug Report', 'Comparison', 'Crash', 'Experience', 'Fake',
#       'Happy', 'Limitation', 'Negation', 'Negative', 'Neutral', 'Other',
#       'Other^^^^Question', 'Other^^^^expectation', 'Other^^^^hope',
#       'Positive', 'Question', 'Request', 'Sad', 'Sarcasm', 'Sarcism',
#       'Security Concern', 'Suggestion', 'Thwarting', 'nan']
classes = ['صحيح', 'ضعيف']
df['Prob'] = None
df['PSentiment'] = None

df['sname'] = None
df['match'] = None
mat =0
nmat =0

for i, row in df.iterrows():
    #print(i)
    # get token tensors
    tokens = prep_data(row['isnad'])
    # get probabilities
    probs = model.predict(tokens)
    # find argmax for winning class
    pred = np.argmax(probs)
    #print (probs[0][9])
    # add to dataframe
  
    df.at[i, 'PSentiment'] = pred
    df.at[i, 'Prob'] = probs[0] [pred]
    df.at[i, 'sname'] = classes[pred]

    if (row['status']==classes[pred]):
         df.at[i, 'match'] =1
         mat=mat+1
    else:
         df.at[i, 'match'] =0
         nmat = nmat+1
    print (mat, nmat)
df.to_csv("predicted.csv",  encoding='utf-8')
acc = mat/(mat+nmat)
print ('accuracy = ',acc)
df.head()

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/content/gdrive')
# %cp /content/model2400.zip /content/gdrive/My\ Drive

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/content/gdrive')
# %cp /content/gdrive/My\ Drive/model14.zip /content/savedmodel.zip

!unzip savedmodel.zip
