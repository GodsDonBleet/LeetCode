def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

input_string = input("Enter the string to encrypt: ")
shift_value = int(input("Enter the shift value: "))

encrypted = caesar_cipher(input_string, shift_value)
print("Encrypted string:", encrypted)
