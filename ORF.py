string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

traL =  string.split()
codonTable = dict(zip(traL[0::2], traL[1::2]))

def ReverseComplement(seq):
  return(seq.replace("C", "g").replace("G", "c").replace("A", "t").replace("T", "a").upper()[::-1])

def mRNA(seq):
    return(seq.replace('T', 'U'))

def tProtein(seq, allProteins):
  start = seq.find("AUG", 0)

  while start != -1:
    protein = ''
    i = start
    while True:
      if i+3>len(seq):
        protein = ''
        break
      if codonTable[seq[i:i+3]] != 'Stop':
        protein += codonTable[seq[i:i+3]]
        i += 3
      elif codonTable[seq[i:i+3]] == 'Stop':
        break
      else:
        protein = ''
        break
    if protein != '' and protein not in allProteins:
      allProteins.append(protein)
    start = seq.find('AUG', start+1)

def main():

  file = open('OpenReadingFrames.txt', 'r')
  fasta = file.read()
  fasta = fasta.split('\n')
  fasta = fasta[1:-1]
  seq = ''

  for i in fasta:
    seq += i

  allProteins = []

  RNAseq = mRNA(seq)
  tProtein(RNAseq, allProteins)
  Cseq = ReverseComplement(seq)
  RNACseq = mRNA(Cseq)
  tProtein(RNACseq, allProteins)

  for p in allProteins:
    print(p)

if __name__ == '__main__':
  main()
