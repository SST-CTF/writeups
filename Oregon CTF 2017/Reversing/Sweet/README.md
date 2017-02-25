Sweet
10

This flag is protected by super secure encryption. Can you crack it?



[bits 32]
main:
mov eax, encrypted_flag
mov esi, 0
loop_head:
xor DWORD [eax], 42
inc eax
inc esi
mov ebx, DWORD [eax]
test ebx, ebx
jnz loop_head

loop_done:
mov eax, 0x04
mov ebx, 0x01
mov ecx, encrypted_flag
mov edx, esi
int 0x80

mov eax, 0x01
int 0x80
encrypted_flag:
db "LFKMQbOFZckG~XKZZONcDki_ZIKAOlKI^EXSW", 0

