import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from textblob import TextBlob
from keras.models import load_model
import os
model = load_model(os.getcwd()+'\TextProcessing\model.h5')
import json
import random
intents = json.loads(open(os.getcwd()+'\TextProcessing\intents.json').read())
words = pickle.load(open(os.getcwd()+'\TextProcessing\words.pkl','rb'))
classes = pickle.load(open(os.getcwd()+'\TextProcessing\classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words



def bag_of_words(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,word in enumerate(words):
            if word == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % word)
    return(np.array(bag))

def predict_class(sentence):
    p = bag_of_words(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    if (ints):
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break
        return result
    else:
        return "Sorry Data Not Available"
        

def autocorrect(msg2):
    text=TextBlob(msg2)
    msg2=str(text.correct())
    return msg2

def resultGeneration(msg):
    ints = predict_class(msg)
    res = getResponse(ints, intents)
    return res


