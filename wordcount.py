filename = open("twain.txt")


def counting_words(file):

    word_in_poem = {}

    for line in file:
        words = line.rstrip().split(" ")
        for word in words:
            word_in_poem[word] = word_in_poem.get(word,0) + 1
        
    for word, number in word_in_poem.items():
        print(f' {word} {number}')


