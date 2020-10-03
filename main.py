"""Python for Visual Effects.
Assignment #1 - Data Types and Variables
Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32)
# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
x = 64
y = 32
print(x+y)
# 3.- Make a program that prints a sentence that includes at least 3 variables.
a = "Python "
b = "is "
c = "fun"
print(a +  b  +  c  + "? Probably? Who knows.")
# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sentence = "This is my first Python program"
print(len(sentence))
# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
def res_overscale(l, w):
    return("The 10% overscan of l is " + str(l*1.1) + ", and w is " + str(w*1.1))

print(res_overscale(1920, 1080))