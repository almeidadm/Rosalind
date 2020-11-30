
def Enumerating(Alphabet, n, s, arr):
	if len(s) == n:
		return arr + [s]
	else:
		for i in Alphabet:
			arr = Enumerating(Alphabet, n, s+i, arr)
	return arr

def KmerComposition(Seq):
	kmers = Enumerating(['A', 'C', 'G', 'T'], 4, '', [])
	freq = [0 for i in range(len(kmers))]
	for i in range(len(kmers)):
		for j in range(len(Seq)):
			if Seq[j:j+4] == kmers[i]:	freq[i] += 1
	for i in freq:	print(i, end = ' ')
	print()

if __name__ == '__main__':
	arq = open('K-MerComposition.txt', 'r')
	arq = arq.read()
	i = arq.find('\n')
	arq = arq[i:].replace('\n', '')
	KmerComposition(arq)
