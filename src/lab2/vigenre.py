import re

def check_string(input_string):
    '''
    использование регулярных выражений для проверки ввода текста
    '''
    pattern = r'^[a-zA-Z]+$'

    if re.match(pattern, input_string):
        return True
    else:
        return False

def continue_encrypt():
    '''
    проверка на продолжение работы программы
    '''
    next_operation = input("Хотите продолжить? (yes/no): ")
    if next_operation == "no":
        print("До скорых встреч!")
        return False
    return True

def correct_key(plaintext: str, keyword: str) -> str:
    '''
    функция преобразует ключевое слово к нормальному виду:
    используются только буквы, нет пробелов,
    такого же размера как и (де)шифруемое слово
    '''

    # текст в список
    plaintext_list = [char for char in plaintext]

    # заполнение ключа до размера текста
    keyword_list = []
    while len(plaintext_list) > len(keyword_list):
        for char in keyword:
            keyword_list.append(char)

    result = []
    # счетчик сдвига для ключевого слова
    key_shift = 0
    while len(plaintext_list) > len(result):
        for char in range(len(plaintext_list)):
            # является ли символ буквой
            if plaintext_list[char].isalpha():
                # добавляем соответствующий символ из ключевого слова в результат
                result.append(keyword_list[char - key_shift])
            # добавление пробела вместо символа
            else:
                key_shift += 1
                result.append(' ')

    # собираем ответ в строку и обрезаем до нужного размера
    corrected_keyword = ''.join([char for char in result])[:len(plaintext)]

    return corrected_keyword

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("AaABbBCcC", "lamotrigini")
    'LaMPuSKiK'
    >>> encrypt_vigenere("", "a")
    ''
    """

    # Проверка, если ключевое слово "A" или "a"
    if keyword.upper() == "A":
        return plaintext

    # заполнение ключевого слова до длины текста
    correct_keyword = correct_key(plaintext, keyword)

    # преобразование текста и ключевого слова в список
    plaintext_list = list(plaintext)
    keyword_list = list(correct_keyword)

    # словари shift для ключей
    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    # реализация шифрования
    ciphertext_list = []
    for char in range(len(plaintext_list)):
        # ASCII код текущего символа текста и ключа
        curr_char = ord(plaintext_list[char])

        # маленькие латинские буквы
        if ord('a') <= curr_char <= ord('z'):
            # базированная точка
            offset = ord('a')

            # Ключ преобразуем в значение смещения, регистр не имеет значения
            shift = 0
            for key, value in alphabet.items():
                if keyword_list[char] == key:
                    shift = value

            # закодированная буква
            new_char = chr((curr_char + shift - offset) % 26 + offset)
            ciphertext_list.append(new_char)

        # большие латинские буквы
        elif ord('A') <= curr_char <= ord('Z'):
            # базированная точка
            offset = ord('A')

            # Ключ преобразуем в значение смещения
            shift = 0
            for key, value in alphabet.items():
                if keyword_list[char] == key:
                    shift = value

            # закодированная буква
            new_char = chr((curr_char + shift - offset) % 26 + offset)
            ciphertext_list.append(new_char)

        # остальные символы
        else:
            ciphertext_list.append(plaintext_list[char])

    ciphertext = ''.join(ciphertext_list)
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("CRIOHFETK", "cRINGe")
    'AAABBBCCC'
    >>> decrypt_vigenere("", "a")
    ''
    """
        # Проверка, если ключевое слово "A" или "a"
    if keyword.upper() == "A":
        return ciphertext

    # заполнение ключевого слова до длины текста
    correct_keyword = correct_key(ciphertext, keyword)

    # преобразование текста и ключевого слова в список
    ciphertext_list = list(ciphertext)
    keyword_list = list(correct_keyword)

    # словари shift для ключей
    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    # реализация шифрования
    cipher_list = []
    for char in range(len(ciphertext_list)):
        # ASCII код текущего символа текста и ключа
        curr_char = ord(ciphertext_list[char])

        # маленькие латинские буквы
        if ord('a') <= curr_char <= ord('z'):
            # базированная точка
            offset = ord('a')

            # Ключ преобразуем в значение смещения, регистр не имеет значения
            shift = 0
            for key, value in alphabet.items():
                if keyword_list[char] == key:
                    shift = value

            # закодированная буква
            new_char = chr((curr_char - shift - offset) % 26 + offset)
            cipher_list.append(new_char)

        # большие латинские буквы
        elif ord('A') <= curr_char <= ord('Z'):
            # базированная точка
            offset = ord('A')

            # Ключ преобразуем в значение смещения
            shift = 0
            for key, value in alphabet.items():
                if keyword_list[char] == key:
                    shift = value

            # закодированная буква
            new_char = chr((curr_char - shift - offset) % 26 + offset)
            cipher_list.append(new_char)

        # остальные символы
        else:
            cipher_list.append(ciphertext_list[char])

    plaintext = ''.join(cipher_list)
    return plaintext

# ЗАПРЕТ НА ПРОБЕЛЫ МЕЖДУ СЛОВАМИ В keyword
# главная часть кода
print('Шифр Виженера')

encryption = True
while encryption is True:
    # какие есть операции
    print('Для шифровки текста нажмите 1')
    print('Для расшифровки текста нажмите 2')

    # выбор операции и проверка на адекватность
    choice = input('Выберите нужную операцию (1, 2): ')

    if choice in ('1', '2'):
        # ввод текста для (де)шифрования
        text = input('Введите текст: ')

        # ввод ключа и проверка на адекватность
        key = input('Введите ключ: ')
        if check_string(key):
            print('Ключ подходит')
        else:
            print('Некорректный ввод ключа')

        # вывод ответа
        if choice == '1':
            print(f'Полученный шифр: {encrypt_vigenere(text, key)}')
        elif choice == '2':
            print(f'Полученная расшифровка: {decrypt_vigenere(text, key)}')

        # продолжать или нет?
        encryption = continue_encrypt()
    else:
        print('Некорректный выбор операции')
