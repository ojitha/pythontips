def find_word(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index +1


find_word('This is my example')
