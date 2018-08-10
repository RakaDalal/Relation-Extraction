import csv
import gensim

def model_load(name):
    model = gensim.models.Word2Vec.load(name)
    return model

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


def extract_training_data(filename):
    training_data = []
    count = 0
    file1 = open(filename, 'r')
    reader = csv.reader(file1)
    for row in reader:
        if len(row)==0:
            continue
        if count == 0:
            count += 1
            continue
        tup = (row[0], row[1], row[2], row[3], row[4])
        training_data.append(tup)
    return training_data


def domain_range_learning(training_data):
    sub_ob= {}
    for row in training_data:
        Subject=row[3]
        Object=row[4]

        text=str(Subject)+"_"+str(Object)
        if text in sub_ob:
            sub_ob[text]+=1
        else:
            sub_ob[text]=1
    domain_range=max(sub_ob, key=sub_ob.get)
    domain_range=domain_range.split("_")
    tup=(domain_range[0],domain_range[1])
    return tup

def vector_dict(training_data, model):
    vector_list=[]
    for tup in training_data:
        vector = 0
        count = 0
        for word in tup[1].split(" "):
            if word != "" and word != "?":
                try:
                    vector += model.wv[word]
                    count += 1
                except:
                    continue
        for word in tup[2].split(" "):
            if word != "" and word != "?":
                try:
                    vector += model.wv[word]
                    count += 1
                except:
                    continue
        if tup[0].index(tup[1])<tup[0].index(tup[2]):
            s= find_between(tup[0],tup[1],tup[2])
        else:
            s= find_between(tup[0],tup[2],tup[1])
        for word in s.split(" "):
            try:
                vector += model.wv[word]
                count += 1
            except:
                continue
        text=tup[0].split(" ")
        sub=tup[1].split(" ")
        try:
            i=text.index(sub[0])
            j=i-2
            while(j<i):
                try:
                    word=text[j]
                    vector += model.wv[word]
                    count += 1
                except:
                    j+=1
                    continue
                j+=1
        except:
            print ("HELLO")
        ob = tup[2].split(" ")
        try:
            i = text.index(ob[len(ob)-1])
            j = i + 2
            while (j > i):
                try:
                    word = text[j]
                    vector += model.wv[word]
                    count += 1
                except:
                    j -= 1
                    continue
                j -= 1
        except:
            print("HELLO")
        if count > 0:
            vector = vector / count
            vector_list.append(vector)
    return (vector_list)

def learning_phase(training_data,relation,VGS_table,model):
    domain_range=domain_range_learning(training_data)
    vector_list=vector_dict(training_data, model)
    tup=(domain_range, vector_list)
    VGS_table[relation]=tup
    return (VGS_table)


