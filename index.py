types_of_words = ['nouns', 'verbs', 'adjectives', 'adverbs'] 

original = str(input("Enter ONE word you would like to classify: ")).strip().lower()

for i in range(len(types_of_words)):
    all_words = open('words/'+types_of_words[i]+'.txt')
    line = all_words.readline().replace('\n', '')

    while line:
        line = all_words.readline().replace('\n', '')
        if line == original:
            print("It's a "+types_of_words[i].replace('s', '')+"!")
            break
