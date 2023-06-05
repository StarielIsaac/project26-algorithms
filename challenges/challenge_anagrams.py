def is_anagram(first_string, second_string):

    first = mergesort_string(first_string.lower()).lower()
    second = mergesort_string(second_string.lower()).lower()
    # print(first, second)

    if (len(first) > 0 and first == second):
        return (first, second, True)
    else:
        return (first, second, False)


def mergesort_string(string):
    if len(string) <= 1:
        return string

    # Dividir a string ao meio
    middle = len(string) // 2
    left_half = string[:middle]
    right_half = string[middle:]

    # Chamada recursiva para ordenar as duas metades
    sorted_left = mergesort_string(left_half)
    sorted_right = mergesort_string(right_half)

    # Combinar as duas metades ordenadas
    return merge(sorted_left, sorted_right)


def merge(left, right):
    merged = ""
    left_index = 0
    right_index = 0

    # Comparar os caracteres das duas metades e mesclá-los em ordem
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged += left[left_index]
            left_index += 1
        else:
            merged += right[right_index]
            right_index += 1

    # Adicionar os caracteres restantes da metade esquerda (se houver)
    while left_index < len(left):
        merged += left[left_index]
        left_index += 1

    # Adicionar os caracteres restantes da metade direita (se houver)
    while right_index < len(right):
        merged += right[right_index]
        right_index += 1

    return merged


print(is_anagram('amor', 'roma'))
