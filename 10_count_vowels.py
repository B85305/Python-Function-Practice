
def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count


word = input("Enter a string: ")

print("Vowel count:", count_vowels(word))

