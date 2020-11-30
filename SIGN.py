import itertools

def SignedPermutations(n):
	permutation = []
	nr = 0
	for i in itertools.permutations(list(range(1, n + 1))):
		for j in itertools.product([-1, 1], repeat=len(i)):
			perm = [a * sign for a, sign in zip(i, j)]
			permutation.append(perm)
			nr += 1

	print(nr)

	for i in permutation:
		for j in i: print(j, end = ' ')
		print()


if __name__ == '__main__':
	file = open('EnumeratingOrientedGeneOrderings.txt', 'r')
	file = file.read()
	n = int(file[0])
	SignedPermutations(n)
