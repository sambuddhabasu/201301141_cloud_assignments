section .data
segment .bss
	sum resb 4

section .text
	global _start

_start:
	mov rax, '3'
	sub rax, '0'
	mov rbx, '6'
	sub rbx, '0'
	add rax, rbx
	add rax, '0'
	mov [sum], rax
	mov rcx, sum
	mov rdx, 1
	mov rbx, 1
	mov rax, 4
	int 0x80
	mov rax, 1
	int 0x80
