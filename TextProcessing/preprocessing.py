import nltk     

from nltk.stem import WordNetLemmatizer

nltk.download('popular',quiet=True) 

nltk.download('punkt')    
                        
nltk.download('wordnet')        
                                
lemmatizer = WordNetLemmatizer()
import json

intents_file = open('intents.json').read()
intents = json.loads(intents_file) 

words=[]
classes = []
documents = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        documents.append((word, intent['tag']))
       
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(words)

words = [lemmatizer.lemmatize(w.lower()) for w in words]    
words = (list(set(words)))
# sort classes
classes = sorted(list(set(classes)))
print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique lemmatized words", words)

import pickle

pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))               

training = []      

output_empty = [0] * len(classes)      

for doc in documents:                   
    
    bag = []                            
    
    pattern_words = doc[0]              
    
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]      
   
    for word in words:                      
        bag.append(1) if word in pattern_words else bag.append(0)
        
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag, output_row])       
    
import random

import numpy as np

random.shuffle(training)             
training = np.array(training)     
train_x = list(training[:,0])        
train_y = list(training[:,1])
print("Training data created")

                                                                        
from keras.models import Sequential

from keras.layers import Dense, Activation, Dropout

from keras.optimizers import SGD

model = Sequential()    
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))        
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))                                         
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))                         


sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)       	  
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])


fitting = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)          
model.save('model.h5', fitting)

print("model created")





































