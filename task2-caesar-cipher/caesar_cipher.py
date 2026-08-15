def encrypt_letter(letter, shift):
    if letter.isupper():
        base = 65
    elif letter.islower():
        base = 97
    else:
        return letter
    shifted = (ord(letter) - base + shift) % 26 + base
    return chr(shifted)


def encrypt_message(message, shift):
    result = ""
    for char in message:
        result += encrypt_letter(char, shift)
    return result


def decrypt_letter(letter, shift):
    if letter.isupper():
        base = 65
    elif letter.islower():
        base = 97
    else:
        return letter
    shifted = (ord(letter) - base - shift) % 26 + base
    return chr(shifted)


def decrypt_message(message, shift):
    result = ""
    for char in message:
        result += decrypt_letter(char, shift)
    return result


print("=== Caesar Cipher Tool ===")
message = input("Enter your message: ")
shift = int(input("Enter shift key (number): "))

encrypted = encrypt_message(message, shift)
decrypted = decrypt_message(encrypted, shift)

print("Original Message :", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
