import codecs
import gensim
from nltk.parse.stanford import StanfordDependencyParser
import math
import csv


def model_load(name):
    model = gensim.models.Word2Vec.load(name)
    return model

def cosine_similarity(vectorx, vectory):
    sumxx = 0
    sumxy = 0
    sumyy = 0
    for i in range(0, len(vectorx)):
        sumxx += float(abs(vectorx[i])) * float(abs(vectorx[i]))
        # print sumxx
        sumyy += float(abs(vectory[i])) * float(abs(vectory[i]))
        # print sumyy
        sumxy += float(abs(vectorx[i])) * float(abs(vectory[i]))
        # print sumxy
    if (sumxx != 0 and sumyy != 0):
        similarity = sumxy / float(math.sqrt(sumxx) * math.sqrt(sumyy))
    else:
        similarity = 0
    return similarity


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def dependency_parse(text, sub, obj):
    flag="false"

    path_to_jar = 'stanford-parser-full-2018-02-27/stanford-parser.jar'
    path_to_models_jar = 'stanford-english-corenlp-2018-02-27-models.jar'

    try:
        dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
        sub=sub.split(" ")
        obj=obj.split(" ")
        sub_list=[]
        obj_list=[]
        result = dependency_parser.raw_parse(text)
        dep = result.next()

        dep_parse=(list(dep.triples()))

        for i in dep_parse:
            tup1=i[0]
            tup2=i[2]
            for s in sub:
                if s==tup1[0]:
                    obj_list.append(tup2[0])
                if s==tup2[0]:
                    obj_list.append(tup1[0])
            for o in obj:
                if o==tup1[0]:
                    sub_list.append(tup2[0])
                if o==tup2[0]:
                    sub_list.append(tup1[0])
        if any(element in sub for element in sub_list) or any(element in obj for element in obj_list):
            flag="true"
        elif any(element in sub_list for element in obj_list):
            flag="true"
        else:
            sub_list2=[]
            obj_list2=[]
            for i in dep_parse:
                tup1=i[0]
                tup2=i[2]
                for sub in sub_list:
                    if sub==tup1[0]:
                        sub_list2.append(tup2[0])
                    if sub==tup2[0]:
                        sub_list2.append(tup1[0])
                for obj in obj_list:
                    if obj==tup1[0]:
                        obj_list2.append(tup2[0])
                    if obj==tup2[0]:
                        obj_list2.append(tup1[0])
                if any(element in sub_list for element in obj_list2) or any(element in obj_list for element in sub_list2):
                    flag="true"
                    break
    except:
        flag="true"
    
    return flag    



def vector_creation(corpus, model):
    corpus_vector=[]
    count=0
    filepointer = codecs.open(corpus, 'r',encoding='utf-8')
    filep=filepointer.readlines()
    for line in filep:
        entities=[]
        semantics=[]
        # if count==5:
        #     break
        line=line.split(" ")
        line2=""
        for i in range(0,len(line)):
            if line[i].strip(" ")!="":
                if "_" not in line[i]:
                    text=line[i]
                    line2+=text.strip()+" "
                else:
                    word=line[i].split("_")
                    text=""
                    for j in range(0,len(word)-1):
                        text+=word[j]+" "
                    entities.append(text)
                    if word[j+1]=="Product" or word[j+1]=="Software" or word[j+1]=="Hardware":
                        semantics.append("Product")
                    else:
                        semantics.append(word[j+1])
                    line2+=text.strip()+" "
        count+=1
        # print (entities)
        # print (semantics)
        # print (line2)
        # print ("\n")
        for i in range(0, len(entities)):
            for j in range(i + 1, len(entities)):
                if entities[i] != entities[j] and entities[i] in line2 and entities[j] in line2:
                    vector = 0
                    count2 = 0
                    for item in entities[i].split():
                        try:
                            vector += model.wv[item]
                            count2 += 1
                        except:
                            continue
                    for item in entities[j].split():
                        try:
                            vector += model.wv[item]
                            count2 += 1
                        except:
                            continue
                    if line2.index(entities[i])<line2.index(entities[j]):
                        s = find_between(line2, entities[i], entities[j])
                    else:
                        s = find_between(line2, entities[j], entities[i])
                    for item in s.split():
                        try:
                            vector += model.wv[item]
                            count2 += 1
                        except:
                            continue
                    text = line2.split(" ")
                    sub = str(entities[i]).split(" ")
                    try:
                        a = text.index(sub[0])
                        b = a - 2
                        while (b < a):
                            try:
                                item = text[b]
                                vector += model.wv[item]
                                count2 += 1
                            except:
                                b += 1
                                continue
                            b += 1
                    except:
                        print("HELLO")

                    ob = str(entities[j]).split(" ")
                    try:
                        a = text.index(ob[len(ob) - 1])
                        b = a + 2
                        while (b > a):
                            try:
                                item = text[b]
                                vector += model.wv[item]
                                count2 += 1
                            except:
                                b -= 1
                                continue
                            b -= 1
                    except:
                        print("HELLO")
                    
                    try:
                        vector = vector / count2
                    except:
                        continue
                    
                    tup = (line2, entities[i], entities[j], semantics[i].strip(), semantics[j].strip(), vector)
                    corpus_vector.append(tup)
                    tup = (line2, entities[j], entities[i], semantics[j].strip(), semantics[i].strip(), vector)
                    corpus_vector.append(tup)

    return corpus_vector

def relation_assertion(training, test, threshold):
    counter=0
    results=[]
    for test_item in test:
        score = 0
        relation = ""
        for key in training:
            (domain_range, vector_list)=training[key]
            if (domain_range[0].lower()==test_item[3].lower() and domain_range[1].lower()==test_item[4].lower()):
                flag=dependency_parse(test_item[0], test_item[1], test_item[2])
                print counter
                counter+=1
                if flag=="true":
                    for vector in vector_list:
                        t = cosine_similarity(test_item[5], vector)
                        if t > score:
                            score = t
                            relation = key
        if relation!="":
            if score >= threshold[relation]:
                tup = (test_item[0], test_item[1], test_item[2], relation, score)
                results.append(tup)

    return results

def writing_results(results):
    writing={}

    fileVul = open("results_hasVulnerability.csv", 'a')
    fileAt = open("results_hasAttacker.csv", 'a')
    filePr = open("results_hasProduct.csv", 'a')
    fileMe = open("results_hasMeans.csv", 'a')
    fileCo = open("results_hasConsequences.csv", 'a')

    writing["hasVulnerability"]=fileVul
    writing["hasAttacker"]=fileAt
    writing["hasProduct"]=filePr
    writing["hasMeans"]=fileMe
    writing["hasConsequences"]=fileCo

    # for key in writing:
    #     writer = csv.writer(writing[key])
    #     new_row = ["Text", "Subject", "Object", "Relation", "Confidence Score"]
    #     writer.writerow(new_row)

    for item in results:
        new_row = [item[0], item[1], item[2], item[3], item[4]]
        writer=csv.writer(writing[item[3]])
        writer.writerow(new_row)

def extraction_phase(annotated_corpus, model, threshold, VGS_table):
    corpus_vector=vector_creation(annotated_corpus, model)
    print len(corpus_vector)
    results=relation_assertion(VGS_table, corpus_vector, threshold)
    print (len(results))
    writing_results(results)
    
    







