
if __name__=='__main__':
	file = open('CountingSubsets.txt', 'r')
	n = int(file.read())
	print(2**n % 1000000)
