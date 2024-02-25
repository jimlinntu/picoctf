import hashlib

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
username_name_trial = b"FREEMAN"

hash_indices = [4, 5, 3, 6, 2, 7, 1, 8]

hashes = list(map(lambda idx: hashlib.sha256(username_name_trial).hexdigest()[idx],
                  hash_indices))


answer = key_part_static1_trial + "".join(hashes) + "}"

print(answer)