
def Union(A, B):
	U = []
	for i in sorted(A+B):
		if i not in U: U.append(i)
	U = str(U)
	U = U.replace('[', '{').replace(']', '}')
	print(U) 

def Intersection(A, B):
	I = []
	for i in A:
		if i in B: I.append(i)
	I = str(I)
	I = I.replace('[', '{').replace(']', '}')
	print(I) 

def Difference(A, B):
	D = []
	for i in A:
		if i not in B: D.append(i)
	D = str(D)
	D = D.replace('[', '{').replace(']', '}')
	print(D)

if __name__=='__main__':
	arq = open('IntroductiontoSetOperations.txt', 'r')
	arq = arq.read()
	arq = arq[:-1].split('\n')
	n = int(arq[0])
	sets = arq[1:]
	for i in range(len(sets)):
		sets[i] = sets[i][1:-1]
		sets[i] = sets[i].split(',')
		sets[i] = [int(j) for j in sets[i]]

	GlobalSet = [i for i in range(1, n+1)]

	Union(sets[0], sets[1])
	Intersection(sets[0], sets[1])
	Difference(sets[0], sets[1])
	Difference(sets[1], sets[0])
	Difference(GlobalSet, sets[0])
	Difference(GlobalSet, sets[1])
