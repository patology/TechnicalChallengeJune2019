import re
#module incliuded in the python library for executing searches

all_docs = []
#an array consisting all the documents to search from

def documents (): #defining a function called documents to scan through the documents
if all_docs:
x1 = re.findall (a"^\w+",all_docs)
print (x1)
documents () #end of function documents

print (all_docs) #output to print out only documents with letter 'a'
