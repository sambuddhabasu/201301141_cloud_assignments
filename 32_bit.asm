section .data
segment .bss
	sum resb 4

section .text
	global _start

_start:
	mov eax, '3'
	sub eax, '0'
	mov ebx, '6'
	sub ebx, '0'
	add eax, ebx
	add eax, '0'
	mov [sum], eax
	mov ecx, sum
	mov edx, 1
	mov ebx, 1
	mov eax, 4
	int 0x80
	mov eax, 1
	int 0x80
