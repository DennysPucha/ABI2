from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generar claves aleatorias de 16 bytes (128 bits)
key_aes = get_random_bytes(16)
key_twofish = get_random_bytes(16)

plaintext = b"Mensaje a cifrar en multinivel para el ABI de seguridad"

# Padding para asegurar que el texto plano tenga un tamaño múltiplo de 16 bytes
def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

plaintext_padded = pad(plaintext)

# Cifrado AES (capa 1)
cipher_aes = AES.new(key_aes, AES.MODE_ECB)
aes_encrypted = cipher_aes.encrypt(plaintext_padded)

# Cifrado Twofish (capa 2)
cipher_twofish = AES.new(key_twofish, AES.MODE_ECB)
twofish_encrypted = cipher_twofish.encrypt(aes_encrypted)

print("Cifrado multinivel (AES + Twofish):", twofish_encrypted.hex())

# --- Descifrado multinivel para verificar ---
twofish_decrypted = cipher_twofish.decrypt(twofish_encrypted)
aes_decrypted = cipher_aes.decrypt(twofish_decrypted)
plaintext_decrypted = unpad(aes_decrypted)

print("Texto descifrado:", plaintext_decrypted.decode())
