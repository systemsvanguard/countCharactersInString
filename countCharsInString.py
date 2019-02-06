# countCharsInString.py

"""
Title: Count the Characters in a String 
Purpose: Simple Python script to count the characters in a string of text.  For example, string **aaabbdcccccf** should yield ***a3b2d1c5f1*** . Similarly, string **hhhhhqqlllllllhhhppp** should yield ***h5q2l7h3p3*** BUT NOT ***h8q2l7p3***.
Coder: Ryan Hunter | GitHub handle: SystemsVanguard | ryan@RyanHunter.org dated 2019-Feb-05
"""
# use a collections.Counter to automatically iterate through the array & count the number of occurrences per character.
from collections import Counter

myStartingString = 'aaabbdcccccf'
# myStartingString = "hhhhhqqlllllllhhhppp" 
# Error! This yields 'h8q217p3' I will fix this very soon.


myCounter = Counter(myStartingString)
# --------->

# Next, create an ordered list with duplicates removed
orderListNoDuplicates =   ''.join([j for i,j in enumerate(myStartingString) if j not in myStartingString[:i]])

# --------->
# for testing only; commented out
# print("Ordered List with no duplicates")
# print(orderListNoDuplicates)
# --------->

print("--- Step 1A ----> ")
print('The starting string is "%s" , and with duplicates removed and order kept, it is "%s". Now we will count the character occurences! '  %  (myStartingString, orderListNoDuplicates) )
print(" ") # for aesthetics only

# ------------->
# for testing only. Commented out.
# print("--- Step 1B ----> ")
# print(myCounter['a'])  # count the number of occurences of the letter 'a'.

"""
print("--- Step 1C ----> ")
for eachLetter in orderListNoDuplicates:
    print('%s%d' % (eachLetter, myCounter[eachLetter]) )
"""
	
print(" ")
print("--- Step 2A ----> ")
# Get the array. Put the members in a horizontal line. Remove the spaces.
finalOutput = ' '.join(str(  '%s%d' % (eachLetter, myCounter[eachLetter])   ) for eachLetter in orderListNoDuplicates).replace(" ", "")  


print(finalOutput)
# --- END ---> 


