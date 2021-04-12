from pwn import *

conn = remote("34.69.61.54", 6001)

print_messages = True
print_data = not print_messages

# max padding == 40
# min padding == 25
padding = "30"

message = conn.recvuntil('?')
if print_messages:
    print(message)

conn.sendline(padding)

message = conn.recvuntil("message is\n")
if print_messages:
    print(message)
    
data = bytes.fromhex(conn.recvline().strip(b'\n').decode())
if print_data:
    for i in range(len(data) // 16):
        print(data[i*16:(i+1)*16])
    print("total length : " + str(len(data)))
    print("padding : " + padding)
    
conn.close()