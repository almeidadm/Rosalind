from math import factorial

def solve(n, m):
	return (factorial(n)//(factorial(m)*factorial(n-m)))
	
if __name__ == "__main__":
	f = open('/home/ddeam/Downloads/rosalind_aspc.txt').read().split('\n')[:-1][0].split(' ')
	n, m = int(f[0]), int(f[1])
	res = 0

	for k in range(m, n + 1):
		res += solve(n, k)
	print(res%1000000)
	
