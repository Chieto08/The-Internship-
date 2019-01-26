def Pig_Latin():
    sentence = input("Enter a sentence here: ")
    words = sentence.split(" ")
    
    for word in words:
        old_string = word
        old_string = old_string.replace(word[0], " ")
        new_string = old_string + word[0] + "ay"
        word = word.replace(word, new_string)
        print(word, end = "")

Pig_Latin()
        
