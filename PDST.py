
def HammingD(seq1, seq2):
	hd = 0
	for i in range(len(seq1)) :
		if seq1[i] != seq2[i]:
			hd += 1

	return ('%.5f' % (hd/len(seq1)))

def DMatrix(seqs):
	M = [[0 for i in range(len(seqs))]for j in range(len(seqs))]
	
	for i in range(len(seqs)):
		M[i][i] = 0

	for i in range(len(seqs)):
		for j in range(i+1, len(seqs)):
			M[i][j] = HammingD(seqs[i], seqs[j])
			M[j][i] = M[i][j]

	for i in range(len(seqs)):
		for j in range(len(seqs)):
			print("%.5f" % float(M[i][j]), end=' ')
		print()

if __name__ == '__main__':
	arq = open('CreatingADistanceMatrix.txt', 'r')
	seqs = arq.read()
	seqs = seqs[1:].split('>')
	for i in range(len(seqs)):
		seqs[i] = seqs[i][seqs[i].find('\n'):]
		seqs[i] = seqs[i].replace('\n', '')

	DMatrix(seqs)
