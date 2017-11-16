def find_word(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index +1


it = find_word('This is my example')
next(it)

#another example
def test():
    for i in range(10):
        yield i

it = test()
it2 = iter(it) #list(it)
print(it, it2)
list(it)
list(it2)

def StringToList(object):
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        for x in self.text:
            yield x

it = StringToList('Hello')
iter(it)
