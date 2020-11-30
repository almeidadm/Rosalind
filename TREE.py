
if __name__ == '__main__':
	file = open('CompletingATree.txt', 'r')
	G = file.read()	
	G = G[:-1].split('\n')
	V = int(G[0])
	E = len(G[1:])
	print(V-E-1) 
