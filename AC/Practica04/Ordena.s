 .text
	.align 4
	.globl Ordenar
	.type Ordenar,@function
Ordenar:
        # Aqui viene vuestro codigo

		pushl %ebp
		movl %esp, %ebp
		subl $8, %esp							# tenim 2 variables
		pushl %ebx 								# farem servir com a @v
		pushl %esi								# farem servir per j
		pushl %edi								# farem sevir per 0x80000000
		movl $0x80000000, %edi
		movl $0, %eax							# i = 0;
		movl 8(%ebp), %ebx						# @v

for_i:	

		imul $12, %eax, %ecx 					# ecx -> i*12
		cmpl 4(%ebx, %ecx), %edi	
		je fi_for_i
		movl %eax, %esi							# j = i
		incl %esi 								# j = i+1

for_j:

		imul $12, %esi, %edx 					# edx -> j*12
		cmpl 4(%ebx, %edx), %edi	
		je fi_for_j
		movl 4(%ebx, %edx), %edx 				# edx -> v[j].k
		cmpl %edx, 4(%ebx, %ecx) 				# if
		jle fuera_if
		pushl %eax								# guardem eax
		pushl %esi								# j
		pushl %eax								# i
		pushl %ebx								# @v
		call Intercambiar
		addl $12, %esp
		popl %eax								# recuperem eax

fuera_if:

		incl %esi								# j++
		jmp for_j

fi_for_j:

		incl %eax								# i++
		jmp for_i	

fi_for_i:

		popl %edi
		popl %esi
		popl %ebx
		movl %ebp, %esp
		popl %ebp
		ret






