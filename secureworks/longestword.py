

def longestword(myfile):
    try:
        with open(myfile, 'r') as infile:
                  words = infile.read().split()
    except IOError:
        print "Could not read file:", fName
    # Read the file and put the words in an array

    if(len(words)>0):
        max_len = len(max(words, key=len))
    else:
        print("No words were found in " + myfile)    
    # Get the max length of the words in the array
    # If the array is empty, print "No Words were found in file"
    
    wordstwo=[word for word in words if len(word) == max_len]
    # Put longest words in an array
    
    newWords = [x[::-1] for x in wordstwo]
     # Transpose/reverse words into a new array

    if(len(wordstwo)==1):
        print("Longest word")
        print(''.join(wordstwo[0]))
        print("Reversed/Transposed word")
        print(''.join(newWords[0]))
    else:
        print("Longest words")
        print(' '.join(wordstwo))
        print("Reversed/Transposed words")
        print(' '.join(newWords))
    #Print the arrays
    return wordstwo, newWords
    #Also return the 2 arrays in case you need to add them to another function


longestword('test0.txt')
#Run the longest word function with a file.


# Test 0 - The original given test case
# Test 1 - Lorem Ipsum file
# Test 2 - A Blank file
# Test 3 - Longest word contains only special characters
# Test 4 - List of words all the exact same length, upper and lower
# Test 5 - Test case with every special character, number, and letter upper and lower case
# Test 6 - Text of Declaration of Independence
# Test 7 - Use the python file itself, python.py
# Test 8 - A PDF file of a resume
# Test 9 - The Documentation file for this project, Documentation.txt
