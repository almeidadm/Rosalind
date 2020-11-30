
def main():

  file_name = "FindingAMotifInDNA.txt"
  file = open(file_name, "r")
  my_seq = file.read()
  my_seq, pattern, trash = my_seq.split("\n")

  for i in range(len(my_seq)):
    if my_seq[i: i+len(pattern)] == pattern:
      print(i+1, end = " ")

if __name__ == "__main__":
  main()
