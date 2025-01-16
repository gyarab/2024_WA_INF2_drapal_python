def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes_in_range(a, b):
    return [x for x in range(a, b) if is_prime(x)]

def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("Invalid argument. 'text' must be a string.")
    return [text[i:i+3] for i in range(0, len(text), 3)]

def caesar_encode(text):
    if not isinstance(text, str):
        raise ValueError("Invalid argument. 'text' must be a string.")
    result = ''
    for c in text:
        if not c.isascii() or c.isdigit():
            raise ValueError("Invalid argument.")
        if c.isalpha():
            ascii_val = ord(c)
            if c.isupper():
                decoded_val = (ascii_val - 65 + 3) % 26 + 65
            else:
                decoded_val = (ascii_val - 97 + 3) % 26 + 97
            result += chr(decoded_val)
        else:
            result += c
    return result

def caesar_decode(text):
    if not isinstance(text, str):
        raise ValueError("Invalid argument. 'text' must be a string.")
    result = ''
    for c in text:
        if not c.isascii() or c.isdigit():
            raise ValueError("Invalid character.")
        if c.isalpha():
            ascii_val = ord(c)
            if c.isupper():
                decoded_val = (ascii_val - 65 - 3) % 26 + 65
            else:
                decoded_val = (ascii_val - 97 - 3) % 26 + 97
            result += chr(decoded_val)
        else:
            result += c
    return result

import unicodedata as ud

def morse(text):
    if not isinstance(text, str):
        raise ValueError("Invalid argument. 'text' must be a string.")
    morse_alphabet = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }
    result = ''
    text = ud.normalize('NFD', text)
    for c in text:
        if c.isalnum():
            result += morse_alphabet[c.upper()] + ' '
        elif c == ' ':
            result += ' / '
    result = result.strip()
    return result

if __name__ == '__main__':
    print(morse("Ahoj světe!"))
    print(morse("A což?"))
    
    