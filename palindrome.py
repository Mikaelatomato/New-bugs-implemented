def palindrome():
    word = str(input("Write a word to know if it's palindrome: "))
    possiblepal = word[::-1]
    if word[::] == possiblepal:
        return print("the given word is a palindrome")
    else:
        return print("the given word isn't a palindrome")
palindrome()
