
alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ., ?!0123456789'


def remove_duplicates(input_string):
    unique_chars = set()
    result = ""
    for char in input_string:
        if char not in unique_chars:
            unique_chars.add(char)
            result += char
    return result


# def checking(letter):
#     if letter in alph:
#         return True
#     return False


def creating_table(keyword):
    res = remove_duplicates(keyword + alph)
    alph_len = len(alph)//4
    table = [res[i:i + alph_len] for i in range(0, len(res), alph_len)]
    return table


def new_num(y, x, table):
    if (len(table[y]) < x) or (y == 3):
        return 0
    return y + 1


def cipher(word, table):
    def exchange(letter):
        for i in range(0, len(alph)//4):
            for num, ch in enumerate(table[i]):
                if ch == letter:
                    return table[new_num(i, num, table)][num]
    res = ''
    for char in word:
        if char in alph:
            res += exchange(char)
    return res


def main():
    key = input('Введите ключевую фразу или слово:\n').upper()
    word = input('Введите текст для зашифровки:\n').upper()
    table = creating_table(key)
    print(f'Готовый текст:\n{cipher(word, table)}')


if __name__ == '__main__':
    main()
