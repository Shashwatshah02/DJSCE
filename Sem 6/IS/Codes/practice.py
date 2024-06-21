def gcd(a, b):
    while b!= 0:
        a, b = b, a%b
    return a

def modulo_inverse(e, phi):
    pass

def key_pair(p, q, e):
    if p == q:
        raise ValueError('P and Q cannot be same')
    n = p*q
    phi = p-1 * q-1

    while gcd(e, phi) != 1:
        e += 1

    d = modulo_inverse(e, phi)

    return ((e,n), (d,n))

def encrypt(text, public_key):
    key, n = public_key
    result = pow(text, key, n)
    return result

def decrypt(text, private_key):
    key, n = private_key
    result = pow(text, key, n)
    return result


p = 7
q = 11
e = 13
text = 5

public_key, private_key = key_pair(p, q, e)
print("Public key:", public_key)
print("Private key:", private_key)

encrypted_msg = encrypt(public_key, text)
print("Encrypted message:", encrypted_msg)

# Decrypt the encrypted message using the private key
decrypted_msg = decrypt(private_key, encrypted_msg)
print("Decrypted message:", decrypted_msg)

