
def binary_search(A, i, j, k):
	
	if j < i:
		 return -2
	else:
		mid = (i+j)//2
	
		if A[mid] == k:
			return mid
		elif A[mid] < k:
			return binary_search(A, mid+1, j, k)
		elif A[mid] > k:
			return binary_search(A, i, mid-1, k)
		

if __name__ == "__main__":
	f = open('/home/ddeam/Downloads/rosalind_bins.txt').read().split('\n')[:-1]
	print(len(f))
	n = int(f[0])
	m = int(f[1])

	A = [int(i) for i in f[2].split(' ')]
	K = [int(j) for j in f[3].split(' ')]
	
	for k in K:
		ans = binary_search(A, 0, n-1, k)
		print(ans+1, end=' ')
	print()
