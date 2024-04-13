#Strings are immutable, this means that whenever we want to change a string, it gets changed and is stored in a new variable
a = "!!!Srijan!!!!!!!!!"
b = "!!!Srijan!! !!! Srijan!!!!"
print(a)
print(len(a))
print("Upper case is: ",a.upper()) #converts string to upper case
print("Lower case is: ",a.lower()) #converts string to lower case
print("R strip is: ", a.rstrip("!")) #removes the trailing characters
print("Replace function of a: ",a.replace("Srijan", "John")) #replaces all the occurences of srijan with john
print("Split function of b: ",b.split(" ")) #splits the string where space occurs and stores them into a list
blogheading = "Introduction to js"
print(blogheading.capitalize()) #turns the first letter of the string to uppercase and rest all the letters to lowercase

str1 = "Welcome to the console!!!"
print(str1.center(50)) #center aligns the string

print("Srijan in b occurs: ",b.count("Srijan")) #counts the number of occurences of the string in the parameter in the original string

print(a.endswith("!"))#checks and tells whether the string ends with the given character or not.

print("The first occurence of \"o\" in the blogheading string is at index no:",blogheading.find("o")) #searches for the first occurence of a given value and returns the index position of that value in the string and if the string is not found it returns -1

str1 = "Welcometotheconsole"
print(str1.isalnum()) #returns True if our string contains only aplha numeric character i.e A-Z, a-z and 0-9, if any other characters are present it will return False

str1 = "Welcome"
print(str1.isalpha()) #return true only if all the characters are alphabets

str1 = "                   "
print(str1.isspace()) #returns true only if our string contains white spaces

str2 = "Python is a great programming language"
print(str2.startswith("Python")) #returns true if it starts with the given string or character