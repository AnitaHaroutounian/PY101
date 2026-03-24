# In this titlizing example word = word.capitalized wasn't defined before the debugging.
# Since strings are immutable, word.capitalize() won't changethe value of word. We have to reassign it within the condition.

def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()  
        new_words.append(word)   

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))