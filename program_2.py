def word_separator(sentence):

    new_sentence = " "
    new_sentence = new_sentence + sentence[0]
    for x in range(1,len(sentence)):
        word = sentence[x]

        if word.isupper():
            word = word.lower()
            new_sentence = new_sentence + ' '
        new_sentence = new_sentence + word

    return new_sentence.strip()

sentence = "StopAndSmellTheRoses"
new_sentence = word_separator(sentence)
print(new_sentence)

