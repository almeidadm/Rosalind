from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def main():

  file_name = 'TranslatingRNAintoProtein.txt'
  file = open(file_name, "r")
  messenger_rna = Seq(file.read(), IUPAC.unambiguous_rna)
  print(messenger_rna.translate())

if __name__ == "__main__":
  main()
