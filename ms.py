
def merge_sort(A):
	if len(A) > 1:
		mid = len(A)//2
		
		l = A[:mid]
		r = A[mid:]
		
		merge_sort(l)
		merge_sort(r)
		
		i = j = k = 0
		
		while i < len(l) and j < len(r):
			if l[i] < r[j]:
				A[k] = l[i]
				i += 1
			else:
				A[k] = r[j]
				j += 1
			k += 1
			
		while(i < len(l)):
			A[k] = l[i]
			i += 1
			k += 1
		while(j < len(r)):
			A[k] = r[j]
			j += 1
			k += 1
			
if __name__ == "__main__":
	f = open('/home/ddeam/Downloads/rosalind_ms.txt').read().split('\n')[:-1]
	
	A = [int(i) for i in f[1].split(' ')]
	
	merge_sort(A)
	
	for i in A:
		print(i, end=' ')
	print()
