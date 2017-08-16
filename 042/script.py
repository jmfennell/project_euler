#!/usr/bin/env python3

def main():
    word_count = {}
    with open('words.txt') as f:
        for line in f:
            words = line.replace('"', '').split(',')
    for word in words:
        sum = 0
        for letter in word:
            val = ord(letter.lower()) - 96
            sum = sum + val
        word_count[word] = sum
    largest_possible = max(word_count.values())

    triples = []
    for i in range(1,1000):
        triple = ((i+1) * i) / 2
        if (triple > largest_possible):
            break
        triples.append(int(triple))

    triple_words = []
    for word in word_count:
        if word_count[word] in triples:
            triple_words.append(word)
    print (len(triple_words))
if __name__ == '__main__':
    main()