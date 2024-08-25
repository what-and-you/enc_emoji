import base64

def encrypt_text(text, key):
    """Mengenkripsi teks menggunakan XOR dengan kunci dan mengembalikan hasil dalam format base64."""
    encrypted_chars = [chr(ord(c) ^ key) for c in text]
    encrypted_text = ''.join(encrypted_chars)
    return base64.b64encode(encrypted_text.encode()).decode()

def convert_to_hex(data):
    """Mengonversi data base64 ke format hex string."""
    return ''.join(f"\\x{b:02x}" for b in base64.b64decode(data))

def encrypt_file(file_path, key):
    """Mengenkripsi file dengan XOR dan mengembalikan hasil dalam format hex."""
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_base64 = encrypt_text(file_data.decode(errors='ignore'), key)
    return convert_to_hex(encrypted_base64)

if __name__ == "__main__":
    # Meminta input dari pengguna
    file_path = input("Masukkan path file yang ingin dienkripsi (misalnya /sdcard/filename.txt): ")
    key = int(input("Masukkan kunci (integer): "))

    # Mengenkripsi file
    encrypted_hex = encrypt_file(file_path, key)
    
    # Mencetak hasil enkripsi dalam format yang diinginkan
    print("\nFile terenkripsi:")
    print(f'contoh = ""')
    for i in range(0, len(encrypted_hex), 50):
        print(f'contoh += "{encrypted_hex[i:i+50]}"')
    print('exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode(contoh.encode()))')
