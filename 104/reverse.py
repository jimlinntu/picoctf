content = None
# The original code:
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
# 
with open("enc", "r", encoding="utf-8") as f:
    content = f.read()

result = []
for c in content:
    code = ord(c)
    first = chr(code >> 8)
    second = chr(code & (256-1))
    result.append(first)
    result.append(second)

# picoCTF{16_bits_inst34d_of_8_e141a0f7}
print("".join(result))


