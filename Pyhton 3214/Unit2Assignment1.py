'''
MI1890 Advanced Python Programming Assignment 2
In this assignment you will write a recursive function that determines whether or not a string is
a palindrome.
• The empty string is a palindrome, as is any string containing only one character
• Any longer string is a palindrome if its first and last characters
match, and if the string formed by removing the first and last characters is also
a palindrome
.
Write a main program that reads a string from the user. Use your recursive function
to determine whether or not the string is a palindrome. Then display an appropriate
message for the user.
'''

def isPalindrome(word): #main fucntion
    if len(word) == 0: #if the word is a single character its a palindrome
        print(f'{storeWord} is a palindrome') #prints out original input and tells the user its a palindrome
    elif word[0] == word[-1]: #this checks if first and last characters are the same
        return isPalindrome(word[1:-1]) #This removes the first and last character of out string
    else:
        print(f'{word} is not a palindrome') #if there not the same then the word is not a palindrome

rawWord = input("Enter a possible palindrome: ").lower()#gets word from user in lowercase
storeWord = rawWord #Storing the word before i cut it up
word = rawWord.replace(' ', '')#replacing all spaces with nothing(this lets the uses input spaces without affecting weither its a palindrome or not)
isPalindrome(word) #calls function