from scipy.special import binom

def setProbAlleles(Gen, Org):
  def p(nOrg, Gen):
    return binom(2**Gen, nOrg) * 0.25**nOrg * 0.75**(2**Gen - nOrg)
  return 1 - sum(p(nOrg, Gen) for nOrg in range(Org))

def main():

  file_name = 'IndependentAlleles.txt'
  file = open(file_name, 'r')
  file = file.read()
  file = file.split(' ')

  print('%0.3f' % setProbAlleles(int(file[0]), int(file[1])))

if __name__ == '__main__':
  main()
