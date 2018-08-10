import codecs
import csv


def corpus_preprocessing(): 
    count=0
    filepointer = codecs.open('Modified_CVE2.txt', 'r',encoding='utf-8')
    filep=filepointer.readlines()
    filepointer2 = codecs.open('sentences2.txt', 'w',encoding='utf-8')
    for line in filep:
        count+=1
        # if count<=40:
        #     continue
        line=line.split(" ")
        line2=""
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
                        tag1="<"+"PRODUCT"+">"
                        tag2="</"+"PRODUCT"+">"
                    else:
                        if word[j+1]=="Vulnerability":
                            tag1="<"+"VULNERABILITY"+">"
                            tag2="</"+"VULNERABILITY"+">"
                        else:
                            # tag1="<"+word[j+1].upper()+">"
                            # tag2="</"+word[j+1].upper()+">"
                            tag1=""
                            tag2=""
                    line2+=tag1+text.strip()+tag2+" "
        print (line2.strip())
        filepointer2.write(line2.strip()+"\n")

def positive_seed():
    count=0
    filepointer2 = codecs.open('seeds_positive2.txt', 'w',encoding='utf-8')
    filepointer2.write("e1:PRODUCT\n")
    filepointer2.write("e2:VULNERABILITY\n\n")
    file1 = open("annotation_hasVulnerability.csv", 'r')
    reader = csv.reader(file1)
    for row in reader:
        if len(row)==0:
            continue
        if count == 0:
            count += 1
            continue
        sub=row[1]
        ob=row[2]

        line2=sub+";"+ob
        print (line2.strip())
        filepointer2.write(line2.strip()+"\n")

def negative_seed():
    count=0
    filepointer2 = codecs.open('seeds_negative2.txt', 'w',encoding='utf-8')
    filepointer2.write("e1:PRODUCT\n")
    filepointer2.write("e2:VULNERABILITY\n\n")
    file1 = open("annotation_hasAttacker.csv", 'r')
    reader = csv.reader(file1)
    for row in reader:
        if len(row)==0:
            continue
        if count == 0:
            count += 1
            continue
        sub=row[1]
        ob=row[2]

        line2=sub+";"+ob
        #print (line2.strip())
        filepointer2.write(line2.strip()+"\n")
        

corpus_preprocessing()
positive_seed()
negative_seed()

  