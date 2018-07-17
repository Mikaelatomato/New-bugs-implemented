def reversestring():
    words = str(input("Please write a sentence: "))
    wordsreversed = " ".join(words.split()[::-1]) # " ".join : puts the items together within a "space" within them (Without it, it would work but dividing the items inside the list)
    return print(wordsreversed) #words.split separates the words and allows to reverse the order (and not the letters) by writing ::-1, if you don't split them, what you would get would be the words, but also, the letters reversed.
reversestring()
