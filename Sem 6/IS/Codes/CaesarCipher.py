def caesar_encrypt(text, shift):
    # Initialize an empty string to store the result
    result = ""
    
    # Loop through each character in the input text
    for char in text:
        # Check if the character is an alphabetical letter
        if char.isalpha():
            # Determine the alphabet to use (uppercase or lowercase)
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if char.isupper() else 'abcdefghijklmnopqrstuvwxyz'
            # Find the new position of the character after applying the shift
            shifted = (alphabet.index(char) + shift) % 26
            # Append the shifted character to the result string
            result += alphabet[shifted]
        else:
            # If the character is not alphabetical, add it unchanged to the result
            result += char
            
    # Return the encrypted text
    return result

def caesar_decrypt(text, shift):
    # Decryption is simply encryption with the negative of the original shift
    return caesar_encrypt(text, -shift)

# Get user input for the text to be encrypted
text = str(input("Enter a String: "))
# Define the shift value for the Caesar cipher
shift = 3
# Encrypt the input text using the Caesar cipher
encrypted_text = caesar_encrypt(text, shift)
# Decrypt the encrypted text back to the original text
decrypted_text = caesar_decrypt(encrypted_text, shift)

# Print the original, encrypted, and decrypted texts
print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
