# had to use str.lstrip() to remove the leading \x00\x00 that results when decoding in this fashion. 
def greet():
    return(str(int("011010000110010101101100011011000110111100100000011101110110111101110010011011000110010000100001", 2).to_bytes(95, "big").decode()).lstrip('\x00'))

print(greet())
