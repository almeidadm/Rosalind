import itertools

def dominant_probability(dominant, hetero, recessive):
	N = float(dominant+recessive+hetero)
	return (1 - 1/N/(N-1) * (recessive*(recessive-1) + recessive*hetero + hetero*(hetero-1)/4.))

if __name__ == "__main__":

	file_name = 'MendelsFirstLaw.txt'
	file = open(file_name, 'r')
	file = file.read()
	file = file.split(' ')
	result = round(dominant_probability(int(file[0]), int(file[1]), int(file[2])), 5)
	print (result)

