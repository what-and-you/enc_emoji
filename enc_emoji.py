import base64

# Kamus untuk enkripsi menggunakan emoji
emoji_map = {
    'a': '😀', 'b': '😁', 'c': '😂', 'd': '🤣', 'e': '😃', 'f': '😄', 'g': '😅', 'h': '😆', 'i': '😉', 'j': '😊',
    'k': '😋', 'l': '😎', 'm': '😍', 'n': '😘', 'o': '😗', 'p': '😙', 'q': '😚', 'r': '☺️', 's': '🙂', 't': '🤗',
    'u': '🤩', 'v': '🤔', 'w': '🤨', 'x': '😐', 'y': '😑', 'z': '😶',
    'A': '😏', 'B': '😣', 'C': '😥', 'D': '😮', 'E': '🤐', 'F': '😯', 'G': '😪', 'H': '😫', 'I': '😴', 'J': '😌',
    'K': '😛', 'L': '😜', 'M': '😝', 'N': '🤤', 'O': '😒', 'P': '😓', 'Q': '😔', 'R': '😕', 'S': '🙃', 'T': '🤑',
    'U': '😲', 'V': '☹️', 'W': '🙁', 'X': '😖', 'Y': '😞', 'Z': '😟',
    '0': '😤', '1': '😢', '2': '😭', '3': '😦', '4': '😧', '5': '😨', '6': '😩', '7': '🤯', '8': '😬', '9': '😰',
    '+': '😱', '/': '😳', '=': '🤪', '\n': '😵'
}

# Fungsi untuk mengenkripsi teks menjadi emoji
def encrypt_to_emoji(text):
    encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    encrypted_text = ''.join([emoji_map[char] for char in encoded_text])
    return encrypted_text

# Fungsi untuk mendekripsi emoji kembali ke teks
def decrypt_from_emoji(emoji_text):
    reverse_emoji_map = {v: k for k, v in emoji_map.items()}
    decoded_text = ''.join([reverse_emoji_map[char] for char in emoji_text])
    decrypted_text = base64.b64decode(decoded_text).decode('utf-8')
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
