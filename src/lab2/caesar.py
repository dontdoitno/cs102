# coding= utf-8
import unittest

def continue_encrypt():
    '''
    проверка на продолжение работы программы
    '''
    next_operation = input("Хотите продолжить? (yes/no): ")
    if next_operation == "no":
        print("До скорых встреч!")
        return False
    return True

# шифрование = смещение на shift символов вперед --> + offset
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        # маленькие латинские буквы
        if 'a' <= char <= 'z':
            # определение базовой точки
            offset = ord('a')
            ciphertext += chr(((ord(char) - offset + shift) % 26) + offset)
        # большие латинские буквы
        elif 'A' <= char <= 'Z':
            # определение базовой точки
            offset = ord('A')
            ciphertext += chr(((ord(char) - offset + shift) % 26) + offset)
        # все остальные символы
        else:
            ciphertext += char
    return ciphertext

# дешифрование = смещение на shift символов назад --> - offset
def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("ABC")
    'XYZ'
    >>> decrypt_caesar("abc")
    'xyz'
    >>> decrypt_caesar("Khoor, Zruog!")
    'Hello, World!'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        # маленькие латинские буквы
        if 'a' <= char <= 'z':
            # определение базовой точки
            offset = ord('a')
            plaintext += chr(((ord(char) - offset - shift) % 26) + offset)
        # большие латинские буквы
        elif 'A' <= char <= 'Z':
            # определение базовой точки
            offset = ord('A')
            plaintext += chr(((ord(char) - offset - shift) % 26) + offset)
        # все остальные символы
        else:
            plaintext += char
    return plaintext

# основная часть кода
print('Шифр Цезаря')

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

        # ввод сдвига и проверка на адекватность
        while True:
            shift = input('Введите количество символов для сдвига: ')

            if shift.isdigit():
                shift = int(shift)
                print('Корректный ввод')
                break  # Выходим из цикла, так как ввод корректный
            else:
                print('Повторите ещё')

        # вывод ответа
        if choice == '1':
            print(f'Полученный шифр: {encrypt_caesar(text, shift)}')
        elif choice == '2':
            print(f'Полученная расшифровка: {decrypt_caesar(text, shift)}')

        # продолжать или нет?
        encryption = continue_encrypt()
    else:
        print('Некорректный выбор операции')
