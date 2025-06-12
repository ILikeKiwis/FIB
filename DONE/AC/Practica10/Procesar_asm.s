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

	movl $0, %esi 										#i 
	movl 16(%ebp), %ebx 								#n
	imul %ebx, %ebx										#n²
	movl 8(%ebp), %ecx									#mata
	movl 12(%ebp), %edx									#matb

for: 
	cmpl %esi, %ebx
	jle fi
	movb (%ecx, %esi), %al								# mata[i*n+j] -> al
	shlb $4, %al										# al * 16
	movb %al, (%edx, %esi)								# matb[i*n+j] = al
	incl %esi											# ++i
	jmp for

fi :


# El final de la rutina ya esta programado

	popl	%edi
	popl	%esi
	popl	%ebx
	movl %ebp,%esp
	popl %ebp
	ret
