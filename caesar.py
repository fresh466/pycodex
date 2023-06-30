"""
caesar.py: Partly generated with ChatGPT as part of the PyCodex project: https://github.com/fresh466/pycodex
"""

import sys

def cae_enc(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def cae_dec(ciphertext, shift):
    return cae_enc(ciphertext, -shift)

def main(argc: int, argv: list[str]):
    if argc != 4:
        print("Usage: caesar.py <-e <plaintext>| -d <ciphertext>> <shift>")
        return 1
    
    shift = int(argv[3])
    if argv[1] == "-e":
        plaintext = argv[2]
        enc_text = cae_enc(plaintext, shift)
        print("Encrypted text:", enc_text)
    elif argv[1] == "-d":
        ciphertext = argv[2]
        dec_text = cae_dec(ciphertext, shift)
        print("Decrypted text:", dec_text)

    return 0


if __name__ == "__main__":
    status = main(len(sys.argv), sys.argv)
    sys.exit(status)
