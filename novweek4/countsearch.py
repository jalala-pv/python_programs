

def analyze_sentence():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    word_count = len(words)
    print("Number of words in the sentence:",word_count)
    search_word = input("Enter the word to search for: ")
    if search_word in words:
        print("The word ",search_word ,"is found in the sentence.")
    else:
        print("The word ",search_word ," is not found in the sentence.")
analyze_sentence()