from process import *
from corpus_process import *



threshold={}
threshold["hasVulnerability"]=0.9
threshold["hasAttacker"]=0.85
threshold["hasProduct"]=0.9
threshold["hasMeans"]=0.85
threshold["hasConsequences"]=0.85




model = model_load("CVE_DATA2")
VGS_table={}
VGS_table=learning_phase(extract_training_data("annotation_hasVulnerability.csv"),"hasVulnerability",VGS_table,model)
VGS_table=learning_phase(extract_training_data("annotation_hasAttacker.csv"),"hasAttacker",VGS_table,model)
VGS_table=learning_phase(extract_training_data("annotation_hasProduct.csv"),"hasProduct",VGS_table,model)
VGS_table=learning_phase(extract_training_data("annotation_hasMeans.csv"),"hasMeans",VGS_table,model)
VGS_table=learning_phase(extract_training_data("annotation_hasConsequences.csv"),"hasConsequences",VGS_table,model)

print len(VGS_table)

extraction_phase('Modified_CVE3.txt', model, threshold, VGS_table)

