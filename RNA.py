def main():

  file_name = "TranscribingDNAintoRNA.txt"
  file = open(file_name, 'r')
  my_seq = file.read()
  print(my_seq.replace('T', 'U'))

if __name__ == "__main__":
  main()
