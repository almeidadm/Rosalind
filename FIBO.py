
def fib(n):
	f1, f2 = 1, 1
	for i in range(2, n):
		f2, f1 =f1, f1+f2
	return f1

if __name__ == '__main__':
	n = int(open("rosalind_fibo.txt").read())
	print(fib(n))
