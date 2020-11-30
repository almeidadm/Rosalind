
def RabbitsOffspring(Months, Offspring):
	a = 1
	b = 1
	for i in range(2, Months):
		a, b  = b, Offspring*a+b
		##f1, f2 = f1 + k*f2, f1
	return b

def main():

  file_name = 'RabbitsAndRecurrenceRalations.txt'
  file = open(file_name, 'r')

  file = file.read()
  file = file.split(' ')
  print(RabbitsOffspring(int(file[0]), int(file[1])))


if __name__ == '__main__':
  main()
