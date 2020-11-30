
def hasEdge(v, w):
	if v[-3:] == w[:3]: return True
	return False

def Overlaps(vertices):
	for i in range(len(vertices)):
		for j in range(len(vertices)):
			if hasEdge(vertices[i][1], vertices[j][1]):
				print(vertices[i][0], vertices[j][0])

if __name__ == '__main__':
	file = open('OverlapGraphs.txt', 'r')
	fasta = file.read()
	fasta = fasta[1:].split('>')

	for f in range(len(fasta)):
		fasta[f] = fasta[f].split('\n')
		aux = [fasta[f][0]]
		seq = ''
		for i in fasta[f][1:-1]:
			seq += i
		aux.append(seq)
		fasta[f] = aux

	Overlaps(fasta)
  
