# coding= utf-8
import unittest

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
