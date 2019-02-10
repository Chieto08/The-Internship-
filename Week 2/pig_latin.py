def pig_latin(sentence):
    words = sentence.split(" ")
    new_sentence = []
    
    for word in words:
        old_string = word
        old_string = old_string.replace(word[0], " ")
        new_string = old_string + word[0] + "ay"
        if new_string != None:
            new_sentence.append(new_string)
    return new_sentence

def print_new_sentence():
    new_sentence = pig_latin("The quick brown fox")
    for item in new_sentence:
        print(item, end = " ")

        
print_new_sentence()
        
