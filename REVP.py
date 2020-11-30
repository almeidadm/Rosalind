def toComplement(my_seq):
	return my_seq.replace("C", "g").replace("G", "c").replace("A", "t").replace("T", "a").upper()

def isEq(s, q):
  q = q[::-1]
  for i in range(len(s)):
    if s[i] != q[i]:  return False
  return True



def palindromeSubStrs(s):
  Cs = toComplement(s)
  for gap in range(4, 13):

    for i in range(len(s)):
      if i+gap <= len(s):
        if isEq(s[i:i+gap], Cs[i:i+gap]):
          print(i+1, gap)

if __name__ == '__main__':
  file = open('LocatingRestrictionSites.txt', 'r')
  fasta = file.read()
  fasta = fasta.split('\n')
  fasta = fasta[1:-1]
  seq = ''
  for i in fasta:
    seq += i
  palindromeSubStrs(seq)
