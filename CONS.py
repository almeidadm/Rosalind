import operator

def mostFreq(A, C, G, T):
  a = {'A' : A, 'C' : C, 'G': G, 'T' : T}
  return max(a.items(), key=operator.itemgetter(1))[0]


def main():

  file = open('ConsensusandProfile.txt', 'r')
  file = file.read()
  file = file.split('>')
  file = file[1:]
  for i in range(len(file)):
    file[i] = file[i].split('\n')
    file[i] = file[i][1:-1]
    file[i] = ''.join(file[i])
  tam = len(file[0])
  Profile = { 'A': [0 for i in range(tam)], 'C' : [0 for i in range(tam)],
 'G' : [0 for i in range(tam)], 'T': [0 for i in range(tam)] }

  for i in range(len(file)):
    for j in range(tam):
      Profile[file[i][j]][j] += 1

  Consensus = ''
  for i in range(tam):
    Consensus += mostFreq(Profile['A'][i], Profile['C'][i], Profile['G'][i], Profile['T'][i])

  print(Consensus)

  print('A:', end = ' ')
  for i in range(tam):
    print(Profile['A'][i], end = ' ')
  print()

  print('C:', end = ' ')
  for i in range(tam):
    print(Profile['C'][i], end = ' ')
  print()

  print('G:', end = ' ')
  for i in range(tam):
    print(Profile['G'][i], end = ' ')
  print()

  print('T:', end = ' ')
  for i in range(tam):
    print(Profile['T'][i], end = ' ')
  print()
if __name__ == "__main__":
  main()
