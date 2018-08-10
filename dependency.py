from nltk.parse.stanford import StanfordDependencyParser

path_to_jar = 'stanford-parser-full-2018-02-27/stanford-parser.jar'
path_to_models_jar = 'stanford-english-corenlp-2018-02-27-models.jar'

dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
sub= "Cisco RV110W firewall "
sub=sub.split(" ")
print sub
obj="does not prevent replaying of modified authentication requests"
obj=obj.split(" ")
print obj
sub_list=[]
obj_list=[]
result = dependency_parser.raw_parse('CVE-2014-0683    The web management interface  on the  Cisco RV110W firewall   with  firmware 1.2.0.9 and earlier  , RV215W router with  firmware 1.1.0.5 and earlier  , and CVR100W router with  firmware 1.0.1.19 and earlier    does not prevent replaying of modified authentication requests  , which allows  remote attackers   to  obtain administrative access  by  leveraging the ability to intercept requests , aka Bug IDs CSCul94527 , CSCum86264 , and CSCum86275  .')
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
print sub_list
print obj_list
if any(element in sub for element in sub_list) or any(element in obj for element in obj_list):
	print "yes"
elif any(element in sub_list for element in obj_list):
 	print "yes"
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
			print "yes"
			break
	print sub_list2
	print obj_list2
