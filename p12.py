from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return ct_bytes, cipher.iv

def decrypt_AES(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plain_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plain_text.decode()

key = get_random_bytes(16)
plain_text = "Hello,world! "
ciphertext, iv = encrypt(plain_text, key)
decrypted_text = decrypt_AES(ciphertext, key, iv)

print("Plain Text:", plain_text)
print("Cipher Text:", ciphertext)
print("Decrypted Text:", decrypted_text)
