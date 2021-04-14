
def round(old_digest, x, r):

    A = old_digest[0]
    B = old_digest[1]
    C = old_digest[2]
    D = old_digest[3]
    E = old_digest[4]
    F = old_digest[5]

    new_digest = bytearray(6)
    
    # computing A
    new_digest[0] = (((C ^ E) & F) + B + (D << 2) + x + r) & 0xFF

    # computing B
    new_digest[1] = A
    
    # computing C
    new_digest[2] = (D << 2) & 0xFF
    
    # computing D
    new_digest[3] = (B >> 5) & 0xFF
    
    # computing E
    new_digest[4] = (A + F) & 0xFF
    
    # computing F
    new_digest[5] = D
    
    return new_digest
    
    
def h_function(digest, x):
    
    for round_number in range(13):
        digest = round(digest, x, round_number)
    return tmp_digest
    
    
def hash(bytes_to_hash):
    
    H = bytearray(b"RITSEC")
    for x in bytes_to_hash:
        H = h_function(H, x)
    return H


# validating the hash's implementation
if hash(b"RITSEC_CTF_2021") == bytes.fromhex("3ba50807aa02"):
    print("hash function working")

# dictionary attack
with open("/usr/share/wordlists/rockyou.txt", "rb") as wordlist:
    for word in wordlist:
        res = hash(word.rstrip(b'\n'))
        if res == bytes.fromhex("435818055906"):
            print("FLAG : RS{" + word + "}")

            
"""
# bruteforce attack

charset = range(0x20, 0x7f)
length = 6


def generate_string(string, depth):
    if depth == 0:
        string[length - 1] = 109 # 'm'
        if hash(string) == b'\x43\x58\x18\x05\x59\x06':
            print(string)
        return
    else:
        for c in charset:
            string[length - depth - 1] = c
            generate_string(string, depth-1)


generate_string(bytearray(length), length-1)
"""
