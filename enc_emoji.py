from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os

def encrypt_file(file_path, key):
    """Mengenkripsi file menggunakan AES dan mengonversi hasilnya ke format base64."""
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))
    # Gabungkan IV dan data terenkripsi, lalu encode ke base64
    return base64.b64encode(cipher.iv + encrypted_data).decode()

if __name__ == "__main__":
    file_path = input("Masukkan path file yang ingin dienkripsi (misalnya /sdcard/test.txt): ")
    encrypted_file_path = input("Masukkan path untuk menyimpan file terenkripsi (misalnya /sdcard/encrypted_test.txt): ")
    key = os.urandom(16)  # Kunci AES harus berukuran 16, 24, atau 32 byte
    
    encrypted = encrypt_file(file_path, key)
    with open(encrypted_file_path, 'w') as file:
        file.write(encrypted)
    print(f"File terenkripsi disimpan di: {encrypted_file_path}")
