def first_word_1(text):
    return text.split(" ")[0]

print(t('first_word_1(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       
print(t('first_word_1(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       
print(t('first_word_1(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))  
print(t('first_word_1(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))  
