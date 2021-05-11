def first_word_2(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text
    
print(t('first_word_2(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~6.3 ms
print(t('first_word_2(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~4.7 ms
print(t('first_word_2(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~7.0 ms
print(t('first_word_2(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~2108.4 ms
