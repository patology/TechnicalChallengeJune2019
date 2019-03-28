import re
#module incliuded in the python library for executing searches

#intitializing variables
all_docs = ['.pdf', '.txt', '.ppt']

#defining a function called documents to scan through the files using .read 
def documents_with_a(): 
  
 #an array consisting all the documents to search fromif all_docs:
x1 = []  
      #checking if files are readable format
      if f.mode == 'r':
          
          #invoking a findall to find a
          f = re.findall('a', all_docs)
           x1.append (f)
      
    return x1
  
#end of function documents
documents_with_a() 

#output to print out only documents with letter 'a'
print (documents_with_a()) 
