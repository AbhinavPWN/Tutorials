def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def palindrome_sen(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    
    return is_palindrome(string)


Word = input('Enter a string to check whether it is palindrome or not ')
if palindrome_sen(Word):
    print(f'{Word} is a palindrome ')
else:
    print(f'{Word} is a not a palindrome ')
