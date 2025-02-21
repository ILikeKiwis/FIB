.text
	.align 4
	.globl OperaVec
	.type	OperaVec, @function
OperaVec:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$16, %esp
	pushl	%ebx
	pushl	%esi
	pushl	%edi
	movl	8(%ebp), %eax
	movl	(%eax), %eax			# Vector[0] -> eax
	movl	%eax, -4(%ebp)			# res = Vector[0]
# Aqui has de introducir el codigo
	movl $1, %eax					# i = 1
	
for:
	cmpl 12(%ebp), %eax				# i < elementos
	jge fuera						
	movl 8(%ebp), %ebx				# ebx = &vector
	movl (%ebx, %eax, 4), %ebx		# ebx = vector[i]
	cmpl %ebx, -4(%ebp) 		
	jge fi_for						# vector[i] < res
	movl %ebx, -4(%ebp)

fi_for:
	incl %eax
	jmp for

fuera:
	movl %eax, -8(%ebp)

# El final de la rutina ya esta programado
	movl	-4(%ebp), %eax
	popl	%edi
	popl	%esi
	popl	%ebx
	movl %ebp,%esp
	popl %ebp
	ret
