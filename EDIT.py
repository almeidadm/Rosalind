
def edit_distance(str1, str2, m, n):
	print('Entrando na função',m, n, '\n')
	
	if(m == 0):
		print('m==0, retornando')
		return n
	if(n==0):
		print('n==0, retornando')
		return m
		
	
	if str1[m-1] == str2[n-1]:
		print('letra iguais...')
		return edit_distance(str1, str2, m-1, n-1)
		
	print('letras diferentes')
	return 1 + min(edit_distance(str1, str2, m-1, n), edit_distance(str1, str2, m, n-1), edit_distance(str1, str2, m-1, n-1))
	
if __name__ == "__main__":
	seqs = open("rosalind_edit.txt").read().split('\n')[1:3:1]
	#seqs = ['PLEASANTLY', 'MEANLY']
	print(seqs)
	print(edit_distance(seqs[0], seqs[1], len(seqs[0]), len(seqs[1]) ))
