#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:03:11 2018

@author: rakadalal
"""
import csv
import re
import codecs
import nltk
from nltk.tag.stanford import StanfordNERTagger

def positive_seed(filename1,filename2, entity1, entity2):
    count=0
    fh = open(filename2, "w")
    string="e1:"+entity1
    fh.writelines(string+"\n")
    string="e2:"+entity2
    fh.writelines(string+"\n")
    fh.writelines("\n")
    file = open(filename1, 'r')
    reader = csv.reader(file)
    for row in reader:
        if len(row)==0:
            continue
        if count == 0:
            count+=1
            continue
        
        tup=row[2]+";"+row[3]
        fh.writelines(tup+"\n")
        
def negative_seed(filename1,filename2, entity1, entity2):
    count=0
    fh = open(filename2, "w")
    string="e1:"+entity1
    fh.writelines(string+"\n")
    string="e2:"+entity2
    fh.writelines(string+"\n")
    fh.writelines("\n")
    file = open(filename1, 'r')
    reader = csv.reader(file)
    for row in reader:
        if len(row)==0:
            continue
        if count == 0:
            count+=1
            continue
        
        tup=row[2]+";"+row[3]
        fh.writelines(tup+"\n")
        
def read_corpus_to_list(filename):
    corpus = []
    file = codecs.open(filename, 'r', encoding='utf-8')
    reader = csv.reader(file)
    counter=0
    for row in reader:
        if len(row) == 0:
            continue
        counter+=1
        if counter<=30:
            continue
        if counter==130:
            break
        tup = (row[0], row[1])
        corpus.append(tup)
        
    return corpus

def ner_tagger(text,st):
    regex=re.compile("([A-Z][a-z]+[\s][\d]([\d]?)(\,)*[\s]+[\d]+)")
    regex2=re.compile("([\d]([\d]?)[\s][A-Z][a-z]+(\,)*[\s]+[\d]+)")
    regex3=re.compile("([\d]+)")
    words=[]
    semantics=[]
    tokenized=nltk.word_tokenize(text)
    s=st.tag(tokenized)
    for item in s:
        entity=item[0].lstrip("(u'")
        entity=entity.rstrip("'")
        concept=item[1].lstrip("u'")
        concept=concept.rstrip("'")
        if concept == 'O':
            continue
        words.append(entity)
        semantics.append(concept)
    match=regex.search(text)
    if match:
        uristr=match.group(1)
    else:
        match=regex2.search(text)
        if match:
            uristr = match.group(1)
        else:
            match=regex3.search(text)
            if match:
                uristr =match.group(1)
            else:
                uristr = "None"
    if uristr != "None":
        words.append(uristr)
        semantics.append("DATE")
    concepts_tagged=[]
    for i in range(0,len(words)):
        tup=(words[i],semantics[i])
        concepts_tagged.append(tup)
    return (concepts_tagged)
        
def concept_tagger(text,url):
    data = {'paragraphArray': text}
    # Make a get request to get the latest position of the international space station from the opennotify api.
    r = requests.get(url, params=data)
    # Print the status code of the response.
    # print(r.status_code)
    data = r.text
    data = data.split(",")
    List = []
    for i in range(0, len(data)):
        if "name" in data[i]:
            List.append(data[i])
        if "semanticType" in data[i]:
            List.append(data[i])
        if "uriStr" in data[i]:
            List.append(data[i])
        if "startByte" in data[i]:
            List.append(data[i])
        if "endByte" in data[i]:
            List.append(data[i])
    words = []
    semantics = []
    uristr = []
    startByte=[]
    endByte=[]
    for i in range(0, len(List)):
        if "name" in str(List[i]):
            s = List[i].split(":")
            s[1] = s[1].lstrip("\"")
            s[1] = s[1].rstrip("\"")
            words.append(str(s[1]))
        if "semanticType" in str(List[i]):
            s = List[i].split(":")
            s[1] = s[1].lstrip("\"")
            s[1] = s[1].rstrip("\"")
            semantics.append(str(s[1]))
        if "uriStr" in str(List[i]):
            s = List[i].split(":")
            s[1] = s[1].lstrip("\"")
            s[1] = s[1].rstrip("\"")
            s[2] = s[2].lstrip("\"")
            s[2] = s[2].rstrip("\"")
            text = str(s[1]) + str(s[2])
            uristr.append(text)
        if "startByte" in str(List[i]):
            s = List[i].split(":")
            s[1] = s[1].lstrip("\"")
            s[1] = s[1].rstrip("\"")
            startByte.append(str(s[1]))
        if "endByte" in str(List[i]):
            s = List[i].split(":")
            s[1] = s[1].lstrip("\"")
            s[1] = s[1].rstrip("\"")
            endByte.append(str(s[1]))
    concepts_tagged=[]
    for i in range(0,len(words)):
        tup=(words[i],semantics[i],uristr[i],startByte[i],endByte[i])
        concepts_tagged.append(tup)
    return (concepts_tagged)

def corpus_tagging(corpus,st,filename):
    print len(corpus)
    fh = open(filename, "w")
    count=0
    for line in corpus:
        if count == 0:
            count += 1
            continue
#        try:
#            text = line[1]
#            concept_tagged = ner_tagger(text, st)
#            for concept in concept_tagged:
#                uristr=concept[0]
#                replacement="CONCEPT_"+str(concept[1])+"#"+str(uristr)
#                regex=re.compile('((CONCEPT_([A-Z])*\#))*(%s)'%concept[0])
#                text=re.sub(regex,replacement,text)
#            uristr="He"
#            replacement="CONCEPT_PERSON#"+str(uristr)
#            regex=re.compile('((CONCEPT_([A-Z])*\#))*(%s)'%uristr)
#            text=re.sub(regex,replacement,text)
#            uristr=" he"
#            replacement="CONCEPT_PERSON#"+str(uristr)
#            regex=re.compile('((CONCEPT_([A-Z])*\#))*(%s)'%uristr)
#            text=re.sub(regex,replacement,text)
#            tup=(line[0],text)
#            print tup
#            tagged_corpus.append(tup)
#        except:
#            continue
        try:
            person = "He"
            text = line[1]
            concept_tagged = ner_tagger(text, st)
            used_words=[]
            for concept in concept_tagged:
                if concept[1]=="PERSON":
                    person=concept[0]
                pas=0
                uristr=concept[0]
#                replacement="CONCEPT_"+str(concept[1])+"#"+str(uristr)
                replacement="<"+str(concept[1])+">"+str(uristr)+"</"+str(concept[1])+">"
                for item in used_words:
                    if concept[0] in item:
                        pas=1
                        break
                if pas==0:
                    regex=re.compile('((CONCEPT_([A-Z])*\#))*(%s)'%concept[0])
                    text=re.sub(regex,replacement,text)
                    used_words.append(concept[0])
            uristr="He"
#            replacement="CONCEPT_PERSON#"+str(person)
            replacement="<PERSON>"+str(uristr)+"</PERSON>"
            regex=re.compile('((CONCEPT_([A-Z])*\#))*(%s)'%uristr)
            text=re.sub(regex,replacement,text)
            uristr=" he"
            replacement="<PERSON>"+str(uristr)+"</PERSON>"
            regex=re.compile('((CONCEPT_([A-Z])*\#))*(%s)'%uristr)
            text=re.sub(regex,replacement,text)
            fh.writelines(text+"\n")
        except:
            continue
        
st=StanfordNERTagger("/Users/rakadalal/Downloads/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz","/Users/rakadalal/Downloads/stanford-ner/stanford-ner.jar")    
positive_seed("annotation.csv","born_in_positive_seed.txt","PERSON","LOCATION")
negative_seed("annotation_graduated_from.csv","born_in_negative_seed.txt","PERSON","LOCATION")
corpus=read_corpus_to_list("corpus.csv")
tagged_corpus = corpus_tagging(corpus, st, "sentences.txt")