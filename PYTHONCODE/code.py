


def fun(function):
        def uppercase():
                func_word = function()
                word = func_word.upper()
                return word
        return uppercase


def wordfunc():
        return 'This is word'


text = fun(wordfunc)

text()