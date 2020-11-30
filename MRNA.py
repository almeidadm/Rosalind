def inf(protein, cP):
  result = 1
  for i in range(len(protein)):
    result *= cP.get(protein[i])
  result *= 3
  return result

def main():

  cP = {}
  cP['A'] = 4
  cP['R'] = 6
  cP['G'] = 4
  cP['V'] = 4
  cP['D'] = 2
  cP['E'] = 2
  cP['N'] = 2
  cP['T'] = 4
  cP['M'] = 1
  cP['I'] = 3
  cP['R'] = 6
  cP['Q'] = 2
  cP['H'] = 2
  cP['P'] = 4
  cP['L'] = 6
  cP['W'] = 1
  cP['C'] = 2
  cP['Y'] = 2
  cP['S'] = 6
  cP['F'] = 2
  cP['K'] = 2
  cP['Y'] = 2

  file_name = 'InferringmRNAfromProtein.txt'
  file = open(file_name, 'r')
  file = file.read()
  print(inf(file[:-1], cP) % 1000000)

if __name__ == "__main__":
  main()
