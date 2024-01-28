content = "00000001|0856f160|f7f17110|f7f09dc7|00000000|08570180|00000002|085713d0|085713f0|6f636970|7b465443|306c5f49|345f7435|6d5f6c6c|306d5f79|5f79336e|63343261|36613431|ffd8007d|f7f44af8|f7f17440|41bbf500|00000001|00000000|f7da6ce9|f7f180c0|f7f095c0|f7f09000|ffd80f88|f7d9768d|f7f095c0|08048eca"

words = content.split("|")
concat = bytearray()
for word in words:
    new_word = bytearray.fromhex(word)
    # Looks like we need to flip because the original hex was printed little endian
    # i.e.
    # lowest address ---> highest address
    # |p|i|c|o|
    # will be printed as "ocip"
    # because o from the higest memory address is regarded as the first byte
    # See https://www.wikiwand.com/en/Endianness#Media/File:32bit-Endianess.svg
    new_word.reverse()
    concat.extend(new_word)
print(concat)
