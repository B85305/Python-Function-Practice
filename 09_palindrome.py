
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


word = input("Enter a word: ")

print(is_palindrome(word))
