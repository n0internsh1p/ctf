import zlib

with open("enc", "rb") as encrypted_file:
    ciphertext = encrypted_file.read()
    ciphertext_length = len(ciphertext)
    plaintext = bytearray(ciphertext_length)
    
    for b1 in range(256):
        key = b""
        key += bytes([b1])
        
        for b2 in range(256):
            key += bytes([b2])
            
            for i in range(36):
                key += zlib.crc32(key).to_bytes(4,'big')

            for i in range(ciphertext_length):
                plaintext[i] = ciphertext[i] ^ key[i+1]
                
            if b'actf{' in plaintext:
                print(plaintext)
            
            key = bytes([key[0]])