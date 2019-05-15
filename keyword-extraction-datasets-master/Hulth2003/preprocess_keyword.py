import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer

def wordNetTags(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('N'):
        return wordnet.NOUN
    else:
        return wordnet.NOUN

lmtizer = WordNetLemmatizer()
for file in os.listdir("./Training/"):
    if file.split(".")[1]=="uncontr":
        with open("./Training/"+file) as f:
            temp=f.read()
        temp=temp.split(";")
        temp=[x.strip() for x in temp]
        for i in range(len(temp)):
            temp[i]=nltk.pos_tag(word_tokenize(temp[i]))
            #print(temp[i])
            for idx in range(len(temp[i])):
                temp[i][idx] = lmtizer.lemmatize(temp[i][idx][0], wordNetTags(temp[i][idx][1])).lower()
            temp[i] = " ".join(temp[i])
        with open("./keys/"+file.split(".")[0]+".key","w") as f:
            for i in temp:
                f.write(str(i)+"\n")
    if file.split(".")[1]=="abstr":
        with open("./Training/"+file) as f:
            temp=f.read()
        temp=temp.split("\n")
        temp=[x.strip() for x in temp]
        temp=" ".join(temp)
        with open("./documents/"+file.split(".")[0]+".txt","w") as f:
            f.write(temp)