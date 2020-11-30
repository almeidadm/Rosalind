def main():

  file_name = "CountMutationPoint.txt"
  file = open(file_name, "r")
  my_seq = file.read()
  my_seq = my_seq.split("\n")

  hamming_distance = 0
  for i in range(len(my_seq[0])) :
    if my_seq[0][i] != my_seq[1][i]:
      hamming_distance += 1

  print(hamming_distance)

if __name__ == "__main__":
  main()
