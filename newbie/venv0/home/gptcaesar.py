def player_input():
    while True:
        plaintext = input("어떤 문장을 암호화하시겠어요? ")
        return plaintext

def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# 테스트
plaintext = player_input()
shift = 1
encrypted_text = caesar_encrypt(plaintext, shift)
print("암호화된 문자열:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("복호화된 문자열:", decrypted_text)
