
def insertion_count_step(A):
	count = 0
	for i in range(1, len(A)):
		k = i
		while(k > 0 and A[k] < A[k-1]):
			A[k-1], A[k] = A[k], A[k-1]
			k -= 1
			count += 1
	return count
	
if __name__ == "__main__":
	f = open('/home/ddeam/Downloads/rosalind_ins.txt').read().split('\n')[:-1]
	
	A = [int(i) for i in f[-1].split(' ')]
	
	print(insertion_count_step(A))
	print(A)
