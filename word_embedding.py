from nltk import word_tokenize
import gensim
import codecs

def word_embedding(filename, name):
    embedding_text = []
    filepointer = codecs.open(filename, "r", encoding='utf-8')
    filep = filepointer.readlines()
    for line in filep:
        line=line.split(" ")
        line2=""
        for i in range(0,len(line)):
            if "_" not in line[i]:
                text=line[i]
            else:
                word=line[i].split("_")
                text=""
                for j in range(0,len(word)-1):
                    text+=word[j]+" "
            line2+=text+" "
        tokenizedSentence = word_tokenize(line2)
        embedding_text.append(tokenizedSentence)   
    model = gensim.models.Word2Vec(embedding_text, min_count=1, size=200,
                                   iter=7)  # min count = min count to be considered for the words, size = size of NN, degrees of freedom
    print(model)
    model.save(name)
    #    model.save('GE_Data')
    return model


model=word_embedding("Modified_CVE2.txt", "CVE_DATA2")