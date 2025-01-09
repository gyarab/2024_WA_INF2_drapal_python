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

if __name__ == '__main__':
    print(split_into_threes('abcdef'))
    print(split_into_threes('abcdefgh'))
    print(split_into_threes(123))
    
    