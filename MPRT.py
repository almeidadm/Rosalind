from urllib.request import urlopen
from Bio import SeqIO

def getFasta(response, protein):
  fasta = response.read().decode('utf-8', 'ignore')
  file = open(protein+'.txt', 'w+')
  file.write(fasta)
  file.close()
  file = open(protein+'.txt', 'r')
  fasta = file.read()
  file.close()
  fasta = fasta.split('\n')
  return fasta[:-1]

def parseFasta(fasta, protein):
  index = []
  seq = ''
  for line in fasta:
    if line[0] != '>':
      seq += line
  for i in range(len(seq)):
    if seq[i] == 'N':
      if seq[i+1] != 'P' and seq[i+3] != 'P':
        if seq[i+2] == 'S' or seq[i+2] == 'T':
          index.append(i+1)
  if index != []:
    print(protein)
    for i in index:
      print(i, end = ' ')
    print()


def main():

  file = open('FindingaProteinMotif.txt', 'r')
  file = file.read()
  file = file.split('\n')
  file = file[:-1]
  for protein in file:
    website = 'http://www.uniprot.org/uniprot/' + protein + '.fasta'
    response = urlopen(website)
    fasta = getFasta(response, protein)
    parseFasta(fasta, protein)

if __name__ == '__main__':
  main()

