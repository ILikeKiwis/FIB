 .text
	.align 4
	.globl Intercambiar
	.type Intercambiar,@function
Intercambiar:
        # Aqui viene vuestro codigo
		pushl %ebp
		movl %esp, %ebp
		subl $12, %esp
		pushl %ebx
		pushl %esi

		movl 8(%ebp), %ebx 							# ebx -> @v*
		movl 12(%ebp), %ecx							# ecx -> i
		movl 16(%ebp), %edx 						# edx -> j


		imul $12, %ecx, %ecx 						# i*12 -> ecx
		imul $12, %edx, %edx						# j*12 -> edx

		movb (%ebx, %ecx), %al						# al = v[i].c 
		movb %al, -3(%ebp)							# s = al
		
		movb (%ebx, %edx), %ah						# ah = v[j].c
		movb %ah, (%ebx, %ecx)						# v[i].c = ah

		movb %al, (%ebx, %edx)						# v[j].c = s 


		movl 4(%ebx, %ecx), %eax					# eax = v[i].k
		movl %eax, -12(%ebp)						# tmp = eax
		
		movl 4(%ebx, %edx), %esi					# esi = v[j].k
		movl %esi, 4(%ebx, %ecx)					# v[i].k = esi

		movl %eax, 4(%ebx, %edx)					# v[j].k = tmp


		movl 8(%ebx, %ecx), %eax					# eax = v[i].m
		movl %eax, -8(%ebp)							# aux = eax
		
		movl 8(%ebx, %edx), %esi					# esi = v[j].m
		movl %esi, 8(%ebx, %ecx)					# v[i].k = esi

		movl %eax, 8(%ebx, %edx)					# v[j].m = aux

		
		popl %esi
		popl %ebx
		movl %ebp, %esp
		popl %ebp
		ret




		
