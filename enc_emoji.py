from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os

def base64url_encode(data):
    """Encode data ke Base64URL."""
    base64_encoded = base64.b64encode(data).decode()
    return base64_encoded.rstrip('=')  # Hapus padding '='

def base64url_decode(data):
    """Decode data dari Base64URL."""
    data += '=' * (-len(data) % 4)  # Tambahkan padding '=' jika diperlukan
    return base64.b64decode(data)

def encrypt_file(file_path, key):
    """Mengenkripsi file menggunakan AES dan mengonversi hasilnya ke format Base64URL."""
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))
    # Gabungkan IV dan data terenkripsi, lalu encode ke Base64URL
    return base64url_encode(cipher.iv + encrypted_data)

if __name__ == "__main__":
    file_path = input("Masukkan path file yang ingin dienkripsi (misalnya /sdcard/script.py): ")
    encrypted_file_path = input("Masukkan path untuk menyimpan file terenkripsi (misalnya /sdcard/encrypted_script.txt): ")
    key = os.urandom(32)  # Kunci AES 256-bit

    encrypted = encrypt_file(file_path, key)
    with open(encrypted_file_path, 'w') as file:
        file.write(encrypted)
    print(f"File terenkripsi disimpan di: {encrypted_file_path}")
    print(f"Simpan kunci ini dengan aman untuk mendekripsi file: {base64url_encode(key)}")
