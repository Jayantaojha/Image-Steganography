from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt_message(message, key=None):
    """Encrypt message using AES"""
    if key is None:
        key = get_random_bytes(16)  # AES-128
    
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    key_b64 = base64.b64encode(key).decode('utf-8')
    return f"{iv}:{ct}:{key_b64}"

def decrypt_message(encrypted):
    """Decrypt message using AES"""
    iv, ct, key_b64 = encrypted.split(':')
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')