alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ., ?!0123456789'


class Tricemus:
    def __init__(self, table=None):
        if table is None:
            table = []
        self.table = table

    def creating_table(self, keyword):
        res = remove_duplicates(keyword + alph)
        alph_len = len(alph) // 4
        self.table = [res[i:i + alph_len] for i in range(0, len(res), alph_len)]
        return

    def new_num(self, y, x, crypt):
        if crypt:
            if (len(self.table[y]) < x) or (y == 3):
                return 0
            return y + 1
        else:
            if (y == 0) and (len(self.table[3]) < x):
                return 2
            elif y == 0:
                return 3
            return y - 1

    def exchange(self, letter, crypt):
        for i in range(0, len(alph) // 4):
            for num, ch in enumerate(self.table[i]):
                if ch == letter:
                    return self.table[self.new_num(i, num, crypt)][num]

    def cipher(self, text):
        res = ''
        for char in text:
            if char in alph:
                res += self.exchange(char, True)
        return res

    def decipher(self, text):
        res = ''
        for char in text:
            if char in alph:
                res += self.exchange(char, False)
        return res


def remove_duplicates(input_string):
    unique_chars = set()
    result = ""
    for char in input_string:
        if char not in unique_chars:
            unique_chars.add(char)
            result += char
    return result


def main():
    cipher = Tricemus()
    key = input('Введите ключевую фразу или слово:\n').upper()
    text = input('Введите текст для зашифровки:\n').upper()
    cipher.creating_table(key)
    res = cipher.cipher(text)
    print(f'Зашифрованный текст: {res}\n')
    print(f'Расшифрованный текст: {cipher.decipher(res)}\n')


if __name__ == '__main__':
    main()
