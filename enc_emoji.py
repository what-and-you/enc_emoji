# Kamus untuk enkripsi menggunakan emoji (menggunakan 16 emoji untuk mapping hex)
emoji_map = {
    '0': '😀', '1': '😁', '2': '😂', '3': '🤣', '4': '😃', '5': '😄', '6': '😅', '7': '😆',
    '8': '😉', '9': '😊', 'a': '😋', 'b': '😎', 'c': '😍', 'd': '😘', 'e': '😗', 'f': '😙'
}

# Fungsi untuk mengenkripsi teks menjadi emoji menggunakan encoding hexadecimal
def encrypt_to_emoji(text):
    encoded_text = text.encode('utf-8').hex()
    encrypted_text = ''.join([emoji_map[char] for char in encoded_text])
    return encrypted_text

# Fungsi untuk mendekripsi emoji kembali ke teks asli
def decrypt_from_emoji(emoji_text):
    reverse_emoji_map = {v: k for k, v in emoji_map.items()}
    decoded_text = ''.join([reverse_emoji_map[char] for char in emoji_text])
    decrypted_text = bytes.fromhex(decoded_text).decode('utf-8')
    return decrypted_text

# Contoh Penggunaan
if __name__ == "__main__":
    original_script = '''
print("Hello, World!")
print("This is an encrypted script.")
'''

    # Enkripsi script menggunakan emoji
    encrypted_script = encrypt_to_emoji(original_script)
    print(f"Encrypted Script: {encrypted_script}")

    # Dekripsi kembali untuk verifikasi
    decrypted_script = decrypt_from_emoji(encrypted_script)
    print(f"\nDecrypted Script:\n{decrypted_script}")
