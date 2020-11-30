
def FindingaSplicedMotif(A, B):
	indx = []
	indx.append(A.find(B[0]))
	if indx[-1] == -1: return
	for i in range(1, len(B)):
		j = A.find(B[i], indx[-1]+1)
		if j == -1: return
		indx.append(j)
	for i in indx: print(i+1, end=' ')
	print()

if __name__ == '__main__':
	file = open('FindingaSplicedMotif.txt', 'r')
	file = file.read()
	file = file[1:-1].split('>')
	for s in range(len(file)):
		i = file[s].find('\n')
		file[s] = file[s][i:]
		file[s] = file[s].replace('\n', '')
	A, B = file[0], file[ 1]
	FindingaSplicedMotif(A, B)
