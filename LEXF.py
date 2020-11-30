
def Enumerating(Alphabet, n, s):
	if len(s) == n:
		return print(s)
	else:
		for i in Alphabet:
			Enumerating(Alphabet, n, s+i)

if __name__ == '__main__':
	file = open('Enumeratingk-mersLexicographically.txt', 'r')
	file = file.read()
	Alphabet, n = file[:-1].split('\n')
	n = int(n)
	Alphabet = Alphabet.split(' ')
	Enumerating(Alphabet, n, '')
