#Program to check if a string is a palindrome.
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = input("Enter string: ")
 
t = reverse(s)
if t==s:
    print("String is palindrome." )
else:
    print("String isn't palindrome." )

