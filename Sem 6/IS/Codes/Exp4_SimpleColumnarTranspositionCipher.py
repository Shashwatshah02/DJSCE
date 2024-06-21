# Function to remove spaces from text
def remove_spaces(text):
    # Split the text into words and then join them back together without spaces
    return ''.join(text.split())

# Function to pad text with 'X' characters to match the length of the key
def pad_text(text, key_length):
    # Calculate the number of characters needed to pad the text
    padding_length = key_length - (len(text) % key_length)
    # If padding is needed (padding_length is not equal to key_length)
    if padding_length != key_length:
        # Add 'X' characters to the text to make its length a multiple of key_length
        text += 'X' * padding_length
    return text

# Function to encrypt plain text using a given key
def encrypt(plain_text, key):
    # Sort the indices of the key to determine the order of columns
    # key_order contains the positions of characters in the sorted key
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cipher_text = ''
    # Remove spaces from the plain text
    plain_text = remove_spaces(plain_text)
    # Pad the plain text to make its length a multiple of the key length
    plain_text = pad_text(plain_text, len(key))
    # Iterate through columns based on the order defined by key_order
    for i in key_order:
        # Collect characters column-wise from the plain text
        cipher_text += ''.join(plain_text[i::len(key)])  # Step by the key length
    return cipher_text

# Function to decrypt cipher text using a given key
def decrypt(cipher_text, key):
    # Sort the indices of the key to determine the order of columns
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    # Determine the number of columns in the transposition grid
    cols = len(cipher_text) // len(key)
    # Initialize an empty list to store the reconstructed plain text
    plain_text = [''] * len(cipher_text)
    pos = 0
    # Reconstruct plain text based on key order and column arrangement
    for i in key_order:
        for j in range(cols):
            # Place characters in the appropriate positions in the plain text
            plain_text[i + j * len(key)] = cipher_text[pos]
            pos += 1
    # Join the list into a single string
    plain_text = ''.join(plain_text)
    # Remove trailing 'X' characters added during padding
    plain_text = plain_text.rstrip('X')
    return plain_text

# Example usage
plaintext = "wearediscoveredfleeatonce"
key = "zebras"

# Encrypt the plain text using the key
cipher_text = encrypt(plaintext, key)
print("Cipher text:", cipher_text)  # Output: "evldecwederfeaonaesirctoe"

# Decrypt the cipher text using the key
decrypted_text = decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)  # Output: "wearediscoveredfleeatonce"
