from cryptography.fernet import Fernet

# Fungsi untuk menghasilkan kunci enkripsi
def generate_key():
    return Fernet.generate_key()

# Fungsi untuk menyimpan kunci enkripsi ke file
def save_key(key, filename):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Fungsi untuk memuat kunci enkripsi dari file
def load_key(filename):
    with open(filename, "rb") as key_file:
        return key_file.read()

# Fungsi untuk mengenkripsi pesan
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Fungsi untuk mendekripsi pesan
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

if __name__ == "__main__":
    # Meminta nama file untuk menyimpan kunci
    key_filename = input("Masukkan nama file untuk menyimpan kunci enkripsi (misalnya 'mykey.key'): ")
    
    # Menghasilkan dan menyimpan kunci enkripsi
    key = generate_key()
    save_key(key, key_filename)
    print(f"Kunci enkripsi disimpan dalam file: {key_filename}")
    
    # Meminta pesan yang akan dienkripsi
    message = input("Masukkan pesan yang ingin dienkripsi: ")
    
    # Mengenkripsi pesan
    encrypted_message = encrypt_message(message, key)
    print(f"Pesan terenkripsi: {encrypted_message.decode()}")

    # Mendekripsi pesan untuk verifikasi
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Pesan setelah didekripsi: {decrypted_message}")
