"""
vigenere.py: Partly generated with ChatGPT as part of the PyCodex project: https://github.com/fresh466/pycodex
"""

import sys

def vig_enc(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    key = key.upper()

    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char

    return ciphertext


def vig_dec(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    key = key.upper()

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += char

    return plaintext


def main(argc: int, argv: list[str]):
    if argc != 4:
        print("Usage: vigenere.py <-e <plaintext>| -d <ciphertext>> <key>")
        return 1
    
    key = argv[3]
    if argv[1] == "-e":
        plaintext = argv[2]
        enc_text = vig_enc(plaintext, key)
        print("Encrypted text:", enc_text)
    elif argv[1] == "-d":
        ciphertext = argv[2]
        dec_text = vig_dec(ciphertext, key)
        print("Decrypted text:", dec_text)

    return 0


if __name__ == "__main__":
    status = main(len(sys.argv), sys.argv)
    sys.exit(status)
