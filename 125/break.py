import subprocess

KEY_LEN = 50000

# encrypted = k ^ flag
encrypted = "51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57"
enc = bytearray.fromhex(encrypted)

num_bytes = len(enc)
print("The length of encrypted: ", num_bytes)

process = subprocess.Popen(["nc", "mercury.picoctf.net", "58913"],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)


remaining_N = KEY_LEN - num_bytes
garbage = "a" * remaining_N
s = "a" * num_bytes
crafted = "{}\n{}\n".format(garbage, s)

stdout, _ = process.communicate(input=crafted.encode())
# Assert the returned encrpyted string should be same length as `ramining_N`
# times 2 because the returned data is in hex format
assert len(stdout.decode().split("Here ya go!")[1].split("\n")[1]) == remaining_N * 2
last = stdout.decode().split("Here ya go!")[-1]
# print("last: ", len(last))
# print("last:", last)
last = last.split("\n")[1]


# Convert hex string to bytes
# decoded = k ^ "aaaa..."
decoded = bytearray.fromhex(last)

# k ^ 'aaaa...' ^ 'aaaa...' should be k
recovered_key = []
for i in range(len(decoded)):
    recovered_key.append(decoded[i] ^ ord(s[i]))

print("recovered_key: ", recovered_key)
print("recovered_key: ", "".join([chr(d) for d in recovered_key]))
debug = "".join([chr(d) for d in recovered_key])
print(ord(debug[0]))
print("recovered_key: ", len(recovered_key))

# encrypted = k ^ flag
# encrypted ^ k ==> k^flag^k ==> flag


flag = []
for i in range(len(enc)):
    flag.append(chr(enc[i] ^ recovered_key[i]))

flag_str = "".join(flag)
print("picoCTF{{}}".format(flag_str))




