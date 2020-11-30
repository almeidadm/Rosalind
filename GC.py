def main():

  file_name = "ComputingGCContent.txt"
  file = open(file_name, "r")
  fasta_file = file.read()

  sequencesWithName = fasta_file.split(">")
  if sequencesWithName[0] == '':
    sequencesWithName = sequencesWithName[1:]

  for i in range(len(sequencesWithName)):
    sequencesWithName[i] = sequencesWithName[i][:13] + ' ' + sequencesWithName[i][14:]
    sequencesWithName[i] = sequencesWithName[i].replace("\n", '') 
    
  maxValu = 0
  for i in range(len(sequencesWithName)):
    percent = ((sequencesWithName[i].count('G')+sequencesWithName[i].count('C'))/len(sequencesWithName[i][14:]))*100
    if percent > maxValu:
      i_max = i
      maxValu = percent
    
  print(sequencesWithName[i_max][:13])
  print("%0.6f" % maxValu)
if __name__ == "__main__":
  main()
