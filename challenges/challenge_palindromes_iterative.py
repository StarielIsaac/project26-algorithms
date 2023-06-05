def is_palindrome_iterative(word):

    if not word:
        return False

    value_first = word[::-1]

    if (value_first == word):
        return True
    else:
        return False
