"""
Write a Python program to add 'ing' at the end
of a given string(lenght should be at least 3).
If the given string already ends with 'ing',
add 'ly' instead.If the string lenght of the given string is less than 3, leave it inchanged
"""


# Example:
# work - working
# doing - doingly
# oh - oh

# A parameterised function
def add_string(testString):
    if len(testString)> 2:
        if testString[-3::1] == "ing":
            testString = testString + "ly"
            print(testString)
        else:
            testString = testString + "ing"
            print(testString)
    else:
        print(testString)



# Question 2
# Given any String of odd length greater than 7,
# print out the middle 3 characters line by line
# testString = "Swiss Cottage1"
# Output: C
#         o
#         t

def mid3(testString):
    # Check if the number is odd or even
    # using the modules operator
    if len(testString) % 2 == 1 and len(testString) > 7:
        middleIndex = int((len(testString) - 1) / 2)
        print(testString[middleIndex - 1])
        print(testString[middleIndex])
        print(testString[middleIndex + 1])

mid3("BUBBLETEA")







