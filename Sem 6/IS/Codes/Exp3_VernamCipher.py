def vernam_encrypt(plaintext, key):
    # Repeat the key if it's shorter than the plaintext
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    encrypted_text = ""
    for p, k in zip(plaintext, key):
        # Convert characters to their corresponding numeric values (0-25)
        p_val = ord(p.lower()) - ord('a')
        k_val = ord(k.lower()) - ord('a')
        # Perform XOR operation and take modulo 26 to stay within the alphabet range
        xor_val = (p_val + k_val) % 26
        # Convert the result back to a character and append to the encrypted text
        encrypted_text += chr(xor_val + ord('a'))
    return encrypted_text

def vernam_decrypt(encrypted_text, key):
    # Repeat the key if it's shorter than the encrypted_text
    key = key * (len(encrypted_text) // len(key)) + key[:len(encrypted_text) % len(key)]
    plaintext = ""
    for e, k in zip(encrypted_text, key):
        # Convert characters to their corresponding numeric values (0-25)
        e_val = ord(e.lower()) - ord('a')
        k_val = ord(k.lower()) - ord('a')
        # Perform XOR operation and take modulo 26 to stay within the alphabet range
        xor_val = (e_val - k_val) % 26
        # Convert the result back to a character and append to the plaintext
        plaintext += chr(xor_val + ord('a'))
    return plaintext

plaintext = str(input("Enter Plaintext: "))
key = str(input("Enter Key: "))
encrypted_text = vernam_encrypt(plaintext, key)
decrypted_text = vernam_decrypt(encrypted_text, key)

print("Encrypted text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
