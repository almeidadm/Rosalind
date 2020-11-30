def verifyStem(stem, arr):
	for i in arr:
		if stem not in i: return False
	return True

def findstem(arr):
	n = len(arr)
	s = arr[0]
	l = len(s)

	res = []
	Max = 0

	for i in range( l) :
		for j in range( i + 1, l + 1) :
			stem = s[i:j]
			if len(stem) >= Max and verifyStem(stem, arr) == True:
				Max = len(stem)
				res.append(stem)
	return res


if __name__ == "__main__":

	file = open('FindingaSharedMotif.txt', 'r')
	fasta = file.read()
	fasta = fasta[1:].split('>')

	for f in range(len(fasta)):
		fasta[f] = fasta[f][:-1].split('\n')
		aux = ''
		print(fasta[f])
		for i in fasta[f]:
			if i[0] != 'R' and i[0] != '':
				aux += i
		fasta[f] = aux

	stems = findstem(sorted(fasta))
	print(stems[-1])
