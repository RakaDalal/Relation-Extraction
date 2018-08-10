import codecs
import csv


def hasVulnerability(filename): 
    count=0
    filepointer = codecs.open('Modified_CVE.txt', 'r',encoding='utf-8')
    filep=filepointer.readlines()
    file = open(filename, 'w')
    writer = csv.writer(file)
    new_row = ["Text", "Subject", "Object", "Domain", "Range"]
    writer.writerow(new_row)
    for line in filep:
        # if count<=40:
        #     continue
        line=line.split(" ")
        line2=""
        sub=""
        obj=""
        for i in range(0,len(line)):
            if line[i].strip()!="":
                if "_" not in line[i]:
                    text=line[i]
                    line2+=text.strip()+" "
                else:
                    word=line[i].split("_")
                    text=""
                    for j in range(0,len(word)-1):
                        text+=word[j]+" "
                    if word[j+1]=="Product" or word[j+1]=="Software" or word[j+1]=="Hardware":
                        sub=text
                    else:
                        if word[j+1]=="Vulnerability":
                            obj=text
                    line2+=text.strip()+" "
        if sub!="" and obj!="":
            new_row=[line2,sub,obj,"Product","Vulnerability"]
            writer.writerow(new_row)
            count+=1
            # if count>=25:
            #     break

def hasAttacker(filename): 
    count=0
    filepointer = codecs.open('Modified_CVE.txt', 'r',encoding='utf-8')
    filep=filepointer.readlines()
    file = open(filename, 'w')
    writer = csv.writer(file)
    new_row = ["Text", "Subject", "Object", "Domain", "Range"]
    writer.writerow(new_row)
    for line in filep:
        # if count<=40:
        #     continue
        line=line.split(" ")
        line2=""
        sub=""
        obj=""
        for i in range(0,len(line)):
            if line[i].strip()!="":
                if "_" not in line[i]:
                    text=line[i]
                    line2+=text.strip()+" "
                else:
                    word=line[i].split("_")
                    text=""
                    for j in range(0,len(word)-1):
                        text+=word[j]+" "
                    if word[j+1]=="Vulnerability":
                        sub=text
                    else:
                        if word[j+1]=="attacker":
                            obj=text
                    line2+=text.strip()+" "
        if sub!="" and obj!="":
            new_row=[line2,sub,obj,"Vulnerability","Attacker"]
            writer.writerow(new_row)
            count+=1
            # if count>=25:
            #     break

def hasProduct(filename): 
    count=0
    filepointer = codecs.open('Modified_CVE.txt', 'r',encoding='utf-8')
    filep=filepointer.readlines()
    file = open(filename, 'w')
    writer = csv.writer(file)
    new_row = ["Text", "Subject", "Object", "Domain", "Range"]
    writer.writerow(new_row)
    for line in filep:
        # if count<=40:
        #     continue
        line=line.split(" ")
        line2=""
        sub=""
        obj=""
        for i in range(0,len(line)):
            if line[i].strip()!="":
                if "_" not in line[i]:
                    text=line[i]
                    line2+=text.strip()+" "
                else:
                    word=line[i].split("_")
                    text=""
                    for j in range(0,len(word)-1):
                        text+=word[j]+" "
                    if word[j+1]=="Vulnerability":
                        sub=text
                    else:
                        if word[j+1]=="Product" or word[j+1]=="Software" or word[j+1]=="Hardware":
                            obj=text
                    line2+=text.strip()+" "
        if sub!="" and obj!="":
            new_row=[line2,sub,obj,"Vulnerability","Product"]
            writer.writerow(new_row)
            count+=1
            # if count>=25:
            #     break


def hasMeans(filename): 
    count=0
    filepointer = codecs.open('Modified_CVE.txt', 'r',encoding='utf-8')
    filep=filepointer.readlines()
    file = open(filename, 'w')
    writer = csv.writer(file)
    new_row = ["Text", "Subject", "Object", "Domain", "Range"]
    writer.writerow(new_row)
    for line in filep:
        # if count<=40:
        #     continue
        line=line.split(" ")
        line2=""
        sub=""
        obj=""
        for i in range(0,len(line)):
            if line[i].strip()!="":
                if "_" not in line[i]:
                    text=line[i]
                    line2+=text.strip()+" "
                else:
                    word=line[i].split("_")
                    text=""
                    for j in range(0,len(word)-1):
                        text+=word[j]+" "
                    if word[j+1]=="Vulnerability":
                        sub=text
                    else:
                        if word[j+1]=="Means":
                            obj=text
                    line2+=text.strip()+" "
        if sub!="" and obj!="":
            new_row=[line2,sub,obj,"Vulnerability","Means"]
            writer.writerow(new_row)
            count+=1
            # if count>=25:
            #     break

def hasConsequences(filename): 
    count=0
    filepointer = codecs.open('Modified_CVE.txt', 'r',encoding='utf-8')
    filep=filepointer.readlines()
    file = open(filename, 'w')
    writer = csv.writer(file)
    new_row = ["Text", "Subject", "Object", "Domain", "Range"]
    writer.writerow(new_row)
    for line in filep:
        # if count<=40:
        #     continue
        line=line.split(" ")
        line2=""
        sub=""
        obj=""
        for i in range(0,len(line)):
            if line[i].strip()!="":
                if "_" not in line[i]:
                    text=line[i]
                    line2+=text.strip()+" "
                else:
                    word=line[i].split("_")
                    text=""
                    for j in range(0,len(word)-1):
                        text+=word[j]+" "
                    if word[j+1]=="Vulnerability":
                        sub=text
                    else:
                        if word[j+1]=="Weakness":
                            obj=text
                    line2+=text.strip()+" "
        if sub!="" and obj!="":
            new_row=[line2,sub,obj,"Vulnerability","Weakness"]
            writer.writerow(new_row)
            count+=1
            # if count>=25:
            #     break


hasVulnerability("annotation_hasVulnerability2.csv")
hasAttacker("annotation_hasAttacker2.csv")
hasProduct("annotation_hasProduct2.csv")
hasMeans("annotation_hasMeans2.csv")
hasConsequences("annotation_hasConsequences2.csv")

