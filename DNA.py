
def main():

  file_name = 'CountNucleotidesDNA.txt'
  file = open(file_name, 'r')
  my_seq = file.read()
  print(my_seq.count('A'), my_seq.count('C'), my_seq.count('G'), my_seq.count('T'))

if __name__ == "__main__":
  main()
