def main():

  file_name = "ComplementingAStrandOfDNA.txt"
  file = open(file_name, "r")
  my_seq = file.read()
  print(my_seq.replace("C", "g").replace("G", "c").replace("A", "t").replace("T", "a").upper()[::-1])

if __name__ == "__main__":
  main()
