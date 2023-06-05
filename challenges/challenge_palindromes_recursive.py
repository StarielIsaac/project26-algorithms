def is_palindrome_recursive(word, low_index, high_index):
    # condição de parada

    if len(word) == 0:
        return False

    if low_index >= high_index:
        return True

    # se a primeira letra for igual a ultima, chama novamente a chamada
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False


print(is_palindrome_recursive('arara', 1, 3))
