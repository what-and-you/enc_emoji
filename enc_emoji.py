from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
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

def decrypt_file(encrypted_file_path, key, output_file_path):
    """Mendekripsi file yang terenkripsi dan menyimpan hasilnya ke file baru."""
    with open(encrypted_file_path, 'r') as file:
        encrypted_data = base64.b64decode(file.read())
    iv = encrypted_data[:AES.block_size]
    encrypted_data = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    # Meminta input dari pengguna
    file_path = input("Masukkan path file yang ingin dienkripsi (misalnya /sdcard/filename.txt): ")
    encrypted_file_path = input("Masukkan path untuk menyimpan file terenkripsi (misalnya /sdcard/encrypted_filename.txt): ")
    decrypted_file_path = input("Masukkan path untuk menyimpan file yang didekripsi (misalnya /sdcard/decrypted_filename.txt): ")
    key = os.urandom(16)  # Anda dapat menggunakan kunci tetap jika diinginkan

    # Mengenkripsi file
    encrypted = encrypt_file(file_path, key)
    with open(encrypted_file_path, 'w') as file:
        file.write(encrypted)
    print(f"File terenkripsi disimpan di: {encrypted_file_path}")

    # Mendekripsi file
    decrypt_file(encrypted_file_path, key, decrypted_file_path)
    print(f"File didekripsi disimpan di: {decrypted_file_path}")
