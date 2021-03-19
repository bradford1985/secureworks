words = []

def longestword(myfile):
    with open(myfile, 'r') as infile:
              words = infile.read().split()
              #print(words)
    max_len = len(max(words, key=len))
    wordstwo=[word for word in words if len(word) == max_len]
    myWord=wordstwo[0]
    yourWord = myWord[::-1]
    
    
    return  myWord + "\n" + yourWord


print(longestword('test.txt'))







 
