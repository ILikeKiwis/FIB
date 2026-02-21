.text
	.align 4
	.globl OperaMat
	.type	OperaMat, @function
OperaMat:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$16, %esp
	pushl	%ebx
	pushl	%esi
	pushl	%edi
# Aqui has de introducir el codigo
	movl $0, -4(%ebp)					#res = 0;
	movl $0, %eax						#eax -> i = 0
for_i:
	cmpl $3, %eax
	jge fi_for_i
	movl $0, %ebx 						#ebx -> j = 0
for_j:
	cmpl $3, %ebx
	jge fi_for_j
	imul $12, %eax, %ecx 				#ecx -> i*12 (3*4)
	movl 8(%ebp), %edx					#edx -> &matriz
	addl %ecx, %edx						#edx +=i*12
	movl (%edx, %ebx, 4), %edx			#edx = matriz[i][j]
	addl %edx, -4(%ebp)					#res+= matriz[i][j]
	addl  12(%ebp), %ebx 
	jmp for_j
fi_for_j: 
	addl  12(%ebp), %eax
	jmp for_i
fi_for_i: 
	movl %eax, -8(%ebp)
	movl %ebx, -12(%ebp)

# El final de la rutina ya esta programado
	movl	-4(%ebp), %eax
	popl	%edi
	popl	%esi
	popl	%ebx	
	movl %ebp,%esp
	popl %ebp
	ret
	