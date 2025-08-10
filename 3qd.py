def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

word = input("Введите слово или фразу: ")
if is_palindrome(word):
    print(f"'{word}' - это палиндром!")
else:
    print(f"'{word}' - это не палиндром.")