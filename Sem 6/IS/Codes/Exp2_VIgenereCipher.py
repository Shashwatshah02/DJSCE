def vigenere(plaintext, key, encrypt=True):
    # Initialize an empty string to store the result
    result = ""
    # Initialize the index for the key
    key_index = 0
    # Determine the factor for encryption or decryption
    factor = 1 if encrypt else -1

    # Loop through each character in the input plaintext
    for char in plaintext:
        # Check if the character is an alphabetical letter
        if char.isalpha():
            # Convert the character to uppercase to simplify processing
            char = char.upper()
            # Get the corresponding key character (also converted to uppercase)
            key_char = key[key_index % len(key)].upper()
            # Calculate the encrypted/decrypted character using the Vigenère cipher formula
            encrypted_char = chr(((ord(char) + factor * ord(key_char) - 2 * ord('A')) % 26) + ord('A'))
            # Move to the next character in the key
            key_index += 1
            # Append the encrypted/decrypted character to the result
            result += encrypted_char
        else:
            # If the character is not alphabetical, add it unchanged to the result
            result += char

    # Return the final encrypted/decrypted text
    return result

# Get user input for the plaintext to be encrypted
plaintext = str(input("Enter plaintext: "))
# Get user input for the key to be used in encryption/decryption
key = str(input("Enter key: "))

# Encrypt the plaintext using the Vigenère cipher
encrypted_text = vigenere(plaintext, key)
# Decrypt the encrypted text back to the original plaintext
decrypted_text = vigenere(encrypted_text, key, encrypt=False)

# Print the original, encrypted, and decrypted texts
print("Original Text: ", plaintext)
print("Encrypted Text: ", encrypted_text)
print("Decrypted Text: ", decrypted_text)
