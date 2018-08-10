#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:30:24 2017
@author: rakadalal
"""

import csv
import nltk
import string

def join_words(words, tag):
    join=''
    words=nltk.word_tokenize(words)
    #print words
    for i in words:
        join=join+"_"+i
    join=join+"_"+tag
    join=join.lstrip("_")
    return join

target=open('Modified_CVE3.txt', 'w')
fd=open('additional_annotation.csv')
reader=csv.reader(fd, delimiter=',')
count=0
line_count=0
for row in reader:
    if count == 0:
        count+=1
        continue
    text=row[0]
    attacker=row[1]
    CVE=str(row[2])
    ExploitTarget=row[3].split(',')
    ExploitTarget = filter(None, ExploitTarget)
    Hardware=row[4].split(',')
    Hardware = filter(None, Hardware)
    Means=row[5].split(',')
    Means = filter(None, Means)
    Product=row[6].split(',')
    Product = filter(None, Product)
    Software=row[7].split(',')
    Software = filter(None, Software)
    Vulnerability=row[8]
    Weakness=row[9].split(',')
    Weakness = filter(None, Weakness)
    Versionnumber=row[10].split(',')
    Versionnumber = filter(None, Versionnumber)
    attacker2 = join_words(attacker,"attacker")
    CVE2 = join_words(CVE,"CVE")
    for i in range(0, len(ExploitTarget)):
        if ExploitTarget[i] in text:
            ExploitTarget2 = join_words(ExploitTarget[i],"ExploitTarget")
            text = string.replace(text,ExploitTarget[i],str(ExploitTarget2))
    for i in range(0, len(Hardware)):
        if Hardware[i] in text:
            Hardware2 = join_words(Hardware[i],"Hardware")
            text = string.replace(text,Hardware[i],str(Hardware2))
    for i in range(0, len(Means)):
        if Means[i] in text:
            Means2 = join_words(Means[i],"Means")
            text = string.replace(text,Means[i],str(Means2))
    for i in range(0, len(Product)):
        if Product[i] in text:
            Product2 = join_words(Product[i],"Product")
            text = string.replace(text,Product[i],str(Product2))
    for i in range(0, len(Software)):
        if Software[i] in text:
            Software2 = join_words(Software[i],"Software")
            text = string.replace(text,Software[i],str(Software2))
    Vulnerability2 = join_words(Vulnerability,"Vulnerability")
    for i in range(0, len(Weakness)):
        if Weakness[i] in text:
            Weakness2 = join_words(Weakness[i],"Weakness")
            text = string.replace(text,Weakness[i],str(Weakness2))
    for i in range(0, len(Versionnumber)):
        if Versionnumber[i] in text:
            Versionnumber2 = join_words(Versionnumber[i],"Versionnumber")
            text = string.replace(text,Versionnumber[i],str(Versionnumber2))
    if (not len(attacker) == 0) and (attacker in text):
        text = string.replace(text,attacker,str(attacker2))
    if (not len(CVE) == 0) and (CVE in text):
        text = string.replace(text,CVE,str(CVE2))
   
    if (not len(Vulnerability) == 0) and (Vulnerability in text):
        text = string.replace(text,Vulnerability,str(Vulnerability2))

    if len(CVE)!=0:
        if "RESERVED" not in text and "REJECT" not in text:
            target.write(text+"\n")
            line_count+=1
    
print line_count