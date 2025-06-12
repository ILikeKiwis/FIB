.text
	.align 4
	.globl procesar
	.type	procesar, @function
procesar:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$16, %esp
	pushl	%ebx
	pushl	%esi
	pushl	%edi

# Aqui has de introducir el codigo

	movl $0, %esi								#i
	movl 8(%ebp), %eax							#mata
	movl 12(%ebp), %ebx							#matb
	movl 16(%ebp), %ecx							#n
	imul %ecx, %ecx

for:
	cmpl %esi, %ecx
	jle fi
	movdqa (%eax, %esi), %xmm0					# pasamos 16 numeros de mata a xmm0
	psllq $4, %xmm0								# los multiplicamos por 16
	movdqa %xmm0, (%ebx, %esi)					# los guardamos en matb
	addl $16, %esi
	jmp for

fi: 


# El final de la rutina ya esta programado

	emms	# Instruccion necesaria si os equivocais y usais MMX
	popl	%edi
	popl	%esi
	popl	%ebx
	movl %ebp,%esp
	popl %ebp
	ret
