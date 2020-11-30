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

def toRNA(DNA):
  return DNA.replace('T', 'U')

def removeIntrons(DNA, Introns):
  for intron in Introns:
    DNA = DNA.replace(intron, '')
  return DNA

def toProtein(RNA):
  Protein = ''
  for i in range(0,len(RNA)-3, 3):
    Protein += codonTable[RNA[i:i+3]]
  return Protein
    
if __name__ == '__main__':
  file = open('RNASplicing.txt', 'r')
  fasta = file.read()
  fasta = fasta[1:].split('>')
	
  for f in range(len(fasta)):
    fasta[f] = fasta[f][:-1].split('\n')
    aux = ''
		
    for i in fasta[f]:
      if i[0] != 'R' and i[0] != '':
        aux += i
    fasta[f] = aux

  DNA = str(fasta[0])
  Introns = fasta[1:]

  DNA = removeIntrons(DNA, Introns)
  RNA = toRNA(DNA)
  print(toProtein(RNA))
