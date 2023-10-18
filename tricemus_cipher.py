import hashlib

alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ., ?!0123456789'


class Tricemus:
    def __init__(self, table=None, md5_hash=''):
        if table is None:
            table = []
        self.table = table
        self.md5_hash = md5_hash

    def md5_h(self, key):
        res = ''
        self.md5_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
        groups = [self.md5_hash[i:i + 4] for i in range(0, len(self.md5_hash), 4)]
        vals = [(int(group, 16) % len(alph)) for group in groups]
        for i in vals:
            res += alph[i]
        return res

    def creating_table(self, keyword):
        key = self.md5_h(keyword)
        res = remove_duplicates(key + alph)
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
        res = self.gronsfeld_cipher(res)
        res = self.transposition(res)
        return res

    def decipher(self, text):
        res = ''
        text = self.transposition(text)
        text = self.gronsfeld_decipher(text)
        for char in text:
            if char in alph:
                res += self.exchange(char, False)
        return res

    def transposition(self, text):
        key = self.md5_hash
        while len(key) < int(len(text) / 2) + 1:
            key += key
        key = key[:int(len(text) / 2) + 1]
        text_groups = [
            tuple([list(text[i: i + 4]), list(text[i + 4: i + 8])])
            for i in range(0, len(text), 8)
        ]
        hash_groups = [
            list(map(lambda x: bool(int(x, 16) % 2), key[i: i + 4]))
            for i in range(0, len(key), 4)
        ]
        for (fst, snd), hash_group in zip(text_groups, hash_groups):
            for i in range(len(min([fst, snd], key=len))):
                if hash_group[i]:
                    fst[i], snd[i] = snd[i], fst[i]
        flattened_list = []
        for sublist in text_groups:
            for item in sublist:
                flattened_list.extend(item)
        return "".join(flattened_list)

    def gronsfeld_cipher(self, text):
        encrypted_text = ""
        key_length = len(self.md5_hash)

        for i, char in enumerate(text):
            if char in alph:
                shift = int(self.md5_hash[i % key_length], 16)
                idx = alph.index(char)
                new_idx = (idx + shift) % len(alph)
                encrypted_text += alph[new_idx]
            else:
                encrypted_text += char

        return encrypted_text

    def gronsfeld_decipher(self, text):
        decrypted_text = ""
        key_length = len(self.md5_hash)

        for i, char in enumerate(text):
            if char in alph:
                shift = int(self.md5_hash[i % key_length], 16)
                idx = alph.index(char)
                new_idx = (idx - shift) % len(alph)
                decrypted_text += alph[new_idx]
            else:
                decrypted_text += char

        return decrypted_text


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
