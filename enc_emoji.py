import base64

def encrypt_to_hex(text):
    """Mengenkripsi teks menjadi string hex yang dapat dijalankan."""
    # Encode teks ke dalam format base64
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    encoded_str = encoded_bytes.decode("utf-8")

    # Konversi setiap karakter dalam encoded_str menjadi nilai hex
    hex_string = "".join([f"\\x{hex(ord(c))[2:]}" for c in encoded_str])
    
    return hex_string

if __name__ == "__main__":
    # Meminta input teks dari pengguna
    text = input("Masukkan teks yang ingin dienkripsi: ")
    
    # Mengenkripsi teks ke dalam format hex
    encrypted_hex = encrypt_to_hex(text)
    
    # Mencetak hasil enkripsi
    print("\nTeks terenkripsi:")
    print(f'contoh = ""')
    for i in range(0, len(encrypted_hex), 10):
        print(f'contoh += "{encrypted_hex[i:i+10]}"')
    print('exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode(contoh.encode()))')
