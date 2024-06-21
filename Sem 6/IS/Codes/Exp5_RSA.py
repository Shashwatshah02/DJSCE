# Function to calculate the Greatest Common Divisor (GCD) of a and b
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate the Modular Inverse of a modulo m
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to check if a number n is prime
def is_prime(n):
    if n < 2:  # Corrected to handle numbers less than 2
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to the square root of n
        if n % i == 0:
            return False
    return True

# Function to generate RSA key pairs
def generate_keypair(p, q, e):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime")
    elif p == q:
        raise ValueError("p and q cannot be equal")
    
    n = p * q  # Calculate n (the modulus)
    phi = (p - 1) * (q - 1)  # Calculate Euler's totient function phi(n)
    
    # Ensure that e is coprime with phi
    while gcd(e, phi) != 1:
        e += 1
    
    # Compute d, the modular inverse of e modulo phi
    d = mod_inverse(e, phi)
    
    # Public key (e, n) and private key (d, n)
    return ((e, n), (d, n))

# Function to encrypt plaintext using the public key
def encrypt(public_key, plaintext):
    key, n = public_key
    encrypted_msg = pow(plaintext, key, n)  # Encrypt the plaintext using modular exponentiation
    return encrypted_msg

# Function to decrypt ciphertext using the private key
def decrypt(private_key, encrypted_msg):
    key, n = private_key
    decrypted_msg = pow(encrypted_msg, key, n)  # Decrypt the ciphertext using modular exponentiation
    return decrypted_msg

# User input for prime numbers p and q, and encryption exponent e
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
e = int(input("Enter a value for e: "))
plaintext = int(input("Enter the plaintext to encrypt (as a number): "))

# Generate RSA key pairs
public_key, private_key = generate_keypair(p, q, e)
print("Public key:", public_key)
print("Private key:", private_key)

# Encrypt the plaintext using the public key
encrypted_msg = encrypt(public_key, plaintext)
print("Encrypted message:", encrypted_msg)

# Decrypt the encrypted message using the private key
decrypted_msg = decrypt(private_key, encrypted_msg)
print("Decrypted message:", decrypted_msg)
