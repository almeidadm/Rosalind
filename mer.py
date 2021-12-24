
def merge(A, B):
	i = 0
	j = 0
	ans = []
	while(i<len(A) and j <len(B)):
		if(A[i] < B[j]):
			ans.append(A[i])
			i += 1
		else:
			ans.append(B[j])
			j += 1

	while(i < len(A)):
		ans.append(A[i])
		i += 1	

	while(j < len(B)):
		ans.append(B[j])
		j += 1
	
	return ans

if __name__ == "__main__":
	f = open('/home/ddeam/Downloads/rosalind_mer.txt').read().split('\n')[:-1]
		
	A = [int(i) for i in f[1].split(' ')]
	B = [int(j) for j in f[-1].split(' ')]
	
	for i in merge(A, B):
		print(i, end=' ')
	print()
